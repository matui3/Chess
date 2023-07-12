from ChessConstants import SQUARE_SIZE, WHITE

class Piece:

    def __init__(self, square, color):
        self.square = square
        self.color = color
        self.x = 0
        self.y = 0
        self.selected_square = None
        self.calc_pos()
        self.file = square.get_file_idx()
        self.rank = square.get_rank()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.square.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.square.row + SQUARE_SIZE // 2

    def draw(self, win, white, black):
        if self.color == WHITE:
            win.blit(white, (self.x - white.get_width()//2, self.y - white.get_height()//2))
        else:
            win.blit(black, (self.x - black.get_width()//2, self.y - black.get_height()//2))

    def move(self, new_square):
        self.square = new_square
        self.calc_pos()

    def get_square(self):
        return self.square
    
    def update_name(self, new_square):
        self.square = new_square

    def __repr__(self):
        return str(self.color)
    