import unittest

from database.client_data import get_client, save_client
from database.config_db import connect
from database.invoice_data import save_invoice
from database.mappers import row_to_client, row_to_plan
from database.payment_data import save_payment
from database.plan_data import get_plan, save_plan
from database.subscription_data import save_subscription
from services.subscription_service import SubscriptionService


class TestIntegration(unittest.TestCase):
    def setUp(self):
        conn = connect()
        cur = conn.cursor()
        cur.execute("TRUNCATE payment, invoice, subscription, plan, client CASCADE")
        conn.commit()
        cur.close()
        conn.close()

    def test_full_flow(self):
        client_id = save_client("Ana", "Lopez", "ana@mail.com")
        plan_id = save_plan("Premium", "desc", 1000, "monthly", "active")

        client = row_to_client(get_client(client_id))
        plan = row_to_plan(get_plan(plan_id))

        sub, invoice = SubscriptionService.activate(client, plan)
        save_subscription(client_id, plan_id, sub.date_start, sub.date_end, sub.status, sub.cancellation_requested)
        invoice_id = save_invoice(client_id, invoice.broadcast, invoice.expiration, invoice.amount, invoice.status)

        payment = SubscriptionService.pay_invoice(invoice)
        save_payment(invoice_id, payment.date, payment.amount, payment.method, payment.status)

        self.assertEqual(sub.status, "active")
        self.assertEqual(invoice.status, "paid")
        self.assertEqual(payment.status, "confirmed")


if __name__ == "__main__":
    unittest.main()
