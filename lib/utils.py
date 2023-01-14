# import only system from os
from os import system, name

import time


def print_delay(text_arr, delay):
    for text in text_arr:
        print(text)
        time.sleep(delay)

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')