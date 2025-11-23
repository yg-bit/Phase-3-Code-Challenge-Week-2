import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    Customer._all.clear()
    Coffee._all.clear()
    Order._all.clear()

def test_customer_creation():
    c = Customer("Alice")
    assert c.name == "Alice"
    assert c in Customer._all

def test_customer_name_validation():
    with pytest.raises(Exception):
        Customer("")
    with pytest.raises(Exception):
        Customer("A"*16)
    with pytest.raises(Exception):
        Customer(123)

def test_create_order_and_relationships():
    c = Customer("Bob")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 5.0)
    assert order in c.orders()
    assert coffee in c.coffees()
