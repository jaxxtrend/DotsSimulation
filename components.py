import esper
from dataclasses import dataclass as component


@component
class Work:
    factory: str = "Basic"
    salary: int = 10

@component
class Citizen:
    age: int = 0
    money: int = 0
    salary: int = 0
    workId: int = None  #factory id

@component
class Factory:
    city: str = "Moscow"
    factoryId: int = None
    productName: str = "Generic"
    productPrice: int = 0
    employs: int = 0
    employSalary: int = 0
    money: int = 0
    resources: int = 0

@component
class Product:
    name: str = ""
    price:int = 0

@component
class City:
    citizens: int = 1000
    budget: int = 1000
    taxRate: int = 20
    factories = []


# city = City()
# factory = Factory()
# factory.employSalary = 28
# factory.factoryId = 1
# city.factories.append(factory)
# citizen = Citizen()
# factory = city.factories[0]
# citizen.salary = factory.employSalary
# citizen.workId = factory.factoryId

# print(citizen)