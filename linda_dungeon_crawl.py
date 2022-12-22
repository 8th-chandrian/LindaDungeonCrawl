from app.init_map import init_l1_map, init_l2_map
from lib.adventurelib import when, start

global map
global current_room

map = init_l1_map()
current_room = map.get_current_room()

@when("map")
def print_map():
    map.print()

@when("room")
def print_current_room():
    print(current_room.description)

@when("exits")
def print_exits():
    print(current_room.exits())

@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        map.set_current_room(room.row, room.col)
        # TODO: this is where room interactions should go (e.g. fights, effects on Mom, etc.)
        print(f'You go {direction}.')
        print(current_room.description)

start()