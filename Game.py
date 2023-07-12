import pygame
from Board import Board
from ChessConstants import WHITE, BLACK, COLOR1, SQUARE_SIZE, COLOR2

class Game:
    def __init__(self, win):
        self.win = win
        self._init()

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_squares)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_squares = []

    def reset(self):
        self._init()

    def select(self, row, col): 
        # grab piece from squaree and CALL self.select AGAIN
        # if this in valid moves, MOVE the piece
        # turn needs to END and repeat.
        # selected piece
        
        selected_square = self.board.get_square(row, col) # this is a square
        print(selected_square.name)
        if self.selected != None: # self.selected will be none initially
            # T
            result = self._move(selected_square) # this is the return value of the move method, this is a boolean
            self.valid_squares = []
            
            if not result: # if the movement fails and isn't valid then reset everything and yeah.
                self.selected = None
                self.select(row, col)
       
        piece = selected_square.get_piece() # grab piece from selected square
        if piece != None and piece.color == self.turn: # if there is a piece otherwise and it's your turn
            self.selected = piece # the selected item is the piece
            self.valid_squares = self.board.get_valid_moves(self.selected) # grab all valid moves of that piece  
            return self.selected
        return selected_square # returns the selected square if no piece

    def _move(self, selected_square): # will probably need to change this
        
        if self.selected and selected_square in self.valid_squares: # issues with this if statement
            result = self.board.move(self.selected, selected_square)
            if result: # this will be a boolean
                self.change_turn()
                return True
        elif self.selected and selected_square.get_piece() != None and selected_square in self.valid_squares and self.selected.color != selected_square.get_piece().color:
            result = self.board.move(self.selected, selected_square)
            if result:
                self.change_turn()
                return True
        return False
        
        
    
    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def draw_valid_moves(self, moves):
        # positions = self.board.board_state()
        
        for square in moves:
            if (square.get_piece() == None):
                 pygame.draw.circle(self.win, COLOR2, (square.col * SQUARE_SIZE + SQUARE_SIZE//2, square.row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
