from constants import MAP_BORDER_CHAR, MAP_CELL_HEIGHT, MAP_CELL_WIDTH
from model.enums import RoomStatus, RoomType
from model.room import init_room
from lib.adventurelib import Room

class Map:

    # Initializes a map containing all empty rooms
    def __init__(self, map_rows: int, map_cols: int):
        self.map_grid = []
        self.map_rows = map_rows
        self.map_cols = map_cols
        self.current_room_row = -1
        self.current_room_col = -1

        for row in range(map_rows):
            for _ in range(map_cols):
                if len(self.map_grid) <= row:
                    self.map_grid.append([])
                self.map_grid[row].append(init_room(RoomType.EMPTY))
    
    # Sets the room at a given cell's coordinates to the provided Room object
    def init_map_cell(self, room: Room, row: int, col: int):
        self.map_grid[row][col] = room
        room.row = row
        room.col = col
        if row-1 >= 0 and self.map_grid[row-1][col].type != RoomType.EMPTY:
            room.north = self.map_grid[row-1][col]
        if row+1 < self.map_rows and self.map_grid[row+1][col].type != RoomType.EMPTY:
            room.south = self.map_grid[row+1][col]
        if col-1 >= 0 and self.map_grid[row][col-1].type != RoomType.EMPTY:
            room.west = self.map_grid[row][col-1]
        if col+1 < self.map_cols and self.map_grid[row][col+1].type != RoomType.EMPTY:
            room.east = self.map_grid[row][col+1]

    def set_current_room(self, row: int, col: int):
        self.current_room_row = row
        self.current_room_col = col
        self.map_grid[row][col].status = RoomStatus.VISITED
        self.set_adjacent_rooms_seen(row, col)

    def set_adjacent_rooms_seen(self, row: int, col: int):
        if row-1 >= 0 and self.map_grid[row-1][col].type != RoomType.EMPTY and self.map_grid[row-1][col].status == RoomStatus.UNSEEN:
            self.map_grid[row-1][col].status = RoomStatus.SEEN
        if row+1 < self.map_rows and self.map_grid[row+1][col].type != RoomType.EMPTY and self.map_grid[row+1][col].status == RoomStatus.UNSEEN:
            self.map_grid[row+1][col].status = RoomStatus.SEEN
        if col-1 >= 0 and self.map_grid[row][col-1].type != RoomType.EMPTY and self.map_grid[row][col-1].status == RoomStatus.UNSEEN:
            self.map_grid[row][col-1].status = RoomStatus.SEEN
        if col+1 < self.map_cols and self.map_grid[row][col+1].type != RoomType.EMPTY and self.map_grid[row][col+1].status == RoomStatus.UNSEEN:
            self.map_grid[row][col+1].status = RoomStatus.SEEN

    def get_current_room(self):
        return self.map_grid[self.current_room_row][self.current_room_col]

    # TODO: we probably want a "see_adjacent_rooms" function, to mark
    # adjacent rooms to the one currently being visited as SEEN status

    def print(self):
        for row in range(len(self.map_grid)):
            self.print_row(self.map_grid[row])
        self.print_map_vert_border(len(self.map_grid[0]))

    def print_map_vert_border(self, num_cols):
        for _ in range(num_cols):
            self.print_all_border_chars()
        print(MAP_BORDER_CHAR)

    def print_all_border_chars(self):
        print(MAP_BORDER_CHAR * MAP_CELL_WIDTH, end = '')

    # Prints the text (middle two lines) of a map cell
    # - For unseen or empty rooms, prints all border chars
    # - For seen rooms, prints ????
    # - For visited rooms, prints room text
    def print_map_cell_text(self, text_index, room):
        if room.type == RoomType.EMPTY or room.status == RoomStatus.UNSEEN:
            self.print_all_border_chars()
        elif room.status == RoomStatus.SEEN:
            print(MAP_BORDER_CHAR + '????'.center(MAP_CELL_WIDTH - 1), end='')
        elif room.status == RoomStatus.VISITED:
            if text_index < len(room.room_text):
                text_to_print = room.room_text[text_index].center(MAP_CELL_WIDTH - 1)
                if room.row == self.current_room_row and room.col == self.current_room_col:
                    text_to_print = '\033[92m' + text_to_print + '\033[0m'
                print(MAP_BORDER_CHAR + text_to_print, end='')
            else:
                self.print_empty_line(room)

    # Prints an empty line.
    # - For unseen or empty rooms, prints all border chars
    # - For seen or visited rooms, prints border chars with white space in the middle
    def print_empty_line(self, room):
        if room.type == RoomType.EMPTY or room.status == RoomStatus.UNSEEN:
            self.print_all_border_chars()
        else:
            print(MAP_BORDER_CHAR + ' ' * (MAP_CELL_WIDTH - 1), end='')

    # Prints one row of cells in the map
    def print_row(self, row):
        self.print_map_vert_border(len(row))
        for i in range(MAP_CELL_HEIGHT):
            for room in row:
                if i % MAP_CELL_HEIGHT == (MAP_CELL_HEIGHT / 2 - 1):
                    self.print_map_cell_text(0, room)
                elif i % MAP_CELL_HEIGHT == (MAP_CELL_HEIGHT / 2):
                    self.print_map_cell_text(1, room)
                else:
                    self.print_empty_line(room)
            print(MAP_BORDER_CHAR)
    