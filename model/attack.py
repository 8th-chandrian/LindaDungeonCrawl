import random

from lib.utils import print_delay

class Attack:

    def __init__(self, damage: int, attack_text1: str = '', attack_text2: str = '', name: str = ''):
        self.name = name
        self.damage = damage
        self.name = name
        self.attack_text1 = attack_text1
        self.attack_text2 = attack_text2

    def attack(self, enemy_name: str = '', multiplier: int = 1):
        real_damage = (self.damage * multiplier) + random.randint(-0.2 * self.damage, 0.2 * self.damage)

        print()
        print_delay([
            self.attack_text1,
            "{} took {} {}.\n".format(enemy_name, real_damage, self.attack_text2)
        ], 2.5)
        return real_damage
