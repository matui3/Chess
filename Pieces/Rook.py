import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_ROOK, WHITE_ROOK, WHITE

class Rook(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_ROOK, BLACK_ROOK)

    def move(self, row, col):
        super().move(row, col)

    def valid_moves(self, board):
        self.valid_moves = [] # this will store a row, col
        # current pos is self.row, self.col
        positions = board.board_state()
        for col in range(self.col, 0, -1):
            if positions[self.row][col].get_piece() == None:
                break
            else:
                self.valid_moves.append((self.row, col))
        return self.valid_moves



                # only wnats the current colum and row the rook is in

        

    def __repr__(self):
        return super().__repr__() + 'R'