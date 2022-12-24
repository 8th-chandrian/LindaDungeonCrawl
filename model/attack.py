import random
import time

class Attack:

    def __init__(self, damage: int, attack_text1: str = '', attack_text2: str = ''):
        self.damage = damage
        self.attack_text1 = attack_text1
        self.attack_text2 = attack_text2

    def enemy_attack(self):
        real_damage = self.damage + random.randint(-0.2 * self.damage, 0.2 * self.damage)
        print(self.attack_text1)
        time.sleep(3)
        print("Linda takes " + real_damage + " " + self.attack_text2 + ".")
        return real_damage

    def linda_attack(self, enemy_name_takes: str = ''):
        # enemy_name_takes string should be in the format "Jackie takes" or "the clients take", no space at the end necessary
        real_damage = self.damage + random.randint(-0.2 * self.damage, 0.2 * self.damage)
        print(self.attack_text1)
        time.sleep(3)
        print(enemy_name_takes + " " + real_damage + self.attack_text2 + ".")


# TODO: adjust damage values
# Linda attacks will be listed with their opponents

# mega jackie attacks
mega_jackie_yell = Attack(75, "Mega Jackie got really mad! Oh no, she started YELLING!", "loudness damage")
mega_jackie_toxicity = Attack(30, "Mega Jackie is acting really toxic.\n\n\"MUAHAHAHAHAHAAAA..... MY TOXICITY HAS ONLY GROWN SINCE LAST WE FOUGHT!!!\"\n\nLinda lost sleep due to stress!", "psychic damage")
mega_jackie_guilt = Attack(30, "Mega Jackie is trying to guilt Linda into continuing to work with her.", " damage")

# jackie attacks ("yell" is an event, not an attack)

# IRS
IRS_tax = Attack(50, "The IRS demanded that Linda do her taxes. Oh no, they're really confusing!", "damage")

# mouse
mouse_run = Attack(30, "The mouse skittered across the floor.\nLinda shrieked!\n\n\"If only I hadn't defeated Tilly in LINDA SUPER ULTRA MEGA BOSS RUSH 2018...\"\n", "damage")

# problematic clients
p_clients_expectations = Attack(30, "The problematic clients are demanding that Linda go beyond the scope of the contract!", "damage")
linda_work_harder = Attack(10, "Linda grits her teeth and simply works harder.", "damage. It works, but this can only go on for so long before someone gets smacked with a copy of the Failing New York Times...")

# big john
john_ask = Attack(50, "Big John is asking Linda to work with him.\n\n\"Oh brother...\" Linda thinks.\n", "damage")
john_everybody = Attack(20, "Big John says, \"Everybody's doin' it...\"", "damage")
john_feel_good = Attack(20, "Big John says, \"It'll make you feel good...\"", "damage")
john_want_to = Attack(20, "Big John says, \"You know you want to...\"", "damage")
linda_say_no = Attack(10, "Linda politely declines Big John's offer.", "damage")

# email inbox
inbox_sit_there = Attack(15, "The inbox is just sitting there.", "damage from the stress of thinking about all those emails.\n\nThe emails assume a fighting stance...")
inbox_grow = Attack(25, "The inbox swells in size.", "damage from the stress of thinking about all those emails.\n\nThe emails assume a fighting stance...")
linda_delete = Attack(20, "Linda deletes a bunch of emails.", "damage")
linda_ignore = Attack(30, "Linda ignores a bunch of emails.\nThe inbox is devestated!", "sadness damage :(")

# dissatisfied clients
