import time
from random import randint
from esper import World
from entityComponents import *
from entityTags import *
from processors import *
from entities import *
from constants import *


def main():    

    world = World()

    city = create_city(world)
    # factory = create_factory(world)
    
    # added processors
    world.add_processor(P_CitizenGeneration())
    world.add_processor(P_Age())

    try:
        i = 0
        t = 0
        while True:
            tick = MONTH
            # Call world.process() to run all Processors.
            world.process()
            i += 1
            if i % tick == 0:
                et = time.process_time() - t
                t = time.process_time()
                if et < 1:
                    time.sleep(1-et)
                print(et)
                print("{}".format(str(timedelta(seconds=(60*i)))))

    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    print("\nHeadless Example. Press Ctrl+C to quit!\n")
    main()
