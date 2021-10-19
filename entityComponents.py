from dataclasses import dataclass as component


@component
class Age:
    v: float = 0 #minutes
    def years(v):
        return v / 525600

@component
class Health:
    v: float = 100

@component
class Name:
    s: str = None


@component
class Income:
    v: float = 0.0


@component
class Subsidy:
    v: float = 0.0


@component
class Salary:
    v: float = 0.0


@component
class Money:
    v: float = 0.0


@component
class TaxRate:
    """Value in percents"""
    v: float = 20.0


@component
class WorkId:
    v: int = None


@component
class Cost:
    v: float = 0.0


@component
class Price:
    v: float = 0.0


@component
class Childrens:
    v: tuple = ()


@component
class Parents:
    v: tuple = ()


@component
class Population:
    v: int = 5
