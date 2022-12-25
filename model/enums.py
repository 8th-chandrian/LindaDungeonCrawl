from enum import Enum

class RoomType(Enum):
    # Represents a cell in the map without an actual room in it
    EMPTY = 1

    # Represents a cell in the map that is a visitable room
    VISITABLE = 2

    # Represents a boss fight cell
    BOSS = 3
    

class RoomStatus(Enum):
    # Have not been in or adjacent to this room
    UNSEEN = 1

    # Have been adjacent to this room but not yet entered
    SEEN = 2

    # Have visited this room
    VISITED = 3

class Level(Enum):
    L1 = 1
    L2 = 2

class Action(Enum):
    ATTACK = 1
    ITEM = 2