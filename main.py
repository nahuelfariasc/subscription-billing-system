from models.client import Client
from models.plan import Plan
from services.subscription_service import SubscriptionService


def main():
    client = Client("Ana", "Lopez", "ana@mail.com")
    plan = Plan("Premium", "Plan premium", 1000, "monthly", "active")

    sub, invoice = SubscriptionService.activate(client, plan)
    print("Activated:", sub.status, "| Invoice:", invoice.status)

    payment = SubscriptionService.pay_invoice(invoice)
    print("Paid:", invoice.status, "| Payment:", payment.status)

    # cancelación
    sub.cancel()
    print("After cancel:", sub.status, "| requested:", sub.cancellation_requested)

if __name__ == "__main__":
    main()
