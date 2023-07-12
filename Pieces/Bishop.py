import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_BISHOP, WHITE_BISHOP, WHITE, BLACK, COLS, ROWS, FILES
from .King import King

class Bishop(Piece):

    def __init__(self, square,  color):
        super().__init__(square, color)
        

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_BISHOP, BLACK_BISHOP)

    def move(self, row, col):
        super().move(row, col)


    def valid_moves(self, squares):
        valid_moves = []
        curr_rank = self.rank
        curr_file = self.file
        
        # moving to the right and up
        while (curr_rank + 1 < ROWS and curr_file + 1 < COLS):
            curr_file += 1
            curr_rank += 1
            if (squares[FILES[curr_file] + str(curr_rank)].get_piece()) == None:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
            else:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
                break
        
        # moving left and up
        while (curr_rank + 1 < ROWS and curr_file - 1 > -1):
            curr_file -= 1
            curr_rank += 1
            if (squares[FILES[curr_file] + str(curr_rank)].get_piece()) == None:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
            else:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
                break

        # moving down and right

        while (curr_rank - 1 > -1 and curr_file + 1 < COLS):
            curr_file += 1
            curr_rank -= 1
            if (squares[FILES[curr_file] + str(curr_rank)].get_piece()) == None:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
            else:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
                break

        # moving down and to the left
        while (curr_rank - 1 > - 1 and curr_file - 1 > -1):
            curr_file -= 1
            curr_rank -= 1
            if (squares[FILES[curr_file] + str(curr_rank)].get_piece()) == None:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
            else:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
                break

        return valid_moves

    def __repr__(self):
        return super().__repr__() + ' B'
    
    def attacking_moves_up_left_diagonal(self):
        attacking_moves = []
        current_col = self.col - 1
        current_row = self.row - 1
        while current_row > -1 and current_col > -1:
            attacking_moves.append((current_row, current_col))
            current_col -= 1
            current_row -= 1

        return attacking_moves
    
    def attacking_moves_up_right_diagonal(self):
        attacking_moves = []
        # reset current_col counter
        # diagonal for going up-right
        current_col = self.col + 1
        current_row = self.row - 1
        while current_row-1 > -1 and current_col+1 < COLS:
            attacking_moves.append((current_row, current_col))
            current_col += 1
            current_row -= 1
        return attacking_moves
    
    def attacking_moves_down_right_diagonal(self):
        attacking_moves = []
        # diagonal for going down-right
        current_col = self.col + 1
        current_row = self.row + 1
        while current_row < ROWS and current_col < COLS:
            attacking_moves.append((current_row, current_col))
            current_col += 1
            current_row += 1
        return attacking_moves
    
    def attacking_moves_down_left_diagonal(self):
        attacking_moves = []
        # diagonal for going down-left
        current_col = self.col - 1
        current_row = self.row + 1
        while current_row < ROWS and current_col > -1:
            attacking_moves.append((current_row, current_col))
            current_col += 1
            current_row -= 1
        return attacking_moves