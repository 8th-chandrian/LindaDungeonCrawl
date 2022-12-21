from constants import MAP_BORDER_CHAR, MAP_CELL_HEIGHT, MAP_CELL_WIDTH
from model.enums import RoomStatus, RoomType
from model.room import Room


class Map:

    # Initializes a map containing all empty rooms
    def __init__(self, map_rows: int, map_columns: int):
        self.map_grid = []
        self.starting_room_row = -1
        self.starting_room_col = -1

        for row in range(map_rows):
            for _ in range(map_columns):
                if len(self.map_grid) <= row:
                    self.map_grid.append([])
                self.map_grid[row].append(Room(RoomType.EMPTY))
    
    # Sets the room at (row, col) to the provided Room object
    def set_room(self, room: Room, row: int, col: int):
        self.map_grid[row][col] = room

    # TODO: we should probably make a more general "visit_room" function
    # that marks the room being visited as VISITED and the adjacent rooms
    # that were previously UNSEEN as SEEN
    def set_starting_room_coords(self, row: int, col: int):
        self.starting_room_row = row
        self.starting_room_col = col
        self.map_grid[row][col].set_status(RoomStatus.VISITED)

    # TODO: we probably want a "see_adjacent_rooms" function, to mark
    # adjacent rooms to the one currently being visited as SEEN status

    def print(self):
        for row in range(len(self.map_grid)):
            print_row(self.map_grid[row])
        print_map_vert_border(len(self.map_grid[0]))

def print_map_vert_border(num_cols):
    for _ in range(num_cols):
        print_all_border_chars()
    print(MAP_BORDER_CHAR)

def print_all_border_chars():
    print(MAP_BORDER_CHAR * MAP_CELL_WIDTH, end = '')

# Prints the text (middle two lines) of a map cell
# - For unseen or empty rooms, prints all border chars
# - For seen rooms, prints ????
# - For visited rooms, prints room text
def print_map_cell_text(text_index, room):
    if room.type == RoomType.EMPTY or room.status == RoomStatus.UNSEEN:
        print_all_border_chars()
    elif room.status == RoomStatus.SEEN:
        print(MAP_BORDER_CHAR + '????'.center(MAP_CELL_WIDTH - 1), end='')
    elif room.status == RoomStatus.VISITED:
        if text_index < len(room.room_text):
            print(MAP_BORDER_CHAR + room.room_text[text_index].center(MAP_CELL_WIDTH - 1), end='')
        else:
            print_empty_line(room)

# Prints an empty line.
# - For unseen or empty rooms, prints all border chars
# - For seen or visited rooms, prints border chars with white space in the middle
def print_empty_line(room):
    if room.type == RoomType.EMPTY or room.status == RoomStatus.UNSEEN:
        print_all_border_chars()
    else:
        print(MAP_BORDER_CHAR + ' ' * (MAP_CELL_WIDTH - 1), end='')

# Prints one row of cells in the map
def print_row(row):
    print_map_vert_border(len(row))
    for i in range(MAP_CELL_HEIGHT):
        for room in row:
            if i % MAP_CELL_HEIGHT == (MAP_CELL_HEIGHT / 2 - 1):
                print_map_cell_text(0, room)
            elif i % MAP_CELL_HEIGHT == (MAP_CELL_HEIGHT / 2):
                print_map_cell_text(1, room)
            else:
                print_empty_line(room)
        print(MAP_BORDER_CHAR)
    