import time
import esper
from dataclasses import dataclass as component
import random


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


# Processors
class LifeProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (citizen) in self.world.get_component(Citizen):
            if citizen.age < 100:
                citizen.age += 1
            else:
                pass


class WorkProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (citizen) in self.world.get_component(Citizen):
            if citizen.age < 18:
                pass
            elif citizen.age >= 60 and citizen.age < 100:
                citizen.salary = random.randint(30, 50)
            elif citizen.age >= 100:
                citizen.salary = citizen.salary + 1
            else:
                citizen.salary += (random.randint(0, 6) * citizen.age)

            citizen.money += citizen.salary
            print(ent, citizen.age, citizen.money, citizen.salary)


def main():
    world = esper.World()

    lifeProcessor = LifeProcessor()
    workProcessor = WorkProcessor()
    world.add_processor(lifeProcessor)
    world.add_processor(workProcessor)

    # generate citizens
    i = 0
    while i < 2:
        name = "citizen" + str(i)
        world.create_entity(name)
        world.add_component(name,
                            Citizen(age=random.randint(0, 30),
                                    money=random.randint(0, 1000),
                                    salary=random.randint(10, 30)))
        i += 1

    try:
        i = 0
        while i < 3:
            # Call world.process() to run all Processors.
            world.process()
            time.sleep(0.1)
            i += 1

    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    print("\nHeadless Example. Press Ctrl+C to quit!\n")
    main()
