
from model.enums import RoomType
from model.map import Map
from model.room import init_room

def init_l1_map() -> Map:
    map = Map(3, 5)
    map.init_map_cell(init_room(RoomType.HYGGE_L1), 1, 0)
    map.init_map_cell(init_room(RoomType.COMBAT_L1, "full email inbox"), 1, 1)
    map.init_map_cell(init_room(RoomType.BODY_PUMP_L1), 2, 1)
    map.init_map_cell(init_room(RoomType.LULU_L1), 0, 1)
    map.init_map_cell(init_room(RoomType.COMBAT_L1, "dissatisfied clients"), 1, 2)
    map.init_map_cell(init_room(RoomType.KITCHEN_L1), 2, 2)
    map.init_map_cell(init_room(RoomType.COMBAT_L1, "incompetent coworkers"), 1, 3)
    map.init_map_cell(init_room(RoomType.BAKERY_L1), 0, 3)
    map.init_map_cell(init_room(RoomType.BOSS_L1), 1, 4)

    map.set_current_room(1, 0)
    
    return map

def init_l2_map() -> Map:
    map = Map(3, 5)
    map.init_map_cell(init_room(RoomType.COMBAT_L2, "IRS"), 0, 0)
    map.init_map_cell(init_room(RoomType.KITCHEN_L2), 0, 1)
    map.init_map_cell(init_room(RoomType.HYGGE_L2), 1, 1)
    map.init_map_cell(init_room(RoomType.COMBAT_L2, "problematic clients"), 1, 2)
    map.init_map_cell(init_room(RoomType.COMBAT_L2, "Big John"), 1, 3)
    map.init_map_cell(init_room(RoomType.BOSS_L2), 1, 4)
    map.init_map_cell(init_room(RoomType.DAIRY_L2), 2, 2)
    map.init_map_cell(init_room(RoomType.WEGMANS_L2), 2, 3)
    map.init_map_cell(init_room(RoomType.LAPTOP_L2), 0, 3)

    map.set_current_room(1, 1)

    return map