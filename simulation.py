import time
from esper import World
from components import *
from processors import *
from random import randint

def main():
    world = World()

    # generate city
    cityName = cp.Name()
    cityName.name = "Moscow"
    city = world.create_entity()
    world.add_component(city, cityName)
    world.add_component(city, cp.City())    
    world.add_component(city, cp.Money())
    world.add_component(city, cp.TaxRate())

    # generate citizens
    i = 0
    while i < 5:
        citizen = world.create_entity()
        world.add_component(citizen, cp.Citizen())
        world.add_component(citizen, cp.Age(value=randint(0,30)))
        world.add_component(citizen, cp.Money())
        world.add_component(citizen, cp.Salary())
        world.add_component(citizen, cp.TaxRate())
        i += 1

    #added processors
    ageProc = AgeProc()
    workProc = WorkProc()
    world.add_processor(ageProc)
    world.add_processor(workProc)

    try:
        i = 0
        while True:
            # Call world.process() to run all Processors.
            world.process()
            time.sleep(0.1)
            i += 1
            #print(len(world._entities))

    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    print("\nHeadless Example. Press Ctrl+C to quit!\n")
    main()