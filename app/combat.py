
import random
import time

from constants import ATTACK_TEXT_DELAY
from model.attack import print_delay
from model.enums import Action

def start_combat(linda, enemy):
    linda_attacks = dict((attack.name.lower(), attack) for attack in (linda.attacks + enemy.linda_attacks))
    linda_items = dict((item.name.lower(), item) for item in linda.consumables)
    enemy_attacks = enemy.attacks

    print_delay(enemy.intro_text)

    while True:
        # Enemy attacks first
        damage = get_enemy_attack(enemy_attacks).attack("Linda")
        linda.curr_hp -= damage

        if linda.curr_hp < 0:
            print_delay(["Oh no! Linda was defeated!"])
            break
        
        # Then Mom attacks
        action = get_linda_action(linda_attacks, linda_items)
        if action[0] == Action.ATTACK:
            damage = action[1].attack(enemy.name)
            enemy.curr_hp -= damage
        if action[0] == Action.ITEM:
            action[1].use(linda)

        if enemy.curr_hp < 0:
            print_delay([enemy.name + " was defeated!"])
            break

def get_enemy_attack(enemy_attacks):
    outer_range = len(enemy_attacks)
    next_attack_int = random.randint(0, outer_range-1)
    return enemy_attacks[next_attack_int]

# returns a tuple of action type and relevant object
def get_linda_action(linda_attacks, linda_items):
    while True:
        print_action_options(linda_attacks)
        action_name = input('> ')
        action_name = action_name.lower()
        if action_name.lower() in linda_attacks.keys():
            return (Action.ATTACK, linda_attacks[action_name])
        if action_name == 'use item':
            print_item_options(linda_items)
            item_name = input('> ')
            item_name = item_name.lower()
            if item_name != 'back':
                return (Action.ITEM, linda_items[item_name])

def print_action_options(linda_attacks, linda_items):
    prompt_string = 'Select an attack or use an item:\n'
    for attack_name in linda_attacks:
        prompt_string += attack_name + '\n'
    if len(linda_items) > 0:
        prompt_string += 'use item\n'
    print(prompt_string)

def print_item_options(linda_items):
    prompt_string = 'Select an item to use:\n'
    for item_name in linda_items:
        prompt_string += item_name + '\n'
    print(prompt_string)
