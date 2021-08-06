import time
import esper
from components import *
import random


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
                # self.world.delete_entity(Citizen)


class WorkProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        averageSalary = 0
        city = self.world.get_component(City)[0][1]
        for ent, (citizen) in self.world.get_component(Citizen):
            if citizen.age < 18:
                # 10% of the budget goes to providing for children
                citizen.salary = int((city.budget * 0.1) / city.citizens)
            elif citizen.age >= 60 and citizen.age < 100:
                # 20% of the budget goes to providing for the elderly
                citizen.salary = int((city.budget * 0.2) / city.citizens)
            elif citizen.age >= 100:
                citizen.salary = 0
            else:
                # 50% of the budget goes to providing for the employs
                citizen.salary = int((city.budget * 0.1) / city.citizens)
            citizen.money += citizen.salary
            averageSalary += citizen.salary
            # subtract salaty from budget
            city.budget -= citizen.salary
        #FAKE product price includes salaries by 50% of full price if sell this budget get profit.
        city.budget += (averageSalary * 2)
        # average salaries
        averageSalary = int(averageSalary/city.citizens)
        
        print("salary = " + str(averageSalary))
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
        print(int(city.budget))


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
    world.add_component(cityName, City(citizens=10000, budget=100000))

    # generate citizens
    i = 0
    while i < 10000:
        name = "citizen" + str(i)
        world.create_entity(name)
        world.add_component(name,
                            Citizen(age=random.randint(0, 30),
                                    money=random.randint(0, 1000)))
        i += 1

    try:
        i = 0
        while True:
            # Call world.process() to run all Processors.
            world.process()
            time.sleep(0.1)
            i += 1
            # print(world.process)

    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    print("\nHeadless Example. Press Ctrl+C to quit!\n")
    main()
