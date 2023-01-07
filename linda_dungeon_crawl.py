from app.combat import print_character_hp
from app.init_map import init_l1_map, init_l2_map
from app.init_consumables import *
from app.init_attacks import linda_hyperbeam, linda_splash
from constants import LEVEL_ONE_STARTING_TEXT, LEVEL_TWO_STARTING_TEXT, LINDA_MAX_HP
from lib.adventurelib import when, start
from lib.utils import print_delay
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

@when("show health")
def print_hp():
    global linda_character
    print_character_hp(linda_character)

@when("show inventory")
def print_items():
    global linda_character
    if len(linda_character.consumables) == 0 and len(linda_character.ingredients) == 0:
        print('\nLinda\'s inventory is empty')
        return
    if len(linda_character.consumables) > 0:
        consumables_arr = ['\nConsumables:']
        for consumable in linda_character.consumables.keys():
            consumables_arr.append(consumable.name)
        consumables_str = '\n'.join(consumables_arr)
        print(consumables_str)
    if len(linda_character.ingredients) > 0:
        ingredients_arr = ['\nIngredients:']
        for ingredient in linda_character.ingredients:
            ingredients_arr.append(ingredient.name)
        ingredients_str = '\n'.join(ingredients_arr)
        print(ingredients_str)

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
        print_delay([f'Linda went {direction}.\n'], 0.75)
        if room.status == RoomStatus.SEEN:
            room.initial_interaction(linda_character)
        else:
            room.subsequent_interaction(linda_character)
        
        if linda_character.curr_hp <= 0:
            map.set_current_room(map.starting_room_row, map.starting_room_col)
            # TODO: Stella, let me know if you can think of better text for this. This prints when she dies and respawns
            print_delay([
                'Linda awoke to find herself in the Hygge Zone', 
                '"Whew! What a rough day!"', 
                'Linda relaxed on the couch and healed to full health',
                'Linda felt ready to kick some ass again!'
            ], 2)
            linda_character.curr_hp = linda_character.max_hp

        elif room.type == RoomType.BOSS and level == Level.L1:
            # TODO: write better text for this
            print_delay([
                'Linda vanquished Patrick back to the corner office from whence he had come, and in doing so, won her freedom from Reward Gateway.',
                'Liberated, she set up an LLC and began working from home.',
                'But little did she know...more trouble was brewing...'
            ], 3)

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
# print('Linda fought Jackie (the first time)')
# time.sleep(1)
# print('Linda was defeated\n')
# time.sleep(1)
# current_room.initial_interaction(linda_character)
# time.sleep(3)

# TODO: delete this. I'm just adding these attacks to make testing easier
linda_character.attacks.append(linda_hyperbeam)
linda_character.attacks.append(linda_splash)


# TODO: delete these items once you've tested them
linda_character.consumables[coffee.name] = coffee
linda_character.consumables[cookies.name] = cookies
linda_character.ingredients.append(milk)
linda_character.ingredients.append(eggs)
linda_character.ingredients.append(sugar)

print(LEVEL_ONE_STARTING_TEXT)
start()