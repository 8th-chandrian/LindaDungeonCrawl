from constants import MAP_BORDER_CHAR, MAP_CELL_SIZE
from model.enums import RoomType
from model.room import Room


class Map:

    # Initializes a map containing all empty rooms
    def __init__(self, map_rows: int, map_columns: int):
        self.map_grid = []
        for row in range(map_rows):
            for _ in range(map_columns):
                self.map_grid[row].append(Room(RoomType.EMPTY))
    
    # Sets the room at (row, col) to the provided Room object
    def set_room(self, room: Room, row: int, col: int):
        self.map_grid[row][col] = room

    def debug_print(self):
        for row in len(self.map_grid):
            debug_print_row(self.map_grid[row])

def print_map_cell_vert_border():
    print(MAP_BORDER_CHAR * MAP_CELL_SIZE)

def print_map_cell_text(text_index, row):
    # Noah TODO implement this
    print()

def debug_print_row(row):
    # Top for loop iterates over rows of text
    for i in range(MAP_CELL_SIZE):
        for room in row:
            if i % MAP_CELL_SIZE == 0:
                print_map_cell_vert_border()
            elif i % MAP_CELL_SIZE == (MAP_CELL_SIZE / 2):
                print_map_cell_text(0, room)
            elif i % MAP_CELL_SIZE == (MAP_CELL_SIZE / 2 + 1):
                print_map_cell_text(1, room)