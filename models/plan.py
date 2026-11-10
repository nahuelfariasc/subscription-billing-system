VALID_STATUSES = {"active", "inactive"}
VALID_FREQUENCES = {"monthly", "yearly"}

class Plan:
    def __init__(self, p_name, p_description, p_price, p_frequency, p_status):
        if p_price <=0:
            raise ValueError("Price must be greater than zero")
        if p_frequency not in VALID_FREQUENCES:
            raise ValueError("Invalid frequency")
        if p_status not in VALID_STATUSES:
            raise ValueError("Invalid status")

        self.name = p_name
        self.description = p_description
        self.price = p_price
        self.frequency = p_frequency
        self.status = p_status

    def update(self, name = None, description = None, price = None, frequency = None, status = None):
        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if price is not None:
            if price <= 0:
                raise ValueError("Price must be greater than zero")
            self.price = price

        if frequency is not None:
            if frequency not in VALID_FREQUENCES:
                raise ValueError("Invalid frequency")
            self.frequency = frequency

        if status is not None:
            if status not in VALID_STATUSES:
                raise ValueError("Invalid status")
            self.status = status

