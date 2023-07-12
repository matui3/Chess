import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_KNIGHT, WHITE_KNIGHT, WHITE, ROWS, COLS

class Knight(Piece):

    def __init__(self, square, color):
        super().__init__(square, color)
        

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_KNIGHT, BLACK_KNIGHT)

    def move(self, row, col):
        super().move(row, col)

    def valid_moves(self, board):
        # current position
        # you check up and down two rows and then left/right one column
        # you also check left/right two columns and then up and down one row
        valid_moves = []
        # positions = board.board_state()
        # current_row = self.row
        # current_col = self.col

        # # check left/right of going two below
        # if current_row + 2 < ROWS:
        #     if current_col - 1 > -1:
        #         if positions[current_row+2][current_col-1].get_piece() == None:
        #             valid_moves.append((current_row + 2, current_col - 1))
        #         else:
        #             valid_moves.append((current_row + 2, current_col - 1))
                    
        
        #     if current_col + 1 < COLS:
        #         if positions[current_row+2][current_col+1].get_piece() == None:
        #             valid_moves.append((current_row + 2, current_col + 1))
        #         else:
        #             valid_moves.append((current_row + 2, current_col + 1))
                    

        # # check L/R of two above
        # if current_row - 2 > -1:
        #     if current_col - 1 > -1:
        #         if positions[current_row - 2][current_col - 1].get_piece() == None:
        #             valid_moves.append((current_row - 2, current_col - 1))
        #         else:
        #             valid_moves.append((current_row - 2, current_col - 1))
                    

        #     if current_col + 1 < ROWS:
        #         if positions[current_row - 2][current_col + 1].get_piece() == None:
        #             valid_moves.append((current_row - 2, current_col + 1))
        #         else:
        #             valid_moves.append((current_row - 2, current_col + 1))
                    

        # # check up down of two to the left
        # if current_col - 2 > -1:
        #     if current_row - 1 > -1:
        #         if positions[current_row - 1][current_col - 2].get_piece() == None:
        #             valid_moves.append((current_row -1, current_col -2))
        #         else:
        #             valid_moves.append((current_row -1, current_col -2))
                    
            
        #     if current_row + 1 < ROWS:
        #         if positions[current_row + 1][current_col -2].get_piece() == None:
        #             valid_moves.append((current_row + 1, current_col - 2))
        #         else:
        #             valid_moves.append((current_row + 1, current_col - 2))
                    

        # # check up/down of two to the right
        # if current_col + 2 < COLS:
        #     if current_row - 1 > - 1:
        #         if positions[current_row -1][current_col + 2].get_piece() == None:
        #             valid_moves.append((current_row - 1, current_col + 2))
        #         else:
        #             valid_moves.append((current_row - 1, current_col + 2))
                    

        #     if current_row + 1 < ROWS:
        #         if positions[current_row + 1][current_col + 2].get_piece() == None:
        #             valid_moves.append((current_row + 1, current_col + 2))
        #         else:
        #             valid_moves.append((current_row + 1, current_col + 2))
                    
        
        return valid_moves

    def __repr__(self):
        return super().__repr__() + ' N'
    
    def attacking_moves(self, board):
        attacking_moves = []
        positions = board.board_state()
        current_row = self.row
        current_col = self.col

        # check left/right of going two below
        if current_row + 2 < ROWS:
            if current_col - 1 > -1:
                 attacking_moves.append((current_row + 2, current_col - 1))
    
            if current_col + 1 < COLS:
                attacking_moves.append((current_row + 2, current_col + 1))
                    

        # check L/R of two above
        if current_row - 2 > -1:
            if current_col - 1 > -1:
                attacking_moves.append((current_row - 2, current_col - 1))

            if current_col + 1 < ROWS:
                attacking_moves.append((current_row - 2, current_col + 1))
                
                    

        # check up down of two to the left
        if current_col - 2 > -1:
            if current_row - 1 > -1:
                attacking_moves.append((current_row -1, current_col -2))
                    
            
            if current_row + 1 < ROWS:
                attacking_moves.append((current_row + 1, current_col - 2))
                    

        # check up/down of two to the right
        if current_col + 2 < COLS:
            if current_row - 1 > - 1:
                attacking_moves.append((current_row - 1, current_col + 2))
                    

            if current_row + 1 < ROWS:
                attacking_moves.append((current_row + 1, current_col + 2))

        return attacking_moves