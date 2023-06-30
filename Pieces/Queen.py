
import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_QUEEN, WHITE_QUEEN, WHITE, ROWS, COLS

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
        positions = board.board_state()
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
        return super().__repr__() + ' Q'