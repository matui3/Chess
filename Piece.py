from .ChessConstants import SQUARE_SIZE

class Piece:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0

        self.calc_pos()

    def position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def valid_move(self):
        pass

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    