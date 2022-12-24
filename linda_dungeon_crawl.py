import time
from app.init_map import init_l1_map, init_l2_map
from constants import LEVEL_ONE_STARTING_TEXT, LEVEL_TWO_STARTING_TEXT, LINDA_MAX_HP
from lib.adventurelib import when, start
from model.character import Character
from model.enums import Level, RoomStatus, RoomType

global map
global level
global current_room
global linda_character

map = init_l1_map()
level = Level.L1
current_room = map.get_current_room()
linda_character = Character(LINDA_MAX_HP)

@when("map")
def print_map():
    map.print()

@when("exits")
def print_exits():
    print(current_room.exits())

@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global map
    global level
    global current_room
    global linda_character

    room = current_room.exit(direction)
    if room:
        print(f'Linda went {direction}.')
        time.sleep(0.5)
        if room.status == RoomStatus.SEEN:
            room.initial_interaction(linda_character)
        else:
            room.subsequent_interaction(linda_character)
        
        if linda_character.curr_hp <= 0:
            map.set_current_room(map.starting_room_row, map.starting_room_col)

        elif room.type == RoomType.BOSS and level == Level.L1:
            # TODO: write better text for this
            print('Linda vanquished Patrick back to the corner office from whence he had come, and in doing so, won her freedom from Reward Gateway.')
            time.sleep(3)
            print('Liberated, she set up an LLC and began working from home.')
            time.sleep(3)
            print('But little did she know...more trouble was brewing...')
            time.sleep(3)

            # TODO: text for interlude with Paul goes here

            # TODO: what do we want to set these stats to?
            linda_character.max_hp = 200
            linda_character.passive_damage_modifier = 1.5

            # Init level two map
            map = init_l2_map()
            current_room = map.get_current_room()
            print(LEVEL_TWO_STARTING_TEXT)
            current_room.initial_interaction(linda_character)
            level = Level.L2

        elif room.type == RoomType.BOSS and level == Level.L1:
            # TODO: write finishing text
            print('Linda kicked Mega Jackie\'s ass! Booyah!!!!!')
            
        else:
            current_room = room
            map.set_current_room(room.row, room.col)

# TODO: we should put the initial fight with Jackie here
print('Linda fought Jackie (the first time)')
time.sleep(1)
print('Linda was defeated\n')
time.sleep(1)
current_room.initial_interaction(linda_character)
time.sleep(3)
print(LEVEL_ONE_STARTING_TEXT)
start()