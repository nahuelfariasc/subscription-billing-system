class Payment:
    def __init__(self, p_date, p_amount, p_method, p_status):
        self.date = p_date
        self.amount = p_amount
        self.method = p_method
        self.status = "pending"

    def confirm(self):
        if self.status == "confirmed":
            raise ValueError("Payment is already confirmed")

        self.status = "confirmed"

    def reject(self):
        if self.status == "rejected":
            raise ValueError("Payment is already rejected")

        self.status = "rejected"
