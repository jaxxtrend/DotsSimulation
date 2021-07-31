"""structures"""

class Location:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class Product:
    """product demanded from citizens"""
    def __init__(self, name:str, type:str, price:int ):
        self.name = name
        self.type = type
        self.price = price

class City:
    """Produce money income"""
    def __init__(self, citizensCount:int, location:Location):
        self.citizensCount = citizensCount
        self.location = location

class Factory:
    """Made products for citizens and trading"""
    def __init__(self, employers:int, product:str, resouces:dict):
        self.employers = employers
        self.product = product
        self.resources = resouces

class Work:
    """citizen work"""
    def __init__(self, factory:Factory, salary:int ):
            self.factory = factory
            self.salary = salary

class Citizen:
    """Lives in cities"""
    def __init__(self, wealth:int, work:Work):
        self.wealth = wealth
        self.work = work

class Transport:
    """Delivery of products between the cities"""
    def __init__(self, location:Location, cargo:dict, speed:int, destination:City, sentfrom:City):
        self.location = location
        self.cargo = cargo
        self.speed = speed
        self.destination = destination
        self.sentfrom = sentfrom

