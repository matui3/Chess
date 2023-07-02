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
        self.insert_squares()
        self.set_up_board()
        self.check = False
        self.white_king = None
        self.black_king = None
        

    # is there a different way to draw this checkerboard
    def insert_squares(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row % 2 == 0 and col % 2 == 0:
                    self.board[row].append(Square(row, col, WHITE))
                elif row % 2 == 1 and col % 2 == 1:
                    self.board[row].append(Square(row, col, WHITE))
                else:
                    self.board[row].append(Square(row, col, BLACK))

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
                        self.black_king = King(row, col, BLACK)
                        self.board[row][col].set_occupying_piece(self.black_king)
                
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
                        self.white_king = King(row, col, WHITE)
                        self.board[row][col].set_occupying_piece(self.white_king)

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

    def move(self, piece, row, col):
        moved_piece = self.board[piece.row][piece.col].get_piece()
        self.board[piece.row][piece.col].set_occupying_piece(None)
        self.board[row][col].set_occupying_piece(moved_piece)
        moved_piece.move(row, col)

    def get_square(self, row, col):
        return self.board[row][col]
    
    def get_valid_moves(self, piece):
        moves = piece.valid_moves(self)
        return moves
    
    def in_check(self):
        white_king_pos = self.white_king.king_position()
        black_king_pos = self.black_king.king_position()
        if self.selected:
            danger_spots = self.selected.attacking_moves()
            self._no_pieces_to_check(white_king_pos, WHITE, self.white_king, danger_spots)
            self._no_pieces_to_check(black_king_pos, BLACK, self.black_king, danger_spots)

            # need to add more to this

            
    def _no_piece_obstacles_check(self, king_pos, color, king, attacking_moves):       
        if self.turn == color:
            for row, col in enumerate(attacking_moves):
                piece = self.board[row][col].get_piece()
                if piece == None:
                    if king_pos in attacking_moves and king.color != self.selected.color:
                        self.check = king.change_check_status()


    def _absolute_pin_for_valid_moves(self, attacking_moves, king_pos):
        for row, col in enumerate(attacking_moves):
            piece = self.board[row][col].get_piece()
            if piece != None and type(piece) != type(self.black_king) and king_pos in attacking_moves:
                return True 
        

    def _discovery_checks(self, piece_prev_pos, attacking_moves):
