import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_KING, WHITE_KING, WHITE

class King(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        if self.color == WHITE:
            win.blit(WHITE_KING, (self.x - WHITE_KING.get_width()//2, self.y - WHITE_KING.get_height()//2))
        else:
            win.blit(BLACK_KING, (self.x - BLACK_KING.get_width()//2, self.y - BLACK_KING.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return 'K'