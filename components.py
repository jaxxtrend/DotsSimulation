import esper
from dataclasses import dataclass as component

@component
class Product:
    def __init__(self, name: str = "", price: int = 1):
        self.name = name
        self.price = price


@component
class Work:
    def __init__(self, factory: str = "", salary: int = 10):
        self.factory = factory
        self.salary = salary


@component
class Citizen:
    def __init__(self, age=0, money=0, salary=0):
        self.age: int = age
        self.money: int = money
        self.salary: int = salary


@component
class City:
    def __init__(self, citizens=1000, budget=1000, taxRate=20):
        self.citizens: int = citizens
        self.budget: int = budget
        self.taxRate: int = taxRate


@component
class Factory:
    def __init__(self, employers=100, products=Product):
        pass