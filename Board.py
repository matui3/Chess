import pygame
import sys
sys.path.append('Pieces')

from ChessConstants import ROWS, COLS, BLACK, SQUARE_SIZE, WHITE
from Square import Square
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook


class Board:

    # this will represent configation of the board aka where pieces are
    # might do this on console first

    def __init__(self):
        
        # I will create a surface with the initialization of board
        # internal representation of board
        self.config = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                      ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                      ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        
        self.board = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                      ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                      ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        
    def create_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                # insert algorithm to add pieces or squares
                pass


    # is there a different way to draw this checkerboard
    def draw_squares(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                if row % 2 == 0 and col % 2 == 0:
                    if row == 0:
                        if self.board[row][col] == 'bR':
                            print(True)
                            self.board[row][col] = Square(row, col, WHITE)
                            self.board[row][col]._set_occupying_piece(Rook(row, col, BLACK))
                            self.board[row][col].draw(win)
                        if self.board[row][col] == 'bN':
                            self.board[row][col] = Square(row, col, WHITE)
                            self.board[row][col]._set_occupying_piece(Knight(row, col, BLACK))
                            self.board[row][col].draw(win)
                        if self.board[row][col] == 'bB':
                            self.board[row][col] = Square(row, col, WHITE)
                            self.board[row][col]._set_occupying_piece(Bishop(row, col, BLACK))
                            self.board[row][col].draw(win)
                        if self.board[row][col] == 'bQ':
                            self.board[row][col] = Square(row, col, WHITE)
                            self.board[row][col]._set_occupying_piece(Queen(row, col, BLACK))
                            self.board[row][col].draw(win)
                        if self.board[row][col] == 'bK':
                            self.board[row][col] = Square(row, col, WHITE)
                            self.board[row][col]._set_occupying_piece(King(row, col, BLACK))
                            self.board[row][col].draw(win)
                        else:
                            self.board[row][col] = Square(row, col, WHITE)
                            self.board[row][col].draw(win)
                elif row % 2 == 1 and col % 2 == 1:
                    self.board[row][col] = Square(row, col, WHITE)
                    self.board[row][col].draw(win)
                else:
                    self.board[row][col] = Square(row, col, BLACK)
                    self.board[row][col].draw(win)
                    

    def draw(self, win):
        self.draw_squares(win)
        # for row in range(ROWS):
        #     for col in range(COLS):
        #         piece = self.board[row][col]
        #         if piece != 0:
        #             piece.draw(win)

    def get_square(self, row, col):
        return self.board[row][col]