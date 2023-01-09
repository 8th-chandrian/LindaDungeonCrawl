from os import system
from app.combat import print_character_hp, start_combat
from app.init_map import init_l1_map, init_l2_map
from app.init_consumables import *
from app.init_attacks import linda_hyperbeam, linda_splash, linda_explain_vitamix_l2
from app.init_enemies import jackie
from constants import *
from lib.adventurelib import when, start
from lib.utils import print_delay
from model.character import Character
from model.enums import Level, RoomStatus, RoomType

global map
global level
global current_room
global linda_character

map = init_l1_map() # TODO revert
level = Level.L1
current_room = map.get_current_room()
linda_character = Character(LINDA_MAX_HP)

# TODO: for debug purposes only. Lets you set the coordinates of the starting room
# map.set_current_room(1, 3)
# current_room = map.get_current_room()

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
    if len(linda_character.consumables) > 0:
        consumables_arr = ['\nConsumables:']
        for consumable in linda_character.consumables.keys():
            consumables_arr.append(consumable)
        consumables_str = '\n'.join(consumables_arr)
        print(consumables_str)
    if len(linda_character.ingredients) > 0:
        ingredients_arr = ['\nIngredients:']
        for ingredient in linda_character.ingredients:
            ingredients_arr.append(ingredient.name)
        ingredients_str = '\n'.join(ingredients_arr)
        print(ingredients_str)
    print('\nMoney: ${0:.2f}'.format(linda_character.money_count))

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
        # Player should not be able to enter the boss room until they have been to every other room on the floor
        if room.type == RoomType.BOSS and map.visited_rooms + 1 < map.total_visitable_rooms:
            boss_room_arr = [
                'You are attempting to enter the BOSS ROOM',
                'You must visit all other rooms before you can enter the BOSS ROOM',
                '(You have visited {}/{} non-boss rooms)'.format(map.visited_rooms, map.total_visitable_rooms-1)
            ]
            print('\n'.join(boss_room_arr))
            return
        print_delay([f'Linda went {direction}.\n'], 0.75)
        if room.status == RoomStatus.SEEN:
            room.initial_interaction(linda_character)
        else:
            room.subsequent_interaction(linda_character)
        
        if linda_character.curr_hp <= 0:
            map.set_current_room(map.starting_room_row, map.starting_room_col)
            print_delay([
                'Linda awoke to find herself in the Hygge Zone', 
                '"Whew! What a rough day!"', 
                'Linda relaxed on the couch and healed to full health',
                'Linda felt ready to kick some ass again!'
            ], 2)
            linda_character.curr_hp = linda_character.max_hp

        elif room.type == RoomType.BOSS and level == Level.L1:
            system('clear')
            print_delay([
                'Linda vanquished Patrick back to the corner office from whence he had come, and in doing so, won her freedom from Reward Gateway.',
                'Liberated, she set up an LLC and began working from home.\n',
                'Linda felt so much more relaxed from all the yoga and good sleep she now had time for.',
                'Being well-rested caused Linda\'s damage to increase! Linda became a more potent warrior!\n',
                'And she found luuuuuuurve when she started dating Paul!',
                'Linda\'s HP doubled due to the power of luuuuuuurve <3\n',
                'But little did she know...',
                'More trouble was brewing...'
            ], 4)

            input('\n(Press <enter> to continue)')
            system('clear')

            linda_character.max_hp = 250
            linda_character.curr_hp = linda_character.max_hp

            # Double the vitamix's damage
            linda_character.attacks = [linda_explain_vitamix_l2]

            # Init level two map
            map = init_l2_map()
            current_room = map.get_current_room()
            print_delay([LEVEL_TWO_STARTING_TEXT], 2)
            current_room.initial_interaction(linda_character)
            level = Level.L2

        elif room.type == RoomType.BOSS and level == Level.L1:
            # TODO: write finishing text
            print('Linda kicked Mega Jackie\'s ass! Booyah!!!!!')
            
        else:
            current_room = room
            map.set_current_room(room.row, room.col)

def print_title_text():
    print_delay([
        TITLE_TEXT_1, 
        TITLE_TEXT_2, 
        TITLE_TEXT_3, 
        TITLE_TEXT_4, 
        TITLE_TEXT_5, 
        TITLE_TEXT_6, 
        TITLE_TEXT_7, 
    ], 2)

print_title_text()
start_combat(linda_character, jackie)

# TODO: delete this. I'm just adding these attacks to make testing easier
linda_character.attacks.append(linda_hyperbeam)
linda_character.attacks.append(linda_splash)

# This is commented out. Can uncomment for testing
# linda_character.consumables[coffee.name] = coffee
# linda_character.consumables[cookies.name] = cookies
# linda_character.ingredients.append(milk)
# linda_character.ingredients.append(eggs)
# linda_character.ingredients.append(sugar)
# linda_character.ingredients.append(butter)
# linda_character.ingredients.append(flour)
# linda_character.ingredients.append(choc_chips)


# TODO get star wars music to play with title text, then stop when jackie attacks

print_delay([LEVEL_ONE_STARTING_TEXT], 2)
print_delay([
    'Linda found herself in the Hygge Zone',
    'Linda healed to full health!'
], 2)
linda_character.curr_hp = linda_character.max_hp
start()