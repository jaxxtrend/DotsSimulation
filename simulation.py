import time
from datetime import timedelta
from random import randint

from constants import *
from entities import *
from entityComponents import *
from entityTags import *
from processors import *


def main():

    world = World()

    city = create_city(world)
    # factory = create_factory(world)

    # added processors
    world.add_processor(CityzenSpawnProcessor())
    world.add_processor(AgeProcessor())
    world.add_processor(DeathProcessor())

    try:
        i = 0
        t = 0
        while True:
            tick = DAY
            # Call world.process() to run all Processors.
            world.process()
            i += 1
            if i % tick == 0:
                world.collectHistory(i//tick)
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
