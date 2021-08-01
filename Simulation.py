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
                #self.world.delete_entity(Citizen)


class WorkProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (citizen) in self.world.get_component(Citizen):
            if citizen.age < 18:
                pass
            elif citizen.age >= 60 and citizen.age < 100:
                citizen.salary = 10
            elif citizen.age >= 100:
                citizen.salary = 0
            else:
                citizen.salary += (random.randint(0, 6) * citizen.age)

            citizen.money += citizen.salary
            #print(ent, citizen.age, citizen.money, citizen.salary)

class TaxProcessor(esper.Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        tax = self.world.get_component(City)[0][1].taxRate
        city = self.world.get_component(City)[0][1]
        for ent, (citizen) in self.world.get_component(Citizen):
            citizen.money = int(citizen.money - citizen.salary * (tax / 100))
            city.budget += (citizen.salary * (tax / 100))
        #print(int(city.budget))

class MigrationProcessor(esper.Processor):
    def __init__(self) -> None:
        super().__init__()
    
    def process(self):
        pass


def main():
    world = esper.World()

    taxProcessor = TaxProcessor()
    lifeProcessor = LifeProcessor()
    workProcessor = WorkProcessor()
    world.add_processor(lifeProcessor)
    world.add_processor(workProcessor)
    world.add_processor(taxProcessor)

    # generate city
    cityName = "Moscow"
    world.create_entity(cityName)
    world.add_component(cityName,City())

    # generate citizens
    i = 0
    while i < 1:
        name = "citizen" + str(i)
        world.create_entity(name)
        world.add_component(name,
                            Citizen(age=random.randint(0, 30),
                                    money=random.randint(0, 1000),
                                    salary=random.randint(10, 30)))
        i += 1

    try:
        i = 0
        while True:
            # Call world.process() to run all Processors.
            world.process()
            time.sleep(0.1)
            i += 1
            print(world.process)

    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    print("\nHeadless Example. Press Ctrl+C to quit!\n")
    main()
