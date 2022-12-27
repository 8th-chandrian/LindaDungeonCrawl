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
    print('Linda entered a room littered with the corpses of her vanquished foes.') # TODO: this may be too aggro but I thought it was funny


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
    time.sleep(4)
    print_delay('Noah appeared', 2)
    print('"Wow Mom, you\'re looking pretty swole"')
    character.temp_damage_modifier = 0.2
def body_pump_l1_subsequent_interaction(character):
    print_delay([
        'Linda thought about going to Body Pump',
        '"Body Pump twice in one day? That\'s crazy."',
        '"Maybe I should take a nap instead..."'
    ], 2)
body_pump_l1 = init_room(RoomType.VISITABLE, BODY_PUMP_ROOM_TEXT, body_pump_l1_initial_interaction, body_pump_l1_subsequent_interaction)

def lulu_l1_initial_interaction(character):
    # TODO: add lululemon interaction here (obtain red rain boots?)
    print('Linda went to Lululemon')
def lulu_l1_subsequent_interaction(character):
    print_delay([
        'Linda went to Lululemon',
        'Linda has already been to Lululemon today'
    ], 2)
lulu_l1 = init_room(RoomType.VISITABLE, LULU_ROOM_TEXT, lulu_l1_initial_interaction, lulu_l1_subsequent_interaction)

def combat_diss_cust_initial_interaction(character):
    # TODO: add combat here
    print('Linda fought dissatisfied customers')
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
    print('Linda fought incompetent coworkers')
combat_inc_co_l1 = init_room(RoomType.VISITABLE, COMBAT_ROOM_TEXT, combat_inc_co_initial_interaction, defeated_enemy_subsequent_interaction)

def bakery_l1_initial_interaction(character):
    print_delay([
        'Linda went to the Village Bakery',
        '"Can you only fill it up halfway and make the rest hot water?"',
        'Linda obtained coffee!'
    ], 2)
    character.consumables.append(coffee)
def bakery_l1_subsequent_interaction(character):
    print_delay([
        'Linda went to the Village Bakery',
        '"I probably shouldn\'t have any more coffee. It\'ll make me jittery"'
    ], 2)
bakery_l1 = init_room(RoomType.VISITABLE, BAKERY_ROOM_TEXT, bakery_l1_initial_interaction, bakery_l1_subsequent_interaction)

def combat_patrick_initial_interaction(character):
    # TODO: add combat here
    print('Linda fought Patrick')
combat_patrick_l1 = init_room(RoomType.BOSS, BOSS_ROOM_TEXT, combat_patrick_initial_interaction, defeated_enemy_subsequent_interaction)


########################################
########## Second Floor Rooms ##########
########################################

# TODO remove
def combat_template_initial_interaction(character):
    # TODO: add combat here
    print('Linda fought XXXXX')
combat_template_l2 = init_room(RoomType.VISITABLE, COMBAT_ROOM_TEXT, combat_template_initial_interaction, defeated_enemy_subsequent_interaction)



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
    if linda_nyt not in character.attacks:
        # TODO: add Stella talking to Mom here and Mom falling asleep
        print('Linda obtained the Failing New York Times!')
        character.attacks.append(linda_nyt)
    print_delay([
        'Linda entered the Hygge Zone',
        'Linda healed to full health!'
    ], 2)
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
    # TODO: add combat with Store Bought Chocolate Chip Cookies
    print('Linda went to Wegmans and fought Store Bought Chocolate Chip Cookies')

    # After winning, Linda gets chocolate chips and flour (if she won)
    if character.curr_hp > 0:
        character.consumables.append([flour, sugar, choc_chips])
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
def laptop_l2_subsequent_interaction(character):
    print_delay([
        'Linda went to the laptop room (????)',
    ], 2)
laptop_l2 = init_room(RoomType.VISITABLE, LAPTOP_ROOM_TEXT, laptop_l2_initial_interaction, laptop_l2_subsequent_interaction)