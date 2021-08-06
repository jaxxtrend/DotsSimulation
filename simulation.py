import time
import esper
from components import *
from processors import *
import random

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
