import attack

class Enemy:

    def __init__(self, name: str, intro_text: str, max_hp: int, attacks, linda_attacks):
        self.name = name
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.attacks = attacks
        self.linda_attacks = linda_attacks
