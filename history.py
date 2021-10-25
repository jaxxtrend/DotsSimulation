from esper import World
from entityTags import Citizen
from entityComponents import Age, DeathChance
import json

'''
tick
    ent
        component
            value

ent
    component
        tick
            value

'''



def collectHistory(tick,world):
    
    for entity in world._entities:
        if world.has_component(entity, Citizen):
            value = world.get_components(Age, DeathChance)
            

            



