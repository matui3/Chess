from ChessConstants import SQUARE_SIZE, WHITE

class Piece:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.selected_square = None
        self.calc_pos()
        

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win, white, black):
        if self.color == WHITE:
            win.blit(white, (self.x - white.get_width()//2, self.y - white.get_height()//2))
        else:
            win.blit(black, (self.x - black.get_width()//2, self.y - black.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        
    def __repr__(self):
        return str(self.color)
    