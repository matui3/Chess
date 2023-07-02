import pygame
from Board import Board
from ChessConstants import WHITE, BLACK, COLOR1, SQUARE_SIZE, COLOR2

class Game:
    def __init__(self, win):
        self.win = win
        self._init()

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = []

    def reset(self):
        self._init()

    def select(self, row, col): 
        # grab piece from squaree and CALL self.select AGAIN
        # if this in valid moves, MOVE the piece
        # turn needs to END and repeat.
        
        # selected piece
        if self.selected:
            result = self._move(row, col)
            self.valid_moves = []
            
            if not result:
                self.selected = None
                self.select(row, col)
       
        piece = self.board.get_square(row, col).get_piece()
        if piece != None and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)    
            return piece        
        return None
            
        
            


    def _move(self, row, col):
        square = self.board.get_square(row, col)
        if self.selected and square.get_piece() == None and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        elif self.selected and square.get_piece() != None and (row, col) in self.valid_moves and self.selected.color != square.get_piece().color:
            self.board.move(self.selected, row, col)
            self.change_turn()
        return square
        
        
    
    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def draw_valid_moves(self, moves):
        positions = self.board.board_state()
        
        for move in moves:
            row, col = move
            if positions[row][col].get_piece() == None:
                pygame.draw.circle(self.win, COLOR2, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
