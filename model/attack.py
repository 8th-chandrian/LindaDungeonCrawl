import random
import time

from constants import ATTACK_TEXT_DELAY

def print_delay(text_arr):
    for text in text_arr:
        print(text)
        time.sleep(ATTACK_TEXT_DELAY)

class Attack:

    def __init__(self, damage: int, name: str = '', attack_text1: str = '', attack_text2: str = ''):
        self.name = name
        self.damage = damage
        self.name = name
        self.attack_text1 = attack_text1
        self.attack_text2 = attack_text2

    def attack(self, enemy_name: str = ''):
        real_damage = self.damage + random.randint(-0.2 * self.damage, 0.2 * self.damage)

        print_delay([
            self.attack_text1,
            enemy_name + " took " + real_damage + " " + self.attack_text2 + "."
        ])
        return real_damage
