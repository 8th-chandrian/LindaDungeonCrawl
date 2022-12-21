from app.init_map import init_l1_map, init_l2_map
from lib.adventurelib import when, start


global current_room

@when("print")
def print_map():
    map = init_l2_map()
    map.debug_print()


start()