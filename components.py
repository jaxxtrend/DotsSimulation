from dataclasses import dataclass as component


@component
class Citizen:
    pass


@component
class Factory:
    pass


@component
class Product:
    pass


@component
class City:
    pass


@component
class Household:
    pass


@component
class Age:
    v: int = 0


@component
class Name:
    s: str = None


@component
class Income:
    v: float = 0.0


@component
class Money:
    v: float = 0.0


@component
class TaxRate:
    """Value in precents"""
    v: float = 20.0


@component
class Employees:
    v: int = 0
