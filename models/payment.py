class Payment:
    def __init__(self, p_date, p_amount, p_method, p_invoice = None):
        self.date = p_date
        self.amount = p_amount
        self.method = p_method
        self.status = "pending"
        self.invoice = p_invoice

    def confirm(self):
        if self.status != "pending":
            raise ValueError("Only pending payments can be confirmed")

        self.status = "confirmed"

    def reject(self):
        if self.status != "pending":
            raise ValueError("Only pending payments can be rejected")

        self.status = "rejected"
