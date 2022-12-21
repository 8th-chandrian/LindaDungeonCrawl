from model.enums import RoomType


class Room:
    def __init__(self, room_type: RoomType, description: str):
        match room_type:
            case RoomType.EMPTY:
                self.description = "empty room (you can't go here)"
            
            # First floor rooms
            case RoomType.COMBAT_L1:
                self.description = description
            case RoomType.INTRO_FIGHT_L1:
                self.description = "intro fight with Jackie"
            case RoomType.BOSS_L1:
                self.description = "first floor boss fight"
            case RoomType.BAKERY_L1:
                self.description = "bakery"
            case RoomType.LULU_L1:
                self.description = "lululemon"
            case RoomType.KITCHEN_L1:
                self.description = "kitchen"
            case RoomType.BODY_PUMP_L1:
                self.description = "body pump"
            case RoomType.HYGGE_L1:
                self.description = "hygge"

            # Second floor rooms

            # default    
            case _:
                print("IDK yo this is the default, we shouldn't be here")