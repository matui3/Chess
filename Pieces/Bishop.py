import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_BISHOP, WHITE_BISHOP, WHITE, BLACK

class Bishop(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.x = 0
        self.y = 0

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        if self.color == WHITE:
            win.blit(WHITE_BISHOP, (self.x - WHITE_BISHOP.get_width()//2, self.y - WHITE_BISHOP.get_height()//2))
        else:
            win.blit(BLACK_BISHOP, (self.x - BLACK_BISHOP.get_width()//2, self.y - BLACK_BISHOP.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)