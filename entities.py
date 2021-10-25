#from esper import World, Processor
from entityComponents import *
from entityTags import *


def create_citizen(world, name="",family="", age=0, money=0, health=100):
    citizen = world.create_entity()
    world.add_component(citizen, Citizen())
    world.add_component(citizen, Age(age))
    world.add_component(citizen, Health(health))
    world.add_component(citizen, Money(money))
    world.add_component(citizen, Name(name))
    world.add_component(citizen, Family(family))
    world.add_component(citizen, DeathTime())    
    world.add_component(citizen, DeathChance())
    #print("Citizen created")
    return citizen

def create_city(world, name="Moscow", money=1000.0, taxRate=20.0):
    city = world.create_entity()
    world.add_component(city, City())
    world.add_component(city, Name(name))
    world.add_component(city, Money(money))
    world.add_component(city, TaxRate(taxRate))
    world.add_component(city, Population())
    world.add_component(city, Childrens())
    #print("City " + name + " created")
    return city


def create_factory(world, name="Basic"):
    """create factory"""
    factory = world.create_entity()
    world.add_component(factory, Factory())
    world.add_component(factory, Name(name))
    world.add_component(factory, Money(1000))
    world.add_component(factory, TaxRate(40))
    #print("Factory created")
    return factory


def create_product(world, name=""):
    product = world.create_entity()
    world.add_component(product, Product())
    world.add_component(product, Name(name))
    world.add_component(product, Cost())
    world.add_component(product, Price())
    #print("Product " + name + " created")
    return product





def add_work(world, ent, workId, salary=0, taxRate=0):
    world.add_component(ent, Salary(v=salary))
    world.add_component(ent, TaxRate(v=taxRate))
    world.add_component(ent, WorkId(v=workId))
    #print("Citizen work added")
