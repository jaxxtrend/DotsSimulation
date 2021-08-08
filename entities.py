#from esper import World, Processor
from components import *


def create_city(world, name="Moscow", money=1000.0, taxRate=20.0):
    city = world.create_entity()
    world.add_component(city, City())
    world.add_component(city, Name(s=name))
    world.add_component(city, Money(v=money))
    world.add_component(city, TaxRate(v=taxRate))
    print("City " + name + " created")


def create_factory(world, name="Basic"):
    """create factory"""
    factory = world.create_entity()
    world.add_component(factory, Factory())
    world.add_component(factory, Name(s=name))
    world.add_component(factory, Money(v=1000))
    world.add_component(factory, TaxRate(v=40))
    world.add_component(factory, Employees())
    product = Product
    product.name = "Energy"
    product.cost = 0
    product.price = 10
    world.add_component(factory, product)
    print("Factory " + name + " created")


def create_citizen(world, age=0, money=0, income=0, taxRate=0):
    citizen = world.create_entity()
    world.add_component(citizen, Citizen())
    world.add_component(citizen, Age(v=age))
    world.add_component(citizen, Money(v=money))
    world.add_component(citizen, Income(v=income))
    world.add_component(citizen, TaxRate(v=taxRate))
