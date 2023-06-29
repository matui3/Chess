# plan create a square in every single spot on the board

import pygame
from ChessConstants import WHITE, BLACK, ROWS, COLS, SQUARE_SIZE

class Square:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.occupying_piece = None
        self.color = color
        self.rect = pygame.Rect(self.row * SQUARE_SIZE, self.col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

    
    def get_coord(self):
        columns = 'ABCDEFGH'
        return columns[self.x] + str(self.y + 1)
    
    def draw(self, win):
        if self.color == WHITE:
            pygame.draw.rect(win, self.color, self.rect)
        elif self.color == BLACK:
            pygame.draw.rect(win, self.color, self.rect)

   
    def get_color(self):
        return self.color
    
    def set_occupying_piece(self, piece):
        self.occupying_piece = piece

    def get_piece(self):
        return self.occupying_piece
        
                
               