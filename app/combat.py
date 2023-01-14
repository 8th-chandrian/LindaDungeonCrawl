
import random
import time
from constants import BIG_JOHN_ENEMY_NAME, MEGA_JACKIE_ENEMY_NAME, PATRICK_ENEMY_NAME
from lib.utils import clear, print_delay

from model.enums import Action

def start_combat(linda, enemy):
    linda_attacks = dict((attack.name.lower(), attack) for attack in (linda.attacks + enemy.linda_attacks))
    enemy_attacks = enemy.attacks

    time.sleep(1)
    clear()
    time.sleep(1)
    print_delay(enemy.intro_text, 3)

    input('\n(Press <enter> to continue)')
    clear()

    enemy_name = enemy.name
    if enemy.name == PATRICK_ENEMY_NAME:
        enemy_name = "Level One Boss: " + enemy_name
    if enemy.name == MEGA_JACKIE_ENEMY_NAME:
        enemy_name = "Level Two Boss: " + enemy_name

    print_delay([f'\nLinda VS {enemy_name}'], 3)
    print_delay(['FIGHT!\n\n\n'], 3)

    # Enemy attacks first
    print_delay([f'{enemy.name} attacks first'], 2)

    enemy_attack_number = 0
    is_big_john = enemy.name == BIG_JOHN_ENEMY_NAME

    while True:
        enemy_attack_number_immediate = enemy_attack_number % (len(enemy_attacks))
        damage = enemy_attacks[enemy_attack_number_immediate].attack("Linda")
        linda.curr_hp -= damage

        enemy_attack_number += 1

        if is_big_john and enemy_attack_number == 1:
            print_delay(["Linda was paralyzed with indecision!", "Linda could not attack!\n"], 2)
            continue
        elif is_big_john and enemy_attack_number < 4:
            continue

        if linda.curr_hp <= 0:
            print_delay(["Oh no! Linda was defeated!\n"], 5)
            enemy.curr_hp = enemy.max_hp
            clear()
            break
        else:
            print('\n')
            print_character_hp(linda)
            print_enemy_hp(enemy)
        
        # Then Mom attacks
        action = get_linda_action(linda_attacks, linda.consumables)
        if action[0] == Action.ATTACK:
            damage = action[1].attack(enemy.name, linda.get_damage_modifier())
            enemy.curr_hp -= damage
        if action[0] == Action.ITEM:
            print()
            action[1].use(linda)
            linda.remove_consumable_from_inventory(action[1])

        if enemy.curr_hp <= 0:
            victory_cash = round(random.uniform(50, 200), 2)
            linda.money_count += victory_cash
            print_delay([enemy.name + " was defeated!", 'Linda got ${0:.2f} for winning'.format(victory_cash)], 3)
            clear()
            break
    
    # Temp damage modifier only lasts for one battle
    linda.temp_damage_modifier = 0

# returns a tuple of action type and relevant object
def get_linda_action(linda_attacks, linda_items):
    while True:
        print_action_options(linda_attacks, linda_items)
        action_name = input('> ')
        action_name = action_name.lower()
        if action_name.lower() in linda_attacks.keys():
            return (Action.ATTACK, linda_attacks[action_name])
        if action_name == 'use item':
            print_item_options(linda_items)
            item_name = input('> ')
            item_name = item_name.lower()
            if item_name != 'back' and item_name in linda_items.keys():
                return (Action.ITEM, linda_items[item_name])

def print_action_options(linda_attacks, linda_items):
    prompt_arr = []
    if len(linda_items) > 0:
        prompt_arr.append('\nSelect an attack or use an item:')
    else:
        prompt_arr.append('\nSelect an attack:')
    
    for attack_name in linda_attacks:
        prompt_arr.append(attack_name)
    if len(linda_items) > 0:
        prompt_arr.append('use item')
    print('\n'.join(prompt_arr))

def print_item_options(linda_items):
    prompt_string = '\nSelect an item to use (or "back" to return to attacks):\n'
    for item_name in linda_items:
        prompt_string += item_name + '\n'
    print(prompt_string)

def print_character_hp(linda):
    print(f'Linda\'s HP:\n{linda.curr_hp} / {linda.max_hp}')

def print_enemy_hp(enemy):
    print(f'Enemy HP:\n{enemy.curr_hp} / {enemy.max_hp}')