
import pygame
import sys
sys.path.append('..')


from Piece import Piece
from ChessConstants import WHITE_PAWN, BLACK_PAWN, WHITE

class Pawn(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def calc_pos(self):
        super().calc_pos()
        

    def draw(self, win):
        super().draw(win, WHITE_PAWN, BLACK_PAWN)

    def move(self, row, col):
        super().move(row, col)

    def __repr__(self):
        return super().__repr__() + 'P'