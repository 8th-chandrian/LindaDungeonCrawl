from constants import *
from model.enums import RoomType


class Room:
    def __init__(self, room_type: RoomType, description: str = ''):
        self.room_text = []
        match room_type:
            case RoomType.EMPTY:
                self.description = "empty room (you can't go here)"
            
            # First floor rooms
            case RoomType.COMBAT_L1:
                self.description = description
                self.room_text = COMBAT_ROOM_TEXT
            case RoomType.INTRO_FIGHT_L1:
                self.description = "intro fight with Jackie"
            case RoomType.BOSS_L1:
                self.description = "first floor boss fight"
                self.room_text = BOSS_ROOM_TEXT
            case RoomType.BAKERY_L1:
                self.description = "bakery"
                self.room_text = BAKERY_ROOM_TEXT
            case RoomType.LULU_L1:
                self.description = "lululemon"
                self.room_text = LULU_ROOM_TEXT
            case RoomType.KITCHEN_L1:
                self.description = "kitchen"
                self.room_text = KITCHEN_ROOM_TEXT
            case RoomType.BODY_PUMP_L1:
                self.description = "body pump"
                self.room_text = BODY_PUMP_ROOM_TEXT
            case RoomType.HYGGE_L1:
                self.description = "hygge"
                self.room_text = HYGGE_ROOM_TEXT

            # Second floor rooms

            # default    
            case _:
                print("IDK yo this is the default, we shouldn't be here")