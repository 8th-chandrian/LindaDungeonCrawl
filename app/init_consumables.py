from lib.utils import print_delay
from model.consumable import Consumable


# In-battle consumables
def use_coffee(character):
    print_delay([
        'Linda drank some coffee', 
        '"Ahh, diluted. Just the way I like it"', 
        'Linda got caffeinated! Linda\'s damage was temporarily increased!'
    ], 2)
    character.temp_damage_modifier = 1
coffee = Consumable("coffee", use_coffee)

def use_cookies(character):
    print_delay([
        'Linda ate some of her homemade chocolate chip cookies',
        'They were phenomenal (as per usual)',
        'Linda healed to full health!'
    ], 2)
    character.curr_hp = character.max_hp
cookies = Consumable("cookies", use_cookies)

# Cookie ingredients
milk = Consumable("milk")
eggs = Consumable("eggs")
butter = Consumable("butter")
flour = Consumable("flour")
choc_chips = Consumable("chocolate chips")
sugar = Consumable("sugar")