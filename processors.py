from esper import Processor, World
import components as cp
from random import randint
from entities import create_citizen


class P_CitizenGeneration(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        for ent, (city, childrens, population) in self.world.get_components(cp.City, cp.Childrens, cp.Population):
            # generate citizens
            if len(childrens.v) < population.v:
                citizens =[]
                while len(citizens) < population.v:
                    citizen = create_citizen(self.world, age=randint(18, 30))
                    citizens.append(citizen)
                childrens.v += tuple(citizens)

class P_Age(Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (age) in self.world.get_component(cp.Age):
            if age.v < 100:  # simple dead if age equal 100
                age.v += 1
                print(age)
            else:
                for ent1,(childrens) in self.world.get_components(cp.City,cp.Childrens):
                    y = list(childrens.v)
                    y.remove(ent)
                    childrens.v = y
                self.world.delete_entity(ent)

                print("citizen is dead")


# Households lifecicle
class P_Households(Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (type, Age) in self.world.get_component(cp.Age):
            if type.type == "citizen" and Age > 18:
                Household = self.world.create_entity(cp.Household)
        for ent, (Household) in self.world.get_component(cp.Household):
            Household.citizens.append()


class P_Work(Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        incomeSum = 0
        for ent, (income, money, taxRate) in self.world.get_components(cp.Income, cp.Money, cp.TaxRate):
            if self.world.has_component(ent, component_type=cp.Citizen):
                money.v += (income.v - income.v * (taxRate.v / 100))
                incomeSum += (income.v - income.v * (taxRate.v / 100))

        for ent, (income, money, taxRate) in self.world.get_components(cp.Income, cp.Money, cp.TaxRate):
            if self.world.has_component(entity=ent, component_type=cp.City):
                money.v += incomeSum * (taxRate.v / 100)
            elif self.world.has_component(entity=ent, component_type=cp.Factory):
                money.v -= incomeSum


class P_Tax(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        tax = self.world.get_component(cp.City)[0][1].taxRate
        city = self.world.get_component(cp.City)[0][1]
        for ent, (citizen) in self.world.get_component(cp.Citizen):
            citizen.money = int(citizen.money - citizen.income * (tax / 100))
            city.budget += (citizen.income * (tax / 100))


class P_Migration(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        pass



