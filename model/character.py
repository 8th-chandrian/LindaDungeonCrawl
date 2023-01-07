class Character:
    def __init__(self, max_hp: int):
        self.max_hp = max_hp
        self.curr_hp = max_hp

        # TODO: these are Mom's base attacks that she gets from various items she picks up
        # Starts as an empty array, but attacks are added when she obtains Failing NYT and Vitamix items
        self.attacks = []

        # Items that can be used in combat (maps item name to item object)
        self.consumables = {}

        # Items that can be used to make other items
        self.ingredients = []

        # TODO: these will be increased by items obtained
        self.passive_damage_modifier = 1
        self.passive_defense_modifier = 1
        self.temp_damage_modifier = 0

        self.money_count = 0

    def get_damage_modifier(self):
        return self.passive_damage_modifier + self.temp_damage_modifier
    
    def remove_consumable_from_inventory(self, consumable):
        del self.consumables[consumable.name]
