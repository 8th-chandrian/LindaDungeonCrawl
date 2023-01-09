import time
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
                '\nLinda used all her ingredients and whipped up a batch of cookies in no time at all.',
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

def buy_aeron(linda):
    aeron_price = linda.money_count + 10
    print_delay([
        '\nPrice: ${0:.2f}'.format(aeron_price),
        'Your funds: ${0:.2f}'.format(linda.money_count),
    ], 2)
    while True:
        buy_aeron = input('\nDo you want to buy the most comfortable office chair in the world (Y/N)? ')
        buy_aeron = buy_aeron.lower()
        if buy_aeron == 'n' or buy_aeron == 'no':
            print_delay(['\nAre you sure???'], 2)
            continue
        if buy_aeron == 'y' or buy_aeron == 'yes':
            print_delay([
                '\nLinda thought about buying the Aeron...',
                'But it wasn\'t in her budget.',
                'Saaaaaaad :(\n'
            ], 2)
            time.sleep(3)
            print_delay([
                'But then she thought some more and realized...',
                'IT\'S TAX DEDUCTABLE!!!\n',
                'Linda bought the Herman Miller Aeron (and it arrived in record time)!',
                '"Oooh, great lumbar support."',
                'Linda\'s HP increased!'
            ], 2)
            linda.max_hp += 150
            linda.curr_hp += 150
            break
