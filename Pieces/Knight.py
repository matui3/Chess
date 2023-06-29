import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_KNIGHT, WHITE_KNIGHT, WHITE

class Knight(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        if self.color == WHITE:
            win.blit(WHITE_KNIGHT, (self.x - WHITE_KNIGHT.get_width()//2, self.y - WHITE_KNIGHT.get_height()//2))
        else:
            win.blit(BLACK_KNIGHT, (self.x - BLACK_KNIGHT.get_width()//2, self.y - BLACK_KNIGHT.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)