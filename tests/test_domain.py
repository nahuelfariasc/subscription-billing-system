import unittest
from datetime import timedelta

from models.client import Client
from models.invoice import Invoice
from models.payment import Payment
from models.plan import Plan
from models.subscription import Subscription
from services.subscription_service import SubscriptionService
from utils.date_utils import get_today


class TestClient(unittest.TestCase):
    def test_valid_email(self):
        c = Client("Ana", "Lopez", "  ANA@Mail.com  ")
        self.assertEqual(c.email, "ana@mail.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            Client("Ana", "Lopez", "bad")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            Client("", "Lopez", "a@b.com")

    def test_update(self):
        c = Client("Ana", "Lopez", "a@b.com")
        c.update(name="Maria", email="m@b.com")
        self.assertEqual(c.name, "Maria")
        self.assertEqual(c.email, "m@b.com")


class TestPlan(unittest.TestCase):
    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Plan("P", "d", 0, "monthly", "active")

    def test_invalid_frequency(self):
        with self.assertRaises(ValueError):
            Plan("P", "d", 10, "weekly", "active")

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            Plan("P", "d", 10, "monthly", "deleted")


class TestSubscription(unittest.TestCase):
    def test_activate_today(self):
        c = Client("A", "B", "a@b.com")
        p = Plan("P", "d", 10, "monthly", "active")
        sub = Subscription(None, None, "pending", s_client=c, s_plan=p)
        sub.activate(get_today())
        self.assertEqual(sub.status, "active")
        self.assertIsNotNone(sub.date_end)

    def test_activate_wrong_date(self):
        sub = Subscription(None, None, "pending")
        with self.assertRaises(ValueError):
            sub.activate(get_today() - timedelta(days=1))

    def test_cancel_deferred(self):
        future = get_today() + timedelta(days=10)
        sub = Subscription(get_today(), future, "active")
        sub.cancel()
        self.assertTrue(sub.cancellation_requested)
        self.assertEqual(sub.status, "active")

    def test_expire(self):
        past = get_today() - timedelta(days=1)
        sub = Subscription(get_today() - timedelta(days=30), past, "active")
        sub.expire()
        self.assertEqual(sub.status, "expired")


class TestInvoicePayment(unittest.TestCase):
    def test_mark_paid(self):
        inv = Invoice(get_today(), get_today(), 100, "pending")
        inv.mark_as_paid()
        self.assertEqual(inv.status, "paid")

    def test_mark_overdue(self):
        past = get_today() - timedelta(days=1)
        inv = Invoice(get_today(), past, 100, "pending")
        inv.mark_as_overdue()
        self.assertEqual(inv.status, "overdue")

    def test_payment_confirm_reject(self):
        pay = Payment(get_today(), 100, "card")
        pay.confirm()
        self.assertEqual(pay.status, "confirmed")
        with self.assertRaises(ValueError):
            pay.reject()

    def test_service_flow(self):
        c = Client("A", "B", "a@b.com")
        p = Plan("P", "d", 10, "monthly", "active")
        sub, inv = SubscriptionService.activate(c, p)
        payment = SubscriptionService.pay_invoice(inv)
        self.assertEqual(sub.status, "active")
        self.assertEqual(inv.status, "paid")
        self.assertEqual(payment.status, "confirmed")
        self.assertIs(inv.payment, payment)


if __name__ == "__main__":
    unittest.main()
