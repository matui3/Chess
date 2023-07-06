import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_ROOK, WHITE_ROOK, WHITE, COLS, ROWS

class Rook(Piece):

    def __init__(self, square, color):
        super().__init__(square, color)

    def calc_pos(self):
        super().calc_pos()
        
    def draw(self, win):
        super().draw(win, WHITE_ROOK, BLACK_ROOK)

    def move(self, row, col):
        super().move(row, col)

    def valid_moves(self, board):
        valid_moves = [] # this will store a row, col
        # current pos is self.row, self.col
        positions = board.board_state()
        if self.col > 0:
            for col in range(self.col-1, -1, -1):
                if positions[self.row][col].get_piece() != None:
                    valid_moves.append((self.row, col))
                    break
                else:
                    valid_moves.append((self.row, col))
        if self.col < COLS:
            for col in range(self.col+1, COLS, 1):
                if positions[self.row][col].get_piece() != None:
                    valid_moves.append((self.row, col))
                    break
                else:
                    valid_moves.append((self.row, col))

        if self.row > 0:
            for row in range(self.row - 1, -1, -1):
                if positions[row][self.col].get_piece() != None:
                    valid_moves.append((row, self.col))
                    break
                else:
                    valid_moves.append((row, self.col))

        if self.row < ROWS:
            for row in range(self.row + 1, ROWS, 1):
                if positions[row][self.col].get_piece() != None:
                    valid_moves.append((row, self.col))
                    break
                else:
                    valid_moves.append((row, self.col))
        return valid_moves


        

    def __repr__(self):
        return super().__repr__() + ' R'
    
    def attacking_moves_left(self):
        attacking_moves = []
        # this will store a row, col
        # current pos is self.row, self.col
        if self.col > 0:
            for col in range(self.col-1, -1, -1):
                attacking_moves.append((self.row, col))
        return attacking_moves
    
    def attacking_moves_right(self):
        attacking_moves = []
        if self.col < COLS:
            for col in range(self.col+1, COLS, 1):
                attacking_moves.append((self.row, col))
        return attacking_moves
    
    def attacking_moves_up(self):
        attacking_moves = []
        if self.row > 0:
            for row in range(self.row - 1, -1, -1):
                attacking_moves.append((row, self.col))
        return attacking_moves

    def attacking_moves_down(self):
        attacking_moves = []
        if self.row < ROWS:
            for row in range(self.row + 1, ROWS, 1):
                attacking_moves.append((row, self.col))
        return attacking_moves