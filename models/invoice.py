from utils.date_utils import get_today


class Invoice:
    def __init__(self, i_broadcast, i_expiration, i_amount, i_status, i_client = None, i_payment = None):
        self.broadcast = i_broadcast
        self.expiration = i_expiration
        self.amount = i_amount
        self.status = i_status
        self.client = i_client
        self.payment = i_payment

    def mark_as_paid(self):
        if self.status == "pending":
            self.status = "paid"

    def mark_as_overdue(self):
        if self.status == "pending" and self.expiration < get_today():
            self.status = "overdue"
