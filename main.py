# Class represents the state of the game, keeps track of turns as well as which player
from Board import Board

import pygame
from ChessConstants import WIDTH, HEIGHT, SQUARE_SIZE


FPS = 60
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


board = Board()


def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                square = board.get_square(row, col)
                print(square.get_piece())                
            
        
        board.draw(WIN)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    # board.draw(WIN)
    main()