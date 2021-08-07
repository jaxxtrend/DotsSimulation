from dataclasses import dataclass as component


@component
class Age:
    age: int = 0


@component
class Type:
    type: str = ""  # city, factory, citizen...


@component
class Name:
    name: str = ""


@component
class ID:
    id: int


@component
class ParentID:
    pID: int


@component
class Salary:
    salary = 10.0


@component
class Money:
    money = 0.0


@component
class TaxRate:
    taxRate = 20.0


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
