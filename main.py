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
            save_client(name, last, email)
            print("Cliente guardado.")

        elif op == "2":
            for row in get_clients():
                print(row)

        elif op == "3":
            name = input("Nombre plan: ")
            desc = input("Descripcion: ")
            price = float(input("Precio: "))
            freq = input("Frecuencia (monthly/yearly): ")
            status = input("Status (active/inactive): ")
            save_plan(name, desc, price, freq, status)
            print("Plan guardado.")

        elif op == "4":
            for row in get_plans():
                if row[5] == "active":
                    print(row)

        elif op == "5":
            client_id = int(input("ID cliente: "))
            plan_id = int(input("ID plan: "))
            client = row_to_client(get_client(client_id))
            plan = row_to_plan(get_plan(plan_id))
            sub, invoice = SubscriptionService.activate(client, plan)
            save_subscription(
                client_id, plan_id, sub.date_start, sub.date_end, sub.status, sub.cancellation_requested
            )
            save_invoice(client_id, invoice.broadcast, invoice.expiration, invoice.amount, invoice.status)
            print("Subscription activa. Invoice creada.")

        elif op == "6":
            invoice_id = int(input("ID invoice: "))
            rows = [r for r in get_invoices() if r[0] == invoice_id]
            if not rows:
                print("Invoice no encontrada.")
                continue
            row = rows[0]
            invoice = row_to_invoice(row)
            payment = SubscriptionService.pay_invoice(invoice)
            save_payment(invoice_id, payment.date, payment.amount, payment.method, payment.status)
            update_invoice(invoice_id, row[1], row[2], row[3], row[4], "paid")
            print("Pago registrado. Payment id:", payment is not None and "ok")

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
