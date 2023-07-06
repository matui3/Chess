
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
    
    def attacking_moves(self):
        attacking_moves = []
        diag_moves_up_left = Bishop.attacking_moves_up_left_diagonal(self)
        diag_moves_up_right= Bishop.attacking_moves_up_right_diagonal(self)
        diag_moves_down_left = Bishop.attacking_moves_down_left_diagonal(self)
        diag_moves_down_right = Bishop.attacking_moves_down_right_diagonal(self)
        linear_moves_left = Rook.attacking_moves_left(self)
        linear_moves_right = Rook.attacking_moves_right(self)
        linear_moves_up = Rook.attacking_moves_up(self)
        linear_moves_down = Rook.attacking_moves_down(self)
        self._create_list_of_attacking_moves(diag_moves_up_left)
        self._create_list_of_attacking_moves(diag_moves_up_right)
        self._create_list_of_attacking_moves(diag_moves_down_left)
        self._create_list_of_attacking_moves(diag_moves_down_right)
        self._create_list_of_attacking_moves(linear_moves_left)
        self._create_list_of_attacking_moves(linear_moves_right)
        self._create_list_of_attacking_moves(linear_moves_up)
        self._create_list_of_attacking_moves(linear_moves_down)
        return attacking_moves
    
    def _create_list_of_attacking_moves(self, list_of_attacking_moves):
        for move in list_of_attacking_moves:
            list_of_attacking_moves.append(move)