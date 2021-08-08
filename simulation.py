import time
from random import randint
from esper import World
from components import *
from processors import *
from entities import *


def main():
    world = World()
    city = create_city(world)
    factory = create_factory(world)
    # generate citizens
    i = 0
    while i < 5:
        citizen = create_citizen(world, age=randint(18, 30))
        add_work(world, citizen, factory, 30, 13)
        i += 1

    # added processors
    p_age = P_Age()
    p_FactoryPaycheck = P_FactoryPaycheck()
    p_getAGob = P_GetGob()
    world.add_processor(p_age)
    world.add_processor(p_FactoryPaycheck)
    world.add_processor(p_getAGob)

    try:
        i = 0
        while True:
            # Call world.process() to run all Processors.
            world.process()
            time.sleep(0.1)
            i += 1
            # print(len(world._entities))

    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    print("\nHeadless Example. Press Ctrl+C to quit!\n")
    main()
