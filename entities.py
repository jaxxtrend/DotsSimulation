#from esper import World, Processor
from entityComponents import *


def create_city(world, name="Moscow", money=1000.0, taxRate=20.0):
    city = world.create_entity()
    world.add_component(city, City())
    world.add_component(city, Name(s=name))
    world.add_component(city, Money(v=money))
    world.add_component(city, TaxRate(v=taxRate))
    world.add_component(city, Population())
    world.add_component(city, Childrens())
    print("City " + name + " created")
    return city


def create_factory(world, name="Basic"):
    """create factory"""
    factory = world.create_entity()
    world.add_component(factory, Factory())
    world.add_component(factory, Name(s=name))
    world.add_component(factory, Money(v=1000))
    world.add_component(factory, TaxRate(v=40))
    print("Factory created")
    return factory


def create_product(world, name=""):
    product = world.create_entity()
    world.add_component(product, Product())
    world.add_component(product, Name(s=name))
    world.add_component(product, Cost())
    world.add_component(product, Price())
    print("Product " + name + " created")
    return product


def create_citizen(world, age=0, money=0,):
    citizen = world.create_entity()
    world.add_component(citizen, Citizen())
    world.add_component(citizen, Age(v=age))
    world.add_component(citizen, Money(v=money))
    print("Citizen created")
    return citizen


def add_work(world, ent, workId, salary=0, taxRate=0):
    world.add_component(ent, Salary(v=salary))
    world.add_component(ent, TaxRate(v=taxRate))
    world.add_component(ent, WorkId(v=workId))
    print("Citizen work added")
