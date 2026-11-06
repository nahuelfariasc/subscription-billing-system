class Plan:
    def __init__(self, p_name, p_description, p_price, p_frequency, p_status):
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
            self.price = price

        if frequency is not None:
            self.frequency = frequency

        if status is not None:
            self.status = status

