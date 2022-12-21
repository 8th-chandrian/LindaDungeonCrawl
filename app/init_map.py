
from model.enums import RoomType
from model.map import Map
from model.room import Room

# TODO add layout of map here (how this should be conceptualized on x and y axis, where 0,0 is)

def init_l1_map() -> Map:
    map = Map(3, 5)
    map[1, 0] = Room(RoomType.HYGGE_L1)
    map[1, 1] = Room(RoomType.COMBAT_L1, "full email inbox")
    map[2, 1] = Room(RoomType.BODY_PUMP_L1)
    map[0, 1] = Room(RoomType.LULU_L1)
    map[1, 2] = Room(RoomType.COMBAT_L1, "dissatisfied clients")
    map[2, 2] = Room(RoomType.KITCHEN_L1)
    map[1, 3] = Room(RoomType.COMBAT_L1, "incompetent coworkers")
    map[0, 3] = Room(RoomType.BAKERY_L1)
    map[1, 4] = Room(RoomType.BOSS_L1)