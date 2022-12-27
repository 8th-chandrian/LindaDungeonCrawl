class Enemy:

    def __init__(self, name: str, intro_text, max_hp: int, attacks, linda_attacks):
        self.name = name

        # This will be an array, so we can print one line after the other with a delay in between
        self.intro_text = intro_text
        
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.attacks = attacks
        self.linda_attacks = linda_attacks
