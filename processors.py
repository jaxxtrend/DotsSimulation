from esper import Processor, World
from entityComponents import *
from entityTags import *
from entities import create_citizen
from random import randint, random
from datetime import timedelta
from generators import *
from constants import *


class CityzenSpawnProcessor(Processor):
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
                                             age=0)
                    citizens.append(citizen)
                childrens.v = tuple(citizens)
                citizens = []


class AgeProcessor(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):

        for ent, (age) in self.world.get_component(Age):
            age.v += 1


class DeathProcessor(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):

        for ent, (age, deathTime, deathChance) in self.world.get_components(Age, DeathTime, DeathChance):

            if age.v != 0 and age.v % YEAR == 0:
                deathChance = (age.v // YEAR) / 200
                # chance to die slow increased from 0 to .5 up to 100 years? after 100 years, every year == .5
                if random() < deathChance:
                    # mark death minute
                    deathTime = randint(1, YEAR)

            if age.v % YEAR == deathTime.v:
                # citizen remove from the city
                for ent1, (city, childrens) in self.world.get_components(City, Childrens):
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
