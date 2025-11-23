class Coffee:
    _all = []

    def __init__(self, name):
        self.name = name
        Coffee._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise Exception("Coffee name must be 3+ characters.")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order._all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(order.price for order in orders) / len(orders)
