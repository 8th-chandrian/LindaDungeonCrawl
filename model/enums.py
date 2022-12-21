from enum import Enum

class RoomType(Enum):
    # Represents a cell in the map without an actual room in it
    EMPTY = 1

    # First floor rooms
    COMBAT_L1 = 2
    INTRO_FIGHT_L1 = 3
    BOSS_L1 = 4
    BAKERY_L1 = 5
    LULU_L1 = 6
    KITCHEN_L1 = 7
    BODY_PUMP_L1 = 8
    HYGGE_L1 = 9

    # Second floor rooms
