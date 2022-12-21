
from model.enums import RoomType
from model.map import Map
from model.room import Room

# TODO add layout of map here (how this should be conceptualized on x and y axis, where 0,0 is)

def init_l1_map() -> Map:
    map = Map(3, 5)
    map.set_room(Room(RoomType.HYGGE_L1), 1, 0)
    map.set_room(Room(RoomType.COMBAT_L1, "full email inbox"), 1, 1)
    map.set_room(Room(RoomType.BODY_PUMP_L1), 2, 1)
    map.set_room(Room(RoomType.LULU_L1), 0, 1)
    map.set_room(Room(RoomType.COMBAT_L1, "dissatisfied clients"), 1, 2)
    map.set_room(Room(RoomType.KITCHEN_L1), 2, 2)
    map.set_room(Room(RoomType.COMBAT_L1, "incompetent coworkers"), 1, 3)
    map.set_room(Room(RoomType.BAKERY_L1), 0, 3)
    map.set_room(Room(RoomType.BOSS_L1), 1, 4)
    
    return map