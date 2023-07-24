import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_KING, WHITE_KING, WHITE, ROWS, COLS, FILES

class King(Piece):

    def __init__(self, square, color):
        super().__init__(square, color)
        self.check = False
        self.first_move = True
        
    
    def king_position(self):
        return (self.row, self.col)

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_KING, BLACK_KING)

    def move(self, new_square):
        self.first_move = False
        super().move(new_square)


    def valid_moves(self, squares):
        valid_moves = []
        rank = self.rank
        file = self.file

        if (rank + 1 < 8 and file + 1 < 8):
            valid_moves.append(squares[FILES[file + 1] + str(rank+1)])

        if (rank + 1 < 8):
            valid_moves.append(squares[FILES[self.file] + str(rank + 1)])

        if (rank + 1 < 8 and file - 1 < 8):
            valid_moves.append(squares[FILES[file - 1] + str(rank + 1)])

        if (file + 1 < 8):
            valid_moves.append(squares[FILES[file + 1] + str(self.rank)])

        if (file - 1 > - 1):
            valid_moves.append(squares[FILES[file - 1] + str(self.rank)])

        if (rank - 1 > -1 and file + 1 < 8):
            valid_moves.append(squares[FILES[file+1] + str(rank-1)])

        if (rank -1 > -1):
            valid_moves.append(squares[FILES[self.file] + str(rank - 1)])

        if (rank - 1 > -1 and file - 1 > -1):
            valid_moves.append(squares[FILES[file -1] + str(rank - 1)])
        
        return valid_moves

    def __repr__(self):
        return super().__repr__() + ' K'
    
    def switch_check_status(self):
        self.check = not self.check
        return self.check