from constants import *
from model.enums import RoomStatus, RoomType
from lib.adventurelib import Room

def init_room(room_type: RoomType, description: str = '') -> Room:
    room = Room(description)
    room.type = room_type
    room.status = RoomStatus.UNSEEN

    match room_type:
            case RoomType.EMPTY:
                room.description = "empty room (you can't go here)"
            
            # First floor rooms
            case RoomType.COMBAT_L1:
                room.description = description
                room.room_text = COMBAT_ROOM_TEXT
            case RoomType.INTRO_FIGHT_L1:
                room.description = "intro fight with Jackie"
            case RoomType.BOSS_L1:
                room.description = "first floor boss fight"
                room.room_text = BOSS_ROOM_TEXT
            case RoomType.BAKERY_L1:
                room.description = "bakery"
                room.room_text = BAKERY_ROOM_TEXT
            case RoomType.LULU_L1:
                room.description = "lululemon"
                room.room_text = LULU_ROOM_TEXT
            case RoomType.KITCHEN_L1:
                room.description = "kitchen"
                room.room_text = KITCHEN_ROOM_TEXT
            case RoomType.BODY_PUMP_L1:
                room.description = "body pump"
                room.room_text = BODY_PUMP_ROOM_TEXT
            case RoomType.HYGGE_L1:
                room.description = "hygge"
                room.room_text = HYGGE_ROOM_TEXT

            # Second floor rooms
            case RoomType.COMBAT_L2:
                room.description = description
                room.room_text = COMBAT_ROOM_TEXT
            case RoomType.BOSS_L2:
                room.description = "second floor boss fight"
                room.room_text = BOSS_ROOM_TEXT
            case RoomType.KITCHEN_L2:
                room.description = "kitchen"
                room.room_text = KITCHEN_ROOM_TEXT
            case RoomType.HYGGE_L2:
                room.description = "hygge"
                room.room_text = HYGGE_ROOM_TEXT
            case RoomType.DAIRY_L2:
                room.description = "dairy"
                room.room_text = DAIRY_ROOM_TEXT
            case RoomType.WEGMANS_L2:
                room.description = "wegmans"
                room.room_text = WEGMANS_ROOM_TEXT
            case RoomType.LAPTOP_L2:
                room.description = "laptop room"
                room.room_text = LAPTOP_ROOM_TEXT
            

            # default    
            case _:
                print("IDK yo this is the default, we shouldn't be here")

    return room