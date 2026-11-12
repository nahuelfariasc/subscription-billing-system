import psycopg
from database.client_data import get_client, get_clients, save_client
from database.invoice_data import get_invoices, save_invoice, update_invoice
from database.mappers import row_to_client, row_to_invoice, row_to_plan
from database.payment_data import save_payment
from database.plan_data import get_plan, get_plans, save_plan
from database.subscription_data import get_subscriptions, save_subscription
from services.subscription_service import SubscriptionService


def menu():
    while True:
        print("\n=== S&BM ===")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Agregar plan")
        print("4. Listar planes activos")
        print("5. Activar subscription")
        print("6. Pagar invoice")
        print("7. Listar subscriptions")
        print("8. Listar invoices")
        print("0. Salir")
        op = input("Opcion: ").strip()

        if op == "1":
            name = input("Nombre: ")
            last = input("Apellido: ")
            email = input("Email: ")
            try:
                save_client(name, last, email)
                print("Cliente guardado.")
            except psycopg.errors.UniqueViolation:
                print("Error: Ya existe un cliente registrado con ese email.")

        elif op == "2":
            for row in get_clients():
                print(row)

        elif op == "3":
            name = input("Nombre plan: ").strip()
            desc = input("Descripcion: ").strip()
            try:
                price = float(input("Precio: ").strip())
            except ValueError:
                print("Error: El precio debe ser un número válido.")
                continue

            freq = input("Frecuencia (monthly/yearly): ").strip().lower()
            if freq not in ("monthly", "yearly"):
                print("Error: La frecuencia debe ser 'monthly' o 'yearly'.")
                continue

            status = input("Status (active/inactive): ").strip().lower()
            if status not in ("active", "inactive"):
                print("Error: El status debe ser 'active' o 'inactive'.")
                continue

            try:
                save_plan(name, desc, price, freq, status)
                print("Plan guardado.")
            except Exception as e:
                print(f"Error al guardar el plan: {e}")

        elif op == "4":
            for row in get_plans():
                if row[5] == "active":
                    print(row)

        elif op == "5":
            try:
                client_id = int(input("ID cliente: ").strip())
                plan_id = int(input("ID plan: ").strip())
            except ValueError:
                print("Error: Los IDs deben ser números enteros.")
                continue

            client_row = get_client(client_id)
            if not client_row:
                print(f"Error: No existe ningún cliente con ID {client_id}.")
                continue

            plan_row = get_plan(plan_id)
            if not plan_row:
                print(f"Error: No existe ningún plan con ID {plan_id}.")
                continue

            if plan_row[5] != "active":
                print(f"Error: El plan '{plan_row[1]}' no está activo.")
                continue

            client = row_to_client(client_row)
            plan = row_to_plan(plan_row)
            try:
                sub, invoice = SubscriptionService.activate(client, plan)
                save_subscription(
                    client_id, plan_id, sub.date_start, sub.date_end, sub.status, sub.cancellation_requested
                )
                save_invoice(client_id, invoice.broadcast, invoice.expiration, invoice.amount, invoice.status)
                print("Subscription activa. Invoice creada.")
            except Exception as e:
                print(f"Error al activar la suscripción: {e}")

        elif op == "6":
            try:
                invoice_id = int(input("ID invoice: ").strip())
            except ValueError:
                print("Error: El ID de la invoice debe ser un número entero.")
                continue

            rows = [r for r in get_invoices() if r[0] == invoice_id]
            if not rows:
                print("Invoice no encontrada.")
                continue
            row = rows[0]
            if row[4] == "paid":
                print("Aviso: Esta invoice ya fue pagada anteriormente.")
                continue

            invoice = row_to_invoice(row)
            try:
                payment = SubscriptionService.pay_invoice(invoice)
                save_payment(invoice_id, payment.date, payment.amount, payment.method, payment.status)
                update_invoice(invoice_id, row[1], row[2], row[3], row[4], "paid")
                print("Pago registrado con éxito.")
            except Exception as e:
                print(f"Error al procesar el pago: {e}")

        elif op == "7":
            for row in get_subscriptions():
                print(row)

        elif op == "8":
            for row in get_invoices():
                print(row)

        elif op == "0":
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    menu()
