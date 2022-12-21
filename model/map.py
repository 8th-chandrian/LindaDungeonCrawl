from constants import MAP_BORDER_CHAR, MAP_CELL_HEIGHT, MAP_CELL_WIDTH
from model.enums import RoomType
from model.room import Room


class Map:

    # Initializes a map containing all empty rooms
    def __init__(self, map_rows: int, map_columns: int):
        self.map_grid = []
        for row in range(map_rows):
            for _ in range(map_columns):
                if len(self.map_grid) <= row:
                    self.map_grid.append([])
                self.map_grid[row].append(Room(RoomType.EMPTY))
    
    # Sets the room at (row, col) to the provided Room object
    def set_room(self, room: Room, row: int, col: int):
        self.map_grid[row][col] = room

    def debug_print(self):
        for row in range(len(self.map_grid)):
            print_row(self.map_grid[row])
        print_map_vert_border(len(self.map_grid[0]))

def print_map_vert_border(num_cols):
    for _ in range(num_cols):
        print_map_cell_vert_border()
    print()

def print_map_cell_vert_border():
    print(MAP_BORDER_CHAR * MAP_CELL_WIDTH, end = '')

def print_map_cell_text(text_index, room):
    if text_index < len(room.room_text):
        print(MAP_BORDER_CHAR + room.room_text[text_index].center(MAP_CELL_WIDTH - 2) + MAP_BORDER_CHAR, end='')
    else:
        print_empty_line()

def print_empty_line():
    print(MAP_BORDER_CHAR + ' ' * (MAP_CELL_WIDTH - 2) + MAP_BORDER_CHAR, end='')

def print_row(row):
    print_map_vert_border(len(row))
    for i in range(MAP_CELL_HEIGHT):
        for room in row:
            if i % MAP_CELL_HEIGHT == (MAP_CELL_HEIGHT / 2 - 1):
                print_map_cell_text(0, room)
            elif i % MAP_CELL_HEIGHT == (MAP_CELL_HEIGHT / 2):
                print_map_cell_text(1, room)
            else:
                print_empty_line()
        print()
    