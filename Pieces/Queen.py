
import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_QUEEN, WHITE_QUEEN, WHITE, ROWS, COLS
from .Bishop import Bishop
from .Rook import Rook

class Queen(Piece):

    def __init__(self, square, color):
        super().__init__(square, color)

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_QUEEN, BLACK_QUEEN)

    def move(self, new_square):
        super().move(new_square)
  

    def valid_moves(self, squares):
        valid_moves = []
        diag_moves = Bishop.valid_moves(self, squares)
        linear_moves = Rook.valid_moves(self, squares)
        for move in diag_moves:
            valid_moves.extend(move)
        for move in linear_moves:
            valid_moves.extend(move)

        return valid_moves

    def __repr__(self):
        return super().__repr__() + ' Q'
    