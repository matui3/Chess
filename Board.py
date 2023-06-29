from Pieces.Rook import Rook
from Pieces.Queen import Queen
from Pieces.Pawn import Pawn
from Pieces.Knight import Knight
from Pieces.King import King
from Pieces.Bishop import Bishop
from Square import Square
from ChessConstants import ROWS, COLS, BLACK, SQUARE_SIZE, WHITE
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
        self.config = [['R','N','B','Q','K','B','N','R'],
                       ['P','P','P','P','P','P','P','P'],
                       [' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' '],
                       ['P','P','P','P','P','P','P','P'],
                       ['R','N','B','Q','K','B','N','R']]
        
        

    def create_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                # insert algorithm to add pieces or squares
                pass

    # is there a different way to draw this checkerboard
    def draw_squares(self, win):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row % 2 == 0 and col % 2 == 0:
                    self.board[row].append(Square(row, col, WHITE))
                    self.board[row][col].draw(win)
                elif row % 2 == 1 and col % 2 == 1:
                    self.board[row].append(Square(row, col, WHITE))
                    self.board[row][col].draw(win)
                else:
                    self.board[row].append(Square(row, col, BLACK))
                    self.board[row][col].draw(win)

    def set_up_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0:
                    if self.config[row][col] == 'R':
                        self.board[row][col].set_occupying_piece(Rook(row, col, BLACK))
                    if self.config[row][col] == 'N':
                        self.board[row][col].set_occupying_piece(Knight(row, col, BLACK))
                    if self.config[row][col] == 'B':
                        self.board[row][col].set_occupying_piece(Bishop(row, col, BLACK))
                    if self.config[row][col] == 'Q':
                        self.board[row][col].set_occupying_piece(Queen(row, col, BLACK))
                    if self.config[row][col] == 'K':
                        self.board[row][col].set_occupying_piece(King(row, col, BLACK))
                
                if row == 1:
                    self.board[row][col].set_occupying_piece(Pawn(row, col, BLACK))
                
                if row == 6:
                    self.board[row][col].set_occupying_piece(Pawn(row, col, WHITE))
                
                if row == 7:
                    if self.config[row][col] == 'R':
                        self.board[row][col].set_occupying_piece(Rook(row, col, WHITE))
                    if self.config[row][col] == 'N':
                        self.board[row][col].set_occupying_piece(Knight(row, col, WHITE))
                    if self.config[row][col] == 'B':
                        self.board[row][col].set_occupying_piece(Bishop(row, col, WHITE))
                    if self.config[row][col] == 'Q':
                        self.board[row][col].set_occupying_piece(Queen(row, col, WHITE))
                    if self.config[row][col] == 'K':
                        self.board[row][col].set_occupying_piece(King(row, col, WHITE))

    def draw(self, win):
        self.draw_squares(win)
        self.set_up_board()
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col].get_piece()
                if piece != None:
                    piece.draw(win)

                    

    def get_square(self, row, col):
        return self.board[row][col]
