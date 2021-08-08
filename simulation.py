import time
from random import randint
from esper import World
from components import *
from processors import *
from entities import *


def main():
    world = World()
    create_city(world)
    create_factory(world)
    # generate citizens
    i = 0
    while i < 5:
        create_citizen(world, age=randint(0, 30))
        i += 1

    # added processors
    p_age = P_Age()
    p_work = P_Work()
    world.add_processor(p_age)
    world.add_processor(p_work)

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
