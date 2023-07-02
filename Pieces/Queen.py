
import pygame
import sys
sys.path.append('..')

from Piece import Piece
from King import King
from ChessConstants import BLACK_QUEEN, WHITE_QUEEN, WHITE, ROWS, COLS
from Bishop import Bishop
from Rook import Rook

class Queen(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_QUEEN, BLACK_QUEEN)

    def move(self, row, col):
        super().move(row, col)
  

    def valid_moves(self, board):
        valid_moves = []
        diag_moves = Bishop.valid_moves(self, board)
        linear_moves = Rook.valid_moves(self, board)
        for move in diag_moves:
            valid_moves.append(move)
        for move in linear_moves:
            valid_moves.append(move)
        # diagonal for going up-left

        return valid_moves

    def __repr__(self):
        return super().__repr__() + ' Q'
    
    def attacking_moves(self, board):
        attacking_moves = []
        diag_moves = Bishop.attacking_moves(self, board)
        linear_moves = Rook.attacking_moves(self, board)
        for move in diag_moves:
            attacking_moves.append(move)
        for move in linear_moves:
            attacking_moves.append(move)
        return attacking_moves