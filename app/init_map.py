
from app.init_rooms import *
from constants import *
from model.map import Map



def init_l1_map() -> Map:
    map = Map(rows=3, cols=5, starting_room_row=1, starting_room_col=0)
    map.init_map_cell(hygge_l1, 1, 0)
    map.init_map_cell(combat_full_inbox_l1, 1, 1)
    map.init_map_cell(body_pump_l1, 2, 1)
    map.init_map_cell(lulu_l1, 0, 1)
    map.init_map_cell(combat_diss_cust_l1, 1, 2)
    map.init_map_cell(kitchen_l1, 2, 2)
    map.init_map_cell(combat_inc_co_l1, 1, 3)
    map.init_map_cell(bakery_l1, 0, 3)
    map.init_map_cell(combat_patrick_l1, 1, 4)

    map.set_current_room(map.starting_room_row, map.starting_room_col)
    
    return map

def init_l2_map() -> Map:
    map = Map(rows=3, cols=5, starting_room_row=0, starting_room_col=1)
    map.init_map_cell(combat_irs_l2, 0, 0)
    map.init_map_cell(kitchen_l2, 1, 1)
    map.init_map_cell(hygge_l2, 0, 1)
    map.init_map_cell(combat_demanding_clients_l2, 1, 2)
    map.init_map_cell(combat_big_john_l2, 1, 3)
    map.init_map_cell(combat_mega_jackie_l2, 1, 4)
    map.init_map_cell(dairy_l2, 2, 2)
    map.init_map_cell(wegmans_l2, 2, 3)
    map.init_map_cell(laptop_l2, 0, 3)

    map.set_current_room(map.starting_room_row, map.starting_room_col)

    return map