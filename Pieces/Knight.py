import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_KNIGHT, WHITE_KNIGHT, WHITE, ROWS, COLS, FILES

class Knight(Piece):

    def __init__(self, square, color):
        super().__init__(square, color)
        

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_KNIGHT, BLACK_KNIGHT)

    def move(self, row, col):
        super().move(row, col)

    def valid_moves(self, squares):
        
        valid_moves = []
        curr_square = self.get_square()
        rank = self.rank
        file = self.file

        if (rank + 2 < 8 and file + 1 < 8):
            valid_moves.append(squares[FILES[file+1] + str(rank + 2)])


        
        return valid_moves

    def __repr__(self):
        return super().__repr__() + ' N'