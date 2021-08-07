import esper
from components import *

# Processors
class LifeProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (Age) in self.world.get_component(Age):
            if Age.age < 100:
                Age.age += 1
            else:
                self.world.delete_entity(ent)

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

class TaxProcessor(esper.Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        tax = self.world.get_component(City)[0][1].taxRate
        city = self.world.get_component(City)[0][1]
        for ent, (citizen) in self.world.get_component(Citizen):
            citizen.money = int(citizen.money - citizen.salary * (tax / 100))
            city.budget += (citizen.salary * (tax / 100))

class MigrationProcessor(esper.Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        pass