from Pieces.Rook import Rook
from Pieces.Queen import Queen
from Pieces.Pawn import Pawn
from Pieces.Knight import Knight
from Pieces.King import King
from Pieces.Bishop import Bishop
from Square import Square
from ChessConstants import ROWS, COLS, BLACK, SQUARE_SIZE, WHITE, FILES

import pygame
import sys
sys.path.append('Pieces')


class Board:

    # this will represent configation of the board aka where pieces are
    # might do this on console first

    def __init__(self):

        # I will create a surface with the initialization of board
        # internal representation of board
        self.board = []
        self.list_of_squares = {}
        self.check = False
        self.config = [['R','N','B','Q','K','B','N','R'],
                       ['P','P','P','P','P','P','P','P'],
                       [' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' '],
                       ['P','P','P','P','P','P','P','P'],
                       ['R','N','B','Q','K','B','N','R']]
        self.list_of_black_pieces = []
        self.list_of_white_pieces = []
        self.setup_board()
        self.setup_pieces()

    # is there a different way to draw this checkerboard

    def setup_board(self):
        row = 0
        for rank in range(ROWS, 0, -1):
            self.board.append([])
            col = 0
            for letter in FILES:
                name = letter + str(rank)
                if row % 2 == 0 and col % 2 == 0:
                    self.list_of_squares[name] = Square(row, col, WHITE)
                    self.board[row].append(self.list_of_squares[name])
                elif row % 2 == 1 and col % 2 == 1:
                    self.list_of_squares[name] = Square(row, col, WHITE)
                    self.board[row].append(self.list_of_squares[name])
                else:
                    self.list_of_squares[name] = Square(row, col, BLACK)
                    self.board[row].append(self.list_of_squares[name])
                col += 1
            row += 1

    def list_of_squares(self):
        return self.list_of_squares

    def setup_pieces(self):
        self.board[0][0].set_occupying_piece(Rook(self.list_of_squares['A8'], BLACK))
        self.board[0][1].set_occupying_piece(Knight(self.list_of_squares['B8'], BLACK))
        self.board[0][2].set_occupying_piece(Bishop(self.list_of_squares['C8'], BLACK))
        self.board[0][3].set_occupying_piece(Queen(self.list_of_squares['D8'], BLACK))
        self.board[0][4].set_occupying_piece(King(self.list_of_squares['E8'], BLACK))
        self.board[0][5].set_occupying_piece(Bishop(self.list_of_squares['F8'], BLACK))
        self.board[0][6].set_occupying_piece(Knight(self.list_of_squares['G8'], BLACK))
        self.board[0][7].set_occupying_piece(Rook(self.list_of_squares['H8'], BLACK))

        
        for col in range(COLS):
            white_pawn_square = '{}2'.format(FILES[col])
            black_pawn_square = '{}7'.format(FILES[col])
            self.board[1][col].set_occupying_piece(Pawn(self.list_of_squares[black_pawn_square], BLACK))
            self.board[6][col].set_occupying_piece(Pawn(self.list_of_squares[white_pawn_square], WHITE))

        self.board[7][0].set_occupying_piece(Rook(self.list_of_squares['A1'], WHITE))
        self.board[7][1].set_occupying_piece(Knight(self.list_of_squares['B1'], WHITE))
        self.board[7][2].set_occupying_piece(Bishop(self.list_of_squares['C1'], WHITE))
        self.board[7][3].set_occupying_piece(Queen(self.list_of_squares['D1'], WHITE))
        self.board[7][4].set_occupying_piece(King(self.list_of_squares['E1'], WHITE))
        self.board[7][5].set_occupying_piece(Bishop(self.list_of_squares['F1'], WHITE))
        self.board[7][6].set_occupying_piece(Knight(self.list_of_squares['G1'], WHITE))     
        self.board[7][7].set_occupying_piece(Rook(self.list_of_squares['H1'], WHITE))            

    def draw(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                self.board[row][col].draw(win)

        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col].get_piece()
                if piece != None:
                    piece.draw(win)

    # temporary function
    def board_state(self):
        return self.board

    def move(self, piece, new_square):
        old_square = piece.get_square()
        new_square.set_occupying_piece(piece)
        old_square.set_occupying_piece(None)
        piece.move(new_square)
        

    def get_square(self, row, col):
        return self.board[row][col]
    
    def get_valid_moves(self, piece):
        moves = piece.valid_moves(self.list_of_squares)
        old_square = piece.get_square()
        # old_square.set_occupying_piece(None)
        # check all the piece references from this square
        # this is for check
        attacking_pieces = old_square.get_piece_reference_list()
        for chess_piece in attacking_pieces:
            possible_moves = chess_piece.valid_moves(self.list_of_squares)
            for square in possible_moves:
                if square.get_piece() is King:
                    moves.remove(square)
                    old_square.set_occupying_piece(piece)
        return moves
    
    def in_check(self):
        self.check = not self.check
        return self.check
            
   