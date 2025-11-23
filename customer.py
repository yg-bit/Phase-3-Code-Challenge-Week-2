class Customer:
    _all = []

    def __init__(self, name):
        self.name = name
        Customer._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 15:
            raise Exception("Name must be a string between 1 and 15 characters.")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order._all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        orders_for_coffee = [o for o in Order._all if o.coffee == coffee]
        if not orders_for_coffee:
            return None
        spending = {}
        for o in orders_for_coffee:
            spending.setdefault(o.customer, 0)
            spending[o.customer] += o.price
        return max(spending, key=spending.get)
