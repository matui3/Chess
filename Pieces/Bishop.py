import pygame
import sys
sys.path.append('..')

from Piece import Piece
from ChessConstants import BLACK_BISHOP, WHITE_BISHOP, WHITE, BLACK

class Bishop(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_BISHOP, BLACK_BISHOP)

    def move(self, row, col):
        super().move(row, col)


    def valid_move(self):
        return super().valid_move()

    def __repr__(self):
        return super().__repr__() + 'B'