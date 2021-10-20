from esper import Processor, World
from entityComponents import *
from entityTags import *
from entities import create_citizen
from random import randint
from datetime import timedelta
from generators import *
from constants import *


class P_CitizenGeneration(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        for ent, (city, childrens, population) in self.world.get_components(City, Childrens, Population):
            # generate citizens
            if len(childrens.v) < 1000000:
                citizens = []
                citizens += list(childrens.v)
                while len(citizens) < 1:
                    citizen = create_citizen(self.world,
                                                name=makeName(),
                                                family=makeFamily(),
                                                age=0 )
                    citizens.append(citizen)
                childrens.v = tuple(citizens)
                citizens = []

class P_Age(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        for ent, (age) in self.world.get_component(Age):
            if age.v < (YEAR * 100):  # simple dead if age equal 100 years
                age.v += 1
            else:
                #citizen dead
                for ent1,(city, childrens) in self.world.get_components(City,Childrens):
                    y = list(childrens.v)
                    y.remove(ent)
                    childrens.v = tuple(y)
                self.world.delete_entity(ent)

class P_Health(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        pass



# Households lifecicle
class P_Households(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        for ent, (type, age) in self.world.get_component(Age):
            if type.type == "citizen" and Age > 18:
                Household = self.world.create_entity(Household)
        for ent, (Household) in self.world.get_component(Household):
            Household.citizens.append()


class P_Work(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        incomeSum = 0
        for ent, (income, money, taxRate) in self.world.get_components(Income, Money, TaxRate):
            if self.world.has_component(ent, component_type=Citizen):
                money.v += (income.v - income.v * (taxRate.v / 100))
                incomeSum += (income.v - income.v * (taxRate.v / 100))

        for ent, (income, money, taxRate) in self.world.get_components(Income, Money, TaxRate):
            if self.world.has_component(entity=ent, component_type=City):
                money.v += incomeSum * (taxRate.v / 100)
            elif self.world.has_component(entity=ent, component_type=Factory):
                money.v -= incomeSum


class P_Tax(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        tax = self.world.get_component(City)[0][1].taxRate
        city = self.world.get_component(City)[0][1]
        for ent, (citizen) in self.world.get_component(Citizen):
            citizen.money = int(citizen.money - citizen.income * (tax / 100))
            city.budget += (citizen.income * (tax / 100))


class P_Migration(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        pass



