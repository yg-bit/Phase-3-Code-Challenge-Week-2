# Coffee Shop — Phase 3 Code Challenge (Week 2)

Simple object-oriented exercise modeling a coffee shop. This repository contains three core classes (`Coffee`, `Customer`, and `Order`) and a small pytest suite that verifies validations and relationships between them.

## What this is

- A small Python project used for learning/testing object relationships and validations.
- Implements: `coffee.py`, `customer.py`, and `order.py`.
- Tests live under `tests/` and exercise the public API and validation logic.

## Project structure

```
coffee_shop/
    coffee.py        # Coffee model
    customer.py      # Customer model
    order.py         # Order model
    Pipfile          # Pipenv environment
    tests/
        test_coffee.py
        test_customer.py
        test_order.py
```

## Requirements

- Python 3.8+ recommended
- Pipenv is used for dependency management (see `Pipfile`)

## Setup (using Pipenv)

Install pipenv if you don't have it, create/activate the environment, and install dependencies:

```bash
pip install --user pipenv
cd coffee_shop
pipenv install --dev
```

Use `pipenv shell` to enter the virtual environment, or run commands with `pipenv run`.

## Running tests

From the `coffee_shop` directory run:

```bash
pipenv run pytest -q
```

Or, if you don't use Pipenv but have the test requirements installed (pytest), run:

```bash
cd coffee_shop
pytest -q
```

## Quick usage examples

Run these examples from inside the `coffee_shop` directory (so the modules `customer`, `coffee`, and `order` can be imported directly):

```bash
python -c "from customer import Customer; from coffee import Coffee; c = Customer('Alice'); coffee = Coffee('Latte'); o = c.create_order(coffee, 4.5); print(c.name, coffee.name, o.price)"
```

That demonstrates creating a customer, a coffee, and an order using the public API used by the tests.

## Notes

- The tests expect simple in-memory collections (`_all` lists) and validate input (name lengths, types, price ranges, etc.).
- If you add new files or change imports, update tests or packaging accordingly.

## Contact

If you need help or want to extend this project, open an issue or reach out to the repo owner.
