import time
from app.combat import start_combat
from constants import *
from lib.utils import print_delay
from model.enums import RoomType
from model.room import init_room
from app.init_attacks import linda_explain_vitamix, linda_nyt
from app.init_consumables import *
from app.init_enemies import *

def defeated_enemy_subsequent_interaction(character):
    print('Linda entered a room with the smell of battle still hanging in the air.')


#######################################
########## First Floor Rooms ##########
#######################################

def hygge_l1_initial_interaction(character):
    print_delay([
        'Linda found herself in the Hygge Zone',
        'Linda healed to full health!'
    ], 2)
    character.curr_hp = character.max_hp
def hygge_l1_subsequent_interaction(character):
    print_delay([
        'Linda entered the Hygge Zone',
        'Linda healed to full health!'
    ], 2)
    character.curr_hp = character.max_hp
hygge_l1 = init_room(RoomType.VISITABLE, HYGGE_ROOM_TEXT, hygge_l1_initial_interaction, hygge_l1_subsequent_interaction)

def combat_full_inbox_initial_interaction(character):
    start_combat(character, full_email_inbox)
combat_full_inbox_l1 = init_room(RoomType.VISITABLE, COMBAT_ROOM_TEXT, combat_full_inbox_initial_interaction, defeated_enemy_subsequent_interaction)

def body_pump_l1_initial_interaction(character):
    print_delay([
        'Linda went to Body Pump',
        'Linda got PUMPED!!!',
        'Linda\'s damage temporarily increased!'
    ], 2)
    time.sleep(3)
    print_delay(['\nNoah appeared'], 2)
    print('"Wow Mom, you\'re looking pretty swole!"')
    character.temp_damage_modifier = 0.2
def body_pump_l1_subsequent_interaction(character):
    print_delay([
        'Linda thought about going to Body Pump',
        '"Body Pump twice in one day? That\'s crazy."',
        '"Maybe I should take a nap instead..."'
    ], 2)
body_pump_l1 = init_room(RoomType.VISITABLE, BODY_PUMP_ROOM_TEXT, body_pump_l1_initial_interaction, body_pump_l1_subsequent_interaction)

def lulu_l1_initial_interaction(character):
    print_delay([
        'Linda went to Lululemon', 
        '"Ooh! They have the Align pants in my size!"',
        '"Yay!!" (fingers apart)',
        'Linda obtained yoga pants!',
        'Linda\'s base health increased by 25 points!'
    ], 2)
    character.max_hp += 25
    character.curr_hp += 25
def lulu_l1_subsequent_interaction(character):
    print_delay([
        'Linda went to Lululemon',
        'Linda has already been to Lululemon today'
    ], 2)
lulu_l1 = init_room(RoomType.VISITABLE, LULU_ROOM_TEXT, lulu_l1_initial_interaction, lulu_l1_subsequent_interaction)

def combat_diss_cust_initial_interaction(character):
    # TODO: add combat here
    print('Linda fought dissatisfied clients.')
combat_diss_cust_l1 = init_room(RoomType.VISITABLE, COMBAT_ROOM_TEXT, combat_diss_cust_initial_interaction, defeated_enemy_subsequent_interaction)

def kitchen_l1_initial_interaction(character):
    print_delay([
        'Linda entered the kitchen',
        'What\'s this on the counter?',
        'No...',
        'Can it be...?',
        'The GREATEST BLENDER EVER INVENTED???',
        'Linda obtained a Vitamix!'
    ], 2)
    character.attacks.append(linda_explain_vitamix)
def kitchen_l1_subsequent_interaction(character):
    print('Linda entered the kitchen')
kitchen_l1 = init_room(RoomType.VISITABLE, KITCHEN_ROOM_TEXT, kitchen_l1_initial_interaction, kitchen_l1_subsequent_interaction)

def combat_inc_co_initial_interaction(character):
    # TODO: add combat here
    print('Linda fought inferior coworkers')
combat_inc_co_l1 = init_room(RoomType.VISITABLE, COMBAT_ROOM_TEXT, combat_inc_co_initial_interaction, defeated_enemy_subsequent_interaction)

def bakery_l1_initial_interaction(character):
    print_delay([
        'Linda went to the Village Bakery',
        '"Can you only fill it up halfway and make the rest hot water?"',
        # Noah this is such a great line hahaha
        # Why thank you :)
        '...',
        'Linda obtained coffee!'
    ], 2)
    character.consumables[coffee.name] = coffee
def bakery_l1_subsequent_interaction(character):
    print_delay([
        'Linda went to the Village Bakery',
        '"I probably shouldn\'t have any more coffee. It\'ll make me jittery."'
    ], 2)
bakery_l1 = init_room(RoomType.VISITABLE, BAKERY_ROOM_TEXT, bakery_l1_initial_interaction, bakery_l1_subsequent_interaction)

def combat_patrick_initial_interaction(character):
    # TODO: add combat here
    print('Linda fought Patrick')
combat_patrick_l1 = init_room(RoomType.BOSS, BOSS_ROOM_TEXT, combat_patrick_initial_interaction, defeated_enemy_subsequent_interaction)


########################################
########## Second Floor Rooms ##########
########################################

def combat_irs_initial_interaction(character):
    # TODO: add combat here
    print('Linda fought the IRS')
combat_irs_l2 = init_room(RoomType.VISITABLE, COMBAT_ROOM_TEXT, combat_irs_initial_interaction, defeated_enemy_subsequent_interaction)

def kitchen_l2_initial_interaction(character):
    # TODO: add kitchen L2 interaction here - if she has all the ingredients, she can make cookies (and obtain the cookie consumable)
    # Should be the same interaction every time she visits
    print('Linda went to the kitchen')
kitchen_l2 = init_room(RoomType.VISITABLE, KITCHEN_ROOM_TEXT, kitchen_l2_initial_interaction, kitchen_l2_initial_interaction)

def hygge_l2_initial_interaction(character):
    print_delay([
        'Linda found herself in the Hygge Zone',
        'Linda healed to full health!'
    ], 2)
    character.curr_hp = character.max_hp
def hygge_l2_subsequent_interaction(character):
    # The first time Mom visits the Hygge Zone AFTER spawning there, she should encounter Stella and obtain the Failing New York Times
    print_delay([
        'Linda entered the Hygge Zone.',
        '\n'
    ], 2)
    if linda_nyt not in character.attacks:
        print_delay([
            '"Okay, I\'m just gonna lie down for a little bit and then I\'ll go to the Y. I won\'t fall asleep."',
            'Linda laid down.',
            'Stella walked in and started talking about some Stella things.',
            '\n',
            STELLA1, STELLA2, STELLA3, STELLA4, STELLA5
        ], 2)
        print_delay(['\n','...','...','...','Linda fell asleep.'], 4)
        print_delay(['\n','...', '\n', 'Linda woke up!', '\n'], 1)
        print_delay(["What's this? There's something on the table here...", "Some sort of paper... Groggily, Linda leaned over to take a look.", "\n"], 2)
        print_delay(['Linda obtained the Failing New York Times!', '\n'], 2)
        character.attacks.append(linda_nyt)
    print_delay(['Linda healed to full health!'], 2)
    character.curr_hp = character.max_hp
hygge_l2 = init_room(RoomType.VISITABLE, HYGGE_ROOM_TEXT, hygge_l2_initial_interaction, hygge_l2_subsequent_interaction)

def combat_demanding_clients_initial_interaction(character):
    # TODO: add combat here
    print('Linda fought overly demanding clients')
combat_demanding_clients_l2 = init_room(RoomType.VISITABLE, COMBAT_ROOM_TEXT, combat_demanding_clients_initial_interaction, defeated_enemy_subsequent_interaction)

def combat_big_john_initial_interaction(character):
    # TODO: add combat here
    print('Linda fought Big John')
combat_big_john_l2 = init_room(RoomType.VISITABLE, COMBAT_ROOM_TEXT, combat_big_john_initial_interaction, defeated_enemy_subsequent_interaction)

def combat_mega_jackie_initial_interaction(character):
    # TODO: add combat here
    print('Linda fought MEGA JACKIE')
combat_mega_jackie_l2 = init_room(RoomType.BOSS, BOSS_ROOM_TEXT, combat_mega_jackie_initial_interaction, defeated_enemy_subsequent_interaction)

def dairy_l2_initial_interaction(character):
    print_delay([
        'Linda went to Pittsford Farms Dairy',
        'Linda obtained milk, eggs, and butter!'
    ], 2)
    character.consumables.append([milk, eggs, butter])
def dairy_l2_subsequent_interaction(character):
    print_delay([
        'Linda went to Pittsford Farms Dairy'
    ], 2)
dairy_l2 = init_room(RoomType.VISITABLE, DAIRY_ROOM_TEXT, dairy_l2_initial_interaction, dairy_l2_subsequent_interaction)

def wegmans_l2_initial_interaction(character):
    print_delay([
        'Linda went to Wegmans.',
        'Linda strolled down one of the aisles.',
        'A package of store-bought chocolate chip cookies slithered up.', # Hahaha this is great Stella
        '"Ugh, how disgusting..."',
        'The cookies attacked!'
    ], 2)

    # TODO: add combat with Store Bought Chocolate Chip Cookies

    # After winning, Linda gets chocolate chips, sugar, and flour (if she won)
    if character.curr_hp > 0:
        character.consumables.append([flour, sugar, choc_chips])
        print("The store-bought cookies dropped flour, sugar, and chocolate chips.")
def wegmans_l2_subsequent_interaction(character):
    print_delay([
        'Linda went to Wegmans',
        'Store Bought Chocolate Chip Cookies were nowhere to be found'
    ], 2)
wegmans_l2 = init_room(RoomType.VISITABLE, WEGMANS_ROOM_TEXT, wegmans_l2_initial_interaction, wegmans_l2_subsequent_interaction)

def laptop_l2_initial_interaction(character):
    # TODO: add interaction here
    # Linda orders the Aeron (TODO maybe the Aeron negates some portion of damage? That way we don't have to implement some sort of defense mechanic)
    print('Linda went to the laptop room (???)') # TODO do we want this to be the office? What room is the laptop in?
    # no she fights jackie in the office. this is just a room with a laptop
def laptop_l2_subsequent_interaction(character):
    print_delay([
        'Linda went to the laptop room (????)',
    ], 2)
laptop_l2 = init_room(RoomType.VISITABLE, LAPTOP_ROOM_TEXT, laptop_l2_initial_interaction, laptop_l2_subsequent_interaction)