import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_KING, WHITE_KING, WHITE, ROWS, COLS

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

    def move(self, row, col):
        self.first_move = False
        super().move(row, col)


    def valid_moves(self, board):
        valid_moves = []
        # current_row = self.row
        # current_col = self.col
        # positions = board.board_state()
        # # check l/r of king
        # if current_col - 1 > -1:
        #     if positions[current_row][current_col-1].get_piece() == None:
        #         valid_moves.append((current_row, current_col-1))
        #     else:
        #         valid_moves.append((current_row, current_col-1))
    
        # if current_col + 1 < COLS:
        #     if positions[current_row][current_col + 1].get_piece() == None:
        #         valid_moves.append((current_row, current_col - 1))
        #     else:
        #         valid_moves.append((current_row, current_col))
        
        # if current_row - 1 > -1:
        #     if positions[current_row - 1][current_col].get_piece() == None:
        #         valid_moves.append((current_row -1, current_col))
        
        # if current_row + 1 < ROWS:
        #     if positions[current_row + 1][current_col].get_piece() == None:
        #         valid_moves.append((current_row + 1, current_col))

        # if current_row - 1 > -1 and current_col - 1 > -1:
        #     if positions[current_row - 1][current_col - 1].get_piece() == None:
        #         valid_moves.append((current_row - 1, current_col))

        # if current_row -1 > -1 and current_col + 1 < COLS:
        #     if positions[current_row - 1][current_col + 1].get_piece() == None:
        #         valid_moves.append((current_row -1, current_col + 1))

        # if current_row + 1 < ROWS and current_col - 1 > -1:
        #     if positions[current_row + 1][current_col - 1].get_piece() == None:
        #         valid_moves.append((current_row + 1, current_col - 1))

        # if current_row + 1 < ROWS and current_col + 1 < COLS:
        #     if positions[current_row + 1][current_col + 1].get_piece() == None:
        #         valid_moves.append((current_row + 1, current_col + 1))

        # # figuring out how to not put yourself in check
        

        return valid_moves

    def __repr__(self):
        return super().__repr__() + ' K'
    
    def switch_check_status(self):
        self.check = not self.check
        return self.check