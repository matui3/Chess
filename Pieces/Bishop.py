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

    def move(self, new_square):
        super().move(new_square)


    def valid_moves(self, squares):
        valid_moves = []
        curr_rank = self.rank
        curr_file = self.file
        
        # moving to the right and up
        while (curr_rank + 1 < ROWS and curr_file + 1 < COLS):
            curr_file += 1
            curr_rank += 1

            if (squares[FILES[curr_file] + str(curr_rank)].get_piece()) == None:
                squares[FILES[curr_file] + str(curr_rank)].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
            else:
                squares[FILES[curr_file] + str(curr_rank)].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
                break
        
        curr_rank = self.rank
        curr_file = self.file
        # moving left and up
        while (curr_rank + 1 < ROWS and curr_file - 1 > -1):
            curr_file -= 1
            curr_rank += 1
            if (squares[FILES[curr_file] + str(curr_rank)].get_piece()) == None:
                squares[FILES[curr_file] + str(curr_rank)].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
            else:
                squares[FILES[curr_file] + str(curr_rank)].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
                break
        

        curr_rank = self.rank
        curr_file = self.file
        # moving down and right
        while (curr_rank - 1 > 0 and curr_file + 1 < COLS):
            curr_file += 1
            curr_rank -= 1
            if (squares[FILES[curr_file] + str(curr_rank)].get_piece()) == None:
                squares[FILES[curr_file] + str(curr_rank)].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
            else:
                squares[FILES[curr_file] + str(curr_rank)].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
                break

        curr_rank = self.rank
        curr_file = self.file
        # moving down and to the left
        while (curr_rank - 1 > 0 and curr_file - 1 > -1):
            curr_file -= 1
            curr_rank -= 1
            if (squares[FILES[curr_file] + str(curr_rank)].get_piece()) == None:
                squares[FILES[curr_file] + str(curr_rank)].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
            else:
                squares[FILES[curr_file] + str(curr_rank)].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
                break
        return valid_moves

    def __repr__(self):
        return super().__repr__() + ' B'
    

    def attacked_moves(self, squares, file, rank):
        valid_moves = []
        curr_rank = rank
        curr_file = file
        
        # moving to the right and up
        while (curr_rank + 1 < ROWS and curr_file + 1 < COLS):
            curr_file += 1
            curr_rank += 1

            if (squares[FILES[curr_file] + str(curr_rank)].get_piece()) == None:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
            else:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
                break
        
        curr_rank = rank
        curr_file = file
        # moving left and up
        while (curr_rank + 1 < ROWS and curr_file - 1 > -1):
            curr_file -= 1
            curr_rank += 1
            if (squares[FILES[curr_file] + str(curr_rank)].get_piece()) == None:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
            else:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
                break
        

        curr_rank = rank
        curr_file = file
        # moving down and right
        while (curr_rank - 1 > 0 and curr_file + 1 < COLS):
            curr_file += 1
            curr_rank -= 1
            if (squares[FILES[curr_file] + str(curr_rank)].get_piece()) == None:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
            else:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
                break

        curr_rank = rank
        curr_file = file
        # moving down and to the left
        while (curr_rank - 1 > 0 and curr_file - 1 > -1):
            curr_file -= 1
            curr_rank -= 1
            if (squares[FILES[curr_file] + str(curr_rank)].get_piece()) == None:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
            else:
                valid_moves.append(squares[FILES[curr_file] + str(curr_rank)])
                break

        return valid_moves