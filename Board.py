import numpy as np

class Board:

    # this will represent configation of the board aka where pieces are
    # might do this on console first

    def __init__(self):
        self.board = np.array([[' ' for col in range(8)] for row in range(8)])

    def display_board(self):
        print(self.board)