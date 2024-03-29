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

    def move(self, new_square):
        super().move(new_square)

    def valid_moves(self, squares):
        
        valid_moves = []
        rank = self.rank
        file = self.file

        # up 2 and right 1
        if (rank + 2 < 8 and file + 1 < 8):
            valid_moves.append(squares[FILES[file + 1] + str(rank + 2)])
            squares[FILES[file + 1] + str(rank + 2)].update_piece_reference_list(self)

        # up 2 and left 1
        if (rank + 2 < 8 and file - 1 > -1):
            valid_moves.append(squares[FILES[file - 1] + str(rank + 2)])
            squares[FILES[file - 1] + str(rank + 2)].update_piece_reference_list(self)

        # down 2 and right 1
        if (rank - 2 > 0 and file + 1 < 8):
            valid_moves.append(squares[FILES[file + 1] + str(rank - 2)])
            squares[FILES[file + 1] + str(rank - 2)].update_piece_reference_list(self)

        # down 2 and left 1
        if (rank - 2 > 0 and file - 1 > -1):
            valid_moves.append(squares[FILES[file - 1] + str(rank - 2)])
            squares[FILES[file - 1] + str(rank - 2)].update_piece_reference_list(self)

        # right 2 and up 1
        if (rank + 1 < 8 and file + 2 < 8):
            valid_moves.append(squares[FILES[file + 2] + str(rank + 1)])
            squares[FILES[file + 2] + str(rank + 1)].update_piece_reference_list(self)

        # left 2 and up 1
        if (rank + 1 < 8 and file - 2 > -1):
            valid_moves.append(squares[FILES[file - 2] + str(rank + 1)])
            squares[FILES[file - 2] + str(rank + 1)].update_piece_reference_list(self)

        # right 2 and down 1
        if (rank - 1 > 0 and file + 2 < 8):
            valid_moves.append(squares[FILES[file + 2] + str(rank - 1)])
            squares[FILES[file + 2] + str(rank - 1)].update_piece_reference_list(self)

        # left 2 and down 1
        if (rank - 1 > 0 and file - 2 > -1):
            valid_moves.append(squares[FILES[file - 2] + str(rank - 1)])
            squares[FILES[file - 2] + str(rank - 1)].update_piece_reference_list(self)

        return valid_moves

    def __repr__(self):
        return super().__repr__() + ' N'
    
    def attacked_moves(self, squares, file, rank):
        
        valid_moves = []

        # up 2 and right 1
        if (rank + 2 < 8 and file + 1 < 8):
            valid_moves.append(squares[FILES[file + 1] + str(rank + 2)])

        # up 2 and left 1
        if (rank + 2 < 8 and file - 1 > -1):
            valid_moves.append(squares[FILES[file - 1] + str(rank + 2)])

        # down 2 and right 1
        if (rank - 2 > 0 and file + 1 < 8):
            valid_moves.append(squares[FILES[file + 1] + str(rank - 2)])

        # down 2 and left 1
        if (rank - 2 > 0 and file - 1 > -1):
            valid_moves.append(squares[FILES[file - 1] + str(rank - 2)])

        # right 2 and up 1
        if (rank + 1 < 8 and file + 2 < 8):
            valid_moves.append(squares[FILES[file + 2] + str(rank + 1)])

        # left 2 and up 1
        if (rank + 1 < 8 and file - 2 > -1):
            valid_moves.append(squares[FILES[file - 2] + str(rank + 1)])


        # right 2 and down 1
        if (rank - 1 > 0 and file + 2 < 8):
            valid_moves.append(squares[FILES[file + 2] + str(rank - 1)])

        # left 2 and down 1
        if (rank - 1 > 0 and file - 2 > -1):
            valid_moves.append(squares[FILES[file - 2] + str(rank - 1)])
            
        return valid_moves