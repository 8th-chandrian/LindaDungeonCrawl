import random
import time

from constants import ATTACK_TEXT_DELAY

class Attack:

    def __init__(self, damage: int, attack_text1: str = '', attack_text2: str = ''):
        self.damage = damage
        self.attack_text1 = attack_text1
        self.attack_text2 = attack_text2

    def enemy_attack(self):
        real_damage = self.damage + random.randint(-0.2 * self.damage, 0.2 * self.damage)
        print(self.attack_text1)
        time.sleep(ATTACK_TEXT_DELAY)
        print("Linda takes " + real_damage + " " + self.attack_text2 + ".")
        return real_damage

    def linda_attack(self, enemy_name_takes: str = ''):
        # enemy_name_takes string should be in the format "Jackie takes" or "the clients take", no space at the end necessary
        real_damage = self.damage + random.randint(-0.2 * self.damage, 0.2 * self.damage)
        print(self.attack_text1)
        time.sleep(ATTACK_TEXT_DELAY)
        print(enemy_name_takes + " " + real_damage + self.attack_text2 + ".")