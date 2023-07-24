
import pygame
import sys
sys.path.append('..')


from Piece import Piece
from ChessConstants import WHITE_PAWN, BLACK_PAWN, BLACK, FILES

class Pawn(Piece):

    def __init__(self, square, color):
        super().__init__(square, color)
        self.first_move = True
        

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_PAWN, BLACK_PAWN)

    def move(self, new_square):
        super().move(new_square)
 

    def _moves_based_on_color(self, valid_moves, squares, direction):
        
        if (self.rank + direction * 1 < 8 and self.rank + direction * 1 > -1):
            if squares[FILES[self.file] + str(self.rank + direction * 1)].get_piece() == None:
                valid_moves.append(squares[FILES[self.file] + str(self.rank + direction * 1)])
                if squares[FILES[self.file] + str(self.rank + direction * 2)].get_piece() == None and self.first_move:
                    valid_moves.append(squares[FILES[self.file] + str(self.rank + direction * 2)])
        # below is for a pawn capturing on the right
        # self.attacking_moves(valid_moves, squares, direction)



    def valid_moves(self, squares) -> list:
        valid_moves = []
        direction = -1 if self.color == BLACK else 1
        self._moves_based_on_color(valid_moves, squares, direction)
        return valid_moves
                        
    def __repr__(self):
        return super().__repr__() + ' P'
    

    def attacking_moves(self, valid_moves, squares, direction):
        attacking_moves = []
        # this should check the right file
        if (self.file + 1 < 8) and (self.rank + direction * 1 < 8 and self.rank + direction * 1 > -1):
            if squares[FILES[self.file + 1] + str(self.rank + direction * 1)].get_piece() != None:
               valid_moves.append(squares(FILES[self.file + 1] + str(self.rank + direction * 1)))
               attacking_moves.append(squares(FILES[self.file + 1] + str(self.rank + direction * 1)))
        # this checks diagonal to the left
        if (self.file + 1 < 8) and (self.rank + direction * 1 < 8 and self.rank + direction * 1 > -1):
            if squares[FILES[self.file] + str(self.rank + direction * 1)].get_piece() != None:
                valid_moves.append(squares(FILES[self.file - 1] + str(self.rank + direction * 1)))
                attacking_moves.append(squares(FILES[self.file - 1] + str(self.rank + direction * 1)))
                
        return attacking_moves
    
    def attacking_moves(self, valid_moves, squares, direction, rank, file):
        attacking_moves = []
        # this should check the right file
        if (self.file + 1 < 8) and (self.rank + direction * 1 < 8 and self.rank + direction * 1 > -1):
            if squares[FILES[self.file + 1] + str(self.rank + direction * 1)].get_piece() != None:
               valid_moves.append(squares(FILES[self.file + 1] + str(self.rank + direction * 1)))
               attacking_moves.append(squares(FILES[self.file + 1] + str(self.rank + direction * 1)))
        # this checks diagonal to the left
        if (self.file + 1 < 8) and (self.rank + direction * 1 < 8 and self.rank + direction * 1 > -1):
            if squares[FILES[self.file] + str(self.rank + direction * 1)].get_piece() != None:
                valid_moves.append(squares(FILES[self.file - 1] + str(self.rank + direction * 1)))
                attacking_moves.append(squares(FILES[self.file - 1] + str(self.rank + direction * 1)))
                
        return attacking_moves