import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_BISHOP, WHITE_BISHOP, WHITE, BLACK, COLS, ROWS
from King import King

class Bishop(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.valid_moves = []

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_BISHOP, BLACK_BISHOP)

    def move(self, row, col):
        super().move(row, col)


    def valid_moves(self, board):
        valid_moves = []
        positions = board.board_state()

        # thinking about how to handle check
        # overlapping valid moves...
        # diagonal for going up-left
        current_col = self.col - 1
        current_row = self.row - 1
        piece = positions[current_row][current_col].get_piece()
        while current_row > -1 and current_col > -1:
            self.attacking_moves.append((current_row, current_col))
            if piece != None and type(piece) != King and piece.color != self.color:
                valid_moves.append((current_row, current_col))
                break
            else:
                valid_moves.append((current_row, current_col))
            current_col -= 1
            current_row -= 1
            
        # reset current_col counter
        # diagonal for going up-right
        current_col = self.col + 1
        current_row = self.row - 1
        while  current_row-1 > -1 and current_col+1 < COLS:
            self.attacking_moves.append((current_row, current_col))
            if piece != None and type(piece) != King and piece.color != self.color:
                valid_moves.append((current_row, current_col))
                break
            else:
                valid_moves.append((current_row, current_col))
            current_col += 1
            current_row -= 1
        
        # diagonal for going down-right
        current_col = self.col + 1
        current_row = self.row + 1
        while current_row < ROWS and current_col < COLS:
            self.attacking_moves.append((current_row, current_col))
            if piece != None and type(piece) != King and piece.color != self.color:
                valid_moves.append((current_row, current_col))
                break
            else:
                valid_moves.append((current_row, current_col))
            current_col += 1
            current_row += 1

        # diagonal for going down-left
        current_col = self.col - 1
        current_row = self.row + 1
        while current_row < ROWS and current_col > -1:
            self.attacking_moves.append((current_row, current_col))
            if piece != None and type(piece) != King and piece.color != self.color:
                valid_moves.append((current_row, current_col))
                break
            else:
                valid_moves.append((current_row, current_col))
            current_col += 1
            current_row -= 1

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
        while  current_row-1 > -1 and current_col+1 < COLS:
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