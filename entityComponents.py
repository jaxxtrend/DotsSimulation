from dataclasses import dataclass as component
from constants import *

##################################
#  Define components:
##################################

@component
class Age:
    v: int = 0  # minutes

@component
class Health:
    v: float = 100

@component
class Sleep:
    v: bool = False


@component
class Energy:
    v: float = 100


@component
class Name:
    v: str = ""


@component
class Family:
    v: str = ""

@component
class Salary:
    v: float = 0.0


@component
class Money:
    v: float = 0.0


@component
class Income:
    v: float = 0.0


@component
class Subsidy:
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