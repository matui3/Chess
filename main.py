# Class represents the state of the game, keeps track of turns as well as which player
from Board import Board
from Game import Game
from Pieces.King import King
from Pieces.Rook import Rook
from Pieces.Queen import Queen
from Pieces.Pawn import Pawn
from Pieces.Knight import Knight
from Pieces.King import King
from Pieces.Bishop import Bishop
from Square import Square


import pygame
from ChessConstants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, BLACK


FPS = 60
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col



def main():
    running = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col) # i dont do anything with the returned piece/square
                         
        game.update()
        clock.tick(FPS)
        

if __name__ == "__main__":
    # print(King is King)
    main()
    