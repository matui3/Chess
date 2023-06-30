import pygame
from Board import Board
from ChessConstants import WHITE, BLACK, COLOR1, SQUARE_SIZE

class Game:
    def __init__(self, win):
        
        self.win = win
        self._init()

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = []

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result.get_piece():
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_square(row, col).get_piece()
            if piece != None:
                if piece.color == self.turn:
                    self.selected = piece
                    self.valid_moves = self.board.get_valid_moves(piece)
                    return True
        return False
            


    def _move(self, row, col):
        square = self.board.get_square(row, col)
        if self.selected and square.get_piece() == None and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        elif self.selected and square.get_piece() != None and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        
        return True
    
    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, COLOR1, (row * SQUARE_SIZE - SQUARE_SIZE//2, col * SQUARE_SIZE - SQUARE_SIZE//2), 15)