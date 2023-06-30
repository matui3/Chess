import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_BISHOP, WHITE_BISHOP, WHITE, BLACK, COLS, ROWS

class Bishop(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_BISHOP, BLACK_BISHOP)

    def move(self, row, col):
        super().move(row, col)


    def valid_moves(self, board):
        valid_moves = []
        positions = board.board_state()
        current = self._current_position()
        # diagonal for going up-left
        current_col = self.col
        current_row = self.row
        while current_row-1 > -1 and current_col-1 > -1:
            if positions[current_row][current_col].get_piece() != None:
                valid_moves.append((current_row, current_col))
                break
            else:
                valid_moves.append((current_row, current_col))
            current_col -= 1
            current_row -= 1
            
        # reset current_col counter
        # diagonal for going up-right
        current_col = self.col
        current_row = self.row
        while  current_row-1 > -1 and current_col+1 < COLS:
            if positions[current_row][current_col].get_piece() != None:
                valid_moves.append((current_row, current_col))
                break
            else:
                valid_moves.append((current_row, current_col))
            current_col += 1
            current_row -= 1
        
        # diagonal for going down-right
        current_col = self.col
        current_row = self.row
        while current_row + 1 < ROWS and current_col + 1 < COLS:
            if positions[current_row][current_col].get_piece() != None:
                valid_moves.append((current_row, current_col))
                break
            else:
                valid_moves.append((current_row, current_col))
            current_col += 1
            current_row += 1

        # diagonal for going down-left
        current_col = self.col
        current_row = self.row
        while current_row +1 < ROWS and current_col -1 > -1:
            if positions[current_row][current_col].get_piece() != None:
                valid_moves.append((current_row, current_col))
                break
            else:
                valid_moves.append((current_row, current_col))
            current_col += 1
            current_row -= 1

        return valid_moves

    def __repr__(self):
        return super().__repr__() + ' B'