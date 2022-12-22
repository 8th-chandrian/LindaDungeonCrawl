class Attack:

    def __init__(self, name: str, damage: int, attack_type: str = ''):
        self.name = name
        self.damage = damage
        self.attack_type = attack_type

    def print_attack_text(self, enemy_name):
        # TODO: determine damage based on self.damage +/- 0-5%
        print(enemy_name + ' used ' + self.name)
        print('It did ' + self.damage + ' ' + self.attack_type + ' damage')


jackie_yell = Attack("YELL", 75, "psychic")
jackie_be_toxic = Attack('be toxic', 30, "poison")
# Add more here