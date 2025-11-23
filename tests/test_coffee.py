import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    Customer._all.clear()
    Coffee._all.clear()
    Order._all.clear()

def test_coffee_creation():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"
    assert coffee in Coffee._all

def test_coffee_name_validation():
    with pytest.raises(Exception):
        Coffee("ab")
    with pytest.raises(Exception):
        Coffee(123)

def test_orders_and_customers():
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    coffee = Coffee("Cappuccino")
    c1.create_order(coffee, 3.0)
    c2.create_order(coffee, 5.0)
    assert coffee.num_orders() == 2
    assert set(coffee.customers()) == {c1, c2}
    assert coffee.average_price() == 4.0
