import Square
from ChessConstants import ROWS, COLS, DARK, SQUARE_SIZE, LIGHT
import pygame

class Board:

    # this will represent configation of the board aka where pieces are
    # might do this on console first

    def __init__(self):
        self.board = []
        # I will create a surface with the initialization of board


    def draw_squares(self, win):
        win.fill(DARK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, LIGHT, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    def display_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(Square(SQUARE_SIZE, SQUARE_SIZE))

    def draw(self, win):
        self.draw_squares(win)