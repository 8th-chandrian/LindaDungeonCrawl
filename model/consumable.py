class Consumable:
    def __init__(self, name: str, use = None):
        self.name = name

        # use is a function that takes the character as input and applies an effect to them
        self.use = use