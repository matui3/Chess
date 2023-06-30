
import pygame
import sys
sys.path.append('..')


from Piece import Piece
from ChessConstants import WHITE_PAWN, BLACK_PAWN, WHITE, BLACK, ROWS

class Pawn(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first_move = True

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_PAWN, BLACK_PAWN)

    def move(self, row, col):
        super().move(row, col)
 

    def valid_moves(self, board):

        positions = board.board_state()
        valid_moves = []
        if self.color == BLACK:
            if self.first_move:
                for row in range(self.row, self.row+3, 1):
                    if positions[row][self.col].get_piece() == None:
                        valid_moves.append((row, self.col))
            else:
                if self.row + 1 < ROWS:
                    if positions[self.row + 1][self.col].get_piece() == None:
                        valid_moves.append((self.row + 1, self.col))

                        
    def __repr__(self):
        return super().__repr__() + 'P'