from dataclasses import dataclass as component


@component
class Age:
    value: int = 0


@component
class City:
    name = ""


@component
class Citizen:
    pass


@component
class Factory:
    pass


@component
class Name:
    string: str = ""


@component
class ParentID:
    pID: int


@component
class Salary:
    value = 10.0


@component
class Money:
    value = 0.0


@component
class TaxRate:
    """Value in precents"""
    value = 20.0


@component
class Product:
    name: str = ""
    cost = 0.0  # prime cost
    price = 0.0  # market price

# not shure
@component
class City:
    households = []
    factories = []

@component
class Household:
    citizens = []
