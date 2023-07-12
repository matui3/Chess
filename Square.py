# plan create a square in every single spot on the board

import pygame
from ChessConstants import WHITE, BLACK, SQUARE_SIZE, FILES

class Square:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self._occupying_piece = None
        self.color = color
        self.rect = pygame.Rect(self.row * SQUARE_SIZE, self.col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        self.name = self.set_square_name(row, col)
        self.file = FILES[col]
        self.rank = row + 1;
        self.piece_ref_list = []

    def set_square_name(self, row, col):
        return FILES[col] + str(row + 1)
    
    def get_file_idx(self):
        return self.col        

    def get_rank(self):
        return self.rank
    
    def draw(self, win):
        if self.color == WHITE:
            pygame.draw.rect(win, self.color, self.rect)
        elif self.color == BLACK:
            pygame.draw.rect(win, self.color, self.rect)

    def get_piece_ref_list(self):
        return self.piece_ref_list

    def get_color(self):
        return self.color
    
    def set_occupying_piece(self, piece):
        self._occupying_piece = piece

    def get_piece(self):
        return self._occupying_piece
    
    def get_row_col(self):
        return (self.row, self.col)
        
                
               