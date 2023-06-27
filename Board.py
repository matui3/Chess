import Square

class Board:

    # this will represent configation of the board aka where pieces are
    # might do this on console first

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_width = width // 8
        self.tile_height = height // 8
        # I will create a surface with the initialization of board



    def display_board(self):
        pass