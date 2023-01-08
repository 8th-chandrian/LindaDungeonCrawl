from lib.utils import print_delay
from app.init_consumables import cookies


def bake_cookies(linda):
    while True:
        bake_cookies = input('\nDo you want to bake cookies (Y/N)? ')
        bake_cookies = bake_cookies.lower()
        if bake_cookies == 'y' or bake_cookies == 'yes':
            linda.ingredients = []
            linda.consumables[cookies.name] = cookies
            linda.has_baked_cookies = True
            print_delay([
                '\nLinda used up all her ingredients and whipped up a batch of cookies in no time at all.',
                'Linda obtained chocolate chip cookies!'
            ], 2)
            return
        if bake_cookies == 'n' or bake_cookies == 'no':
            print_delay([
                '\nLinda decided not to make cookies.',
                '"Eh...maybe later."'
            ], 2)
            return
        print_delay(['\nUnrecognized input. Please enter Y or N'], 2)