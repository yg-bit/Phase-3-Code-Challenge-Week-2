import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    Customer._all.clear()
    Coffee._all.clear()
    Order._all.clear()

def test_order_creation():
    c = Customer("Alice")
    coffee = Coffee("Mocha")
    o = Order(c, coffee, 4.5)
    assert o in Order._all
    assert o.customer == c
    assert o.coffee == coffee
    assert o.price == 4.5

def test_order_validation():
    c = Customer("Alice")
    coffee = Coffee("Mocha")
    with pytest.raises(Exception):
        Order("not_customer", coffee, 3.0)
    with pytest.raises(Exception):
        Order(c, "not_coffee", 3.0)
    with pytest.raises(Exception):
        Order(c, coffee, 0)
    with pytest.raises(Exception):
        Order(c, coffee, 11)
    with pytest.raises(Exception):
        Order(c, coffee, "not_number")

