import time
from random import randint
from esper import World
from entityComponents import *
from entityTags import *
from processors import *
from entities import *
from constants import *
from dataBase import create_connection, execute_query
import json
import pickle



def main():    

    db = create_connection(":memory:")
    backupDb = create_connection("history.db")

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
            tick = MONTH
            # Call world.process() to run all Processors.
            world.process()
                
            pickle.dump(world, "dump.pcl", pickle.HIGHEST_PROTOCOL)

            # worldDict = world.__dict__
            # worldList = list(worldDict)
            # worldJson = json.dumps(worldList)
            # execute_query(backupDb, worldJson)

            # for entity in world._entities:
            #     entities = []
            #     for comp in world.components_for_entity(entity):
            #         componentsDict = {}
            #         componentsDict.update(comp.__dict__)
            #     entities.append(componentsDict)
            # dumpStr = json.dumps(entities)
            # #db.execute(str(dumpStr))


            i += 1
            if i % tick == 0:
                et = time.process_time() - t
                t = time.process_time()
                if et < 1:
                    time.sleep(1-et)
                print(et)
                print("{}".format(str(timedelta(seconds=(60*i)))))
                
                #backup to the disk
                db.backup(backupDb)

    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    print("\nHeadless Example. Press Ctrl+C to quit!\n")
    main()
