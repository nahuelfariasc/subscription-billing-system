from models.invoice import Invoice
from models.payment import Payment
from models.subscription import Subscription
from utils.date_utils import get_today


class SubscriptionService:
    @staticmethod
    def activate(client, plan):
        sub = Subscription(None, None, "pending", s_client = client, s_plan = plan)
        sub.activate(get_today())

        invoice = Invoice(
            i_broadcast = get_today(),
            i_expiration = sub.date_end,
            i_amount = plan.price,
            i_status = "pending",
            i_client = client,
        )
        invoice.payment = None

        return sub, invoice

    @staticmethod
    def pay_invoice(invoice, method = "card"):
        payment = Payment(
            p_date = get_today(),
            p_amount = invoice.amount,
            p_method = method,
            p_invoice = invoice,
        )
        payment.confirm()
        invoice.payment = payment
        invoice.mark_as_paid()
        return payment

