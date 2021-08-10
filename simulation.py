import time
from random import randint
from esper import World
from components import *
from processors import *
from entities import *


def main():


    world = World()

    city = create_city(world)
    # factory = create_factory(world)
    
    # added processors
    world.add_processor(P_CitizenGeneration())
    world.add_processor(P_Age())

# one step is one day
    try:
        i = 0
        while True:
            # Call world.process() to run all Processors.
            world.process()
            time.sleep(0.1)
            i += 1

    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    print("\nHeadless Example. Press Ctrl+C to quit!\n")
    main()
