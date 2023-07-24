import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_ROOK, WHITE_ROOK, COLS, ROWS, FILES

class Rook(Piece):

    def __init__(self, square, color):
        super().__init__(square, color)
        self.first_move = True

    def calc_pos(self):
        super().calc_pos()
        
    def draw(self, win):
        super().draw(win, WHITE_ROOK, BLACK_ROOK)

    def move(self, new_square):
        super().move(new_square)

    def valid_moves(self, squares):
        valid_moves = []
        # before we check if a move is valid, we also need to look does this result in a king being in check? how do i check that... 
        # check all the squares up/left/right/down
        # I have a dictionary of all my squares
        # check everything in a file
        for rank in range(self.rank, ROWS + 1, 1):
            if squares[FILES[self.file] + str(rank)].get_piece() == None:
                squares[FILES[self.file + str(rank)]].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[self.file] + str(rank)])
            if squares[FILES[self.file] + str(rank)].get_piece() != None:
                squares[FILES[self.file] + str(rank)].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[self.file]])
                break
        
        for rank in range(self.rank, 0, -1):
            if squares[FILES[self.file] + str(rank)].get_piece() == None:
                squares[FILES[self.file + str(rank)]].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[self.file] + str(rank)])
            if squares[FILES[self.file] + str(rank)].get_piece() != None:
                squares[FILES[self.file] + str(rank)].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[self.file]])
                break
        
        for file in range(self.file, COLS  + 1, 1):
            if squares[FILES[file] + str(self.rank)].get_piece() == None:
                squares[FILES[self.file] + str(rank)].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[file] + str(self.rank)])
            if squares[FILES[file] + str(self.rank)].get_piece() != None:
                squares[FILES[self.file] + str(rank)].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[self.file]])
                break

        for file in range(self.file, 0, -1):
            if squares[FILES[file] + str(self.rank)].get_piece() == None:
                squares[FILES[self.file + str(rank)]].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[file] + str(self.rank)])
            if squares[FILES[file] + str(self.rank)].get_piece() != None:
                squares[FILES[self.file + str(rank)]].update_piece_reference_list(self)
                valid_moves.append(squares[FILES[file] + str(self.rank)])
                break

        return valid_moves

    def __repr__(self):
        return super().__repr__() + ' R'
    
    def attacked_squares(self, squares, rank, file):
        valid_moves = []
        # before we check if a move is valid, we also need to look does this result in a king being in check? how do i check that... 
        # check all the squares up/left/right/down
        # I have a dictionary of all my squares
        # check everything in a file
        for curr_rank in range(rank, ROWS + 1, 1):
            if squares[FILES[file] + str(curr_rank)].get_piece() == None:
                valid_moves.append(squares[FILES[file] + str(rank)])
            if squares[FILES[file] + str(rank)].get_piece() != None:
                valid_moves.append(squares[FILES[file]])
                break
        
        for curr_rank in range(rank, 0, -1):
            if squares[FILES[file] + str(curr_rank)].get_piece() == None:
                valid_moves.append(squares[FILES[file] + str(rank)])
            if squares[FILES[file] + str(curr_rank)].get_piece() != None:
                valid_moves.append(squares[FILES[file]])
                break
        
        for curr_file in range(file, COLS + 1, 1):
            if squares[FILES[curr_file] + str(rank)].get_piece() == None:
                valid_moves.append(squares[FILES[curr_file] + str(rank)])
            if squares[FILES[curr_file] + str(rank)].get_piece() != None:
                valid_moves.append(squares[FILES[curr_file]])
                break

        for curr_file in range(file, 0, -1):
            if squares[FILES[curr_file] + str(rank)].get_piece() == None:
                valid_moves.append(squares[FILES[curr_file] + str(rank)])
            if squares[FILES[curr_file] + str(rank)].get_piece() != None:
                valid_moves.append(squares[FILES[curr_file] + str(rank)])
                break

        return valid_moves