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
        self.white_king = None
        self.black_king = None
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
        self.create_squares_for_board()
        self.insert_squares()
        self.set_up_board()

    # is there a different way to draw this checkerboard

    def create_squares_for_board(self):
        file = 'ABCDEFGH'
        row = 0
        for rank in range(8, 0, -1):
            col = 0
            for letter in file:
                name = letter + str(rank)
                if row % 2 == 0 and col % 2 == 0:
                    self.list_of_squares[name] = Square(row, col, WHITE)
                elif row % 2 == 1 and col % 2 == 1:
                    self.list_of_squares[name] = Square(row, col, WHITE)
                else:
                    self.list_of_squares[name] = Square(row, col, BLACK)
                col += 1
            row += 1

    def list_of_squares(self):
        return self.list_of_squares

    def insert_squares(self):
        squares = list(self.list_of_squares.values())
        idx = 0
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(squares[idx])
                idx += 1

    def set_up_board(self):
        self.board[0][0].set_occupying_piece(Rook(self.list_of_squares['A8'], BLACK))
        self.board[0][1].set_occupying_piece(Knight(self.list_of_squares['B8'], BLACK))
        self.board[0][2].set_occupying_piece(Bishop(self.list_of_squares['C8'], BLACK))
        self.board[0][3].set_occupying_piece(Queen(self.list_of_squares['D8'], BLACK))
        self.board[0][4].set_occupying_piece(King(self.list_of_squares['E8'], BLACK))
        self.board[0][5].set_occupying_piece(Bishop(self.list_of_squares['F8'], BLACK))
        self.board[0][6].set_occupying_piece(Knight(self.list_of_squares['G8'], BLACK))
        self.board[0][7].set_occupying_piece(Rook(self.list_of_squares['H8'], BLACK))

        
        for col in range(COLS):
            white_pawn_square = '{}7'.format(FILES[col])
            black_pawn_square = '{}2'.format(FILES[col])
            self.board[1][col].set_occupying_piece(Pawn(self.list_of_squares[black_pawn_square], BLACK))
            self.board[6][col].set_occupying_piece(Pawn(self.list_of_squares[white_pawn_square], WHITE))

        self.board[7][0].set_occupying_piece(Rook(self.list_of_squares['A1'], WHITE))
        self.board[7][1].set_occupying_piece(Knight(self.list_of_squares['B1'], WHITE))
        self.board[7][2].set_occupying_piece(Bishop(self.list['C1'], WHITE))
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

    def move(self, piece, old_square, new_square):
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
        return False
        

    def _discovery_checks(self, list_of_pieces, king):
        for piece in list_of_pieces:
            # if piece.
            pass