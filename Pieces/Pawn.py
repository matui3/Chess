
import pygame
import sys
sys.path.append('..')


from Piece import Piece
from ChessConstants import WHITE_PAWN, BLACK_PAWN, WHITE, BLACK, ROWS, COLS, FILES

class Pawn(Piece):

    def __init__(self, square, color):
        super().__init__(square, color)
        self.first_move = True
        

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_PAWN, BLACK_PAWN)

    def move(self, row, col):
        super().move(row, col)
 

    def _moves_based_on_color(self, current_square, valid_moves, color, squares):
        file = current_square.get_file_idx()
        rank = current_square.get_rank()
        direction = -1 if color == BLACK else 1
        if squares[FILES[file] + str(rank + direction * 1)]:
            if squares[FILES[file] + str(rank + direction * 1)].get_piece() == None:
                valid_moves.append(squares[FILES[file] + str(rank + direction * 1)])
            if squares[FILES[file] + str(rank + direction * 2)]:
                if squares[FILES[file] + str(rank + direction * 2)].get_piece() == None and self.first_move:
                    valid_moves.append(squares[file + str(rank + direction * 2)])
        
        # below is for a pawn capturing on the right
        
        if squares[FILES[file + 1] + str(rank + direction * 1)]:
            if squares[FILES[file] + str(rank + direction * 1)].get_piece() != None:
                valid_moves.append(squares(FILES[file + 1] + str(rank + direction * 1)))

        if squares[FILES[file - 1] + str(rank + direction * 1)]:
            if squares[FILES[file] + str(rank + direction * 1)].get_piece() != None:
                valid_moves.append(squares(FILES[file - 1] + str(rank + direction * 1)))



    def valid_moves(self, squares) -> list:
        current_square = self.get_square()
        valid_moves = []
        self._moves_based_on_color(current_square, valid_moves, self.color, squares)
        return valid_moves
                        
    def __repr__(self):
        return super().__repr__() + ' P'
    

    # will restructure this later
    def attacking_moves(self, board):
        attacking_moves = []
        if self.col + 1 < COLS and self.row - 1 > -1:
            attacking_moves.append((self.row-1, self.col + 1))
        if self.row - 1 > -1 and self.col - 1 > -1:
            attacking_moves.append((self.row-1, self.col))

        return attacking_moves