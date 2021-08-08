from esper import Processor, World
import components as cp


# Processors
class AgeProc(Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (age) in self.world.get_component(cp.Age):
            if age.value < 100:  # simple dead if age equal 100
                age.value += 1
            else:
                self.world.delete_entity(ent)


# Households lifecicle
class HouseholdsProc(Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (type, Age) in self.world.get_component(cp.Age):
            if type.type == "citizen" and Age > 18:
                Household = self.world.create_entity(cp.Household)
        for ent, (Household) in self.world.get_component(cp.Household):
            Household.citizens.append()


class WorkProc(Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        salaries = 0
        for ent, (salary, money, taxRate) in self.world.get_components(cp.Salary, cp.Money, cp.TaxRate):
            if self.world.has_component(ent, component_type=cp.Citizen):
                money.value += (salary.value - salary.value * (taxRate.value / 100))
                salaries += (salary.value - salary.value * (taxRate.value / 100))

        for ent, (salary, money, taxRate) in self.world.get_components(cp.Salary, cp.Money, cp.TaxRate):
            if self.world.has_component(entity=ent, component_type=cp.City):
                money.value += salaries * (taxRate.value / 100)
            elif self.world.has_component(entity=ent, component_type=cp.Factory):
                money.value -= salaries
        

class TaxProc(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        tax = self.world.get_component(City)[0][1].taxRate
        city = self.world.get_component(City)[0][1]
        for ent, (citizen) in self.world.get_component(Citizen):
            citizen.money = int(citizen.money - citizen.salary * (tax / 100))
            city.budget += (citizen.salary * (tax / 100))


class MigrationProc(Processor):
    def __init__(self) -> None:
        super().__init__()

    def process(self):
        pass
