from constants import *
from model.enums import RoomStatus, RoomType
from lib.adventurelib import Room

def init_room(type: RoomType = RoomType.EMPTY, map_text: str = '', initial_interaction = None, subsequent_interaction = None) -> Room:
    room = Room('')
    room.type = type
    room.status = RoomStatus.UNSEEN
    room.map_text = map_text

    # The initial_interaction function is called the first time Mom visits a room
    room.initial_interaction = initial_interaction
    # The subsequent_interaction function is called every other time Mom visits a room
    room.subsequent_interaction = subsequent_interaction

    return room