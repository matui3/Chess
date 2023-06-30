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


chessboard = Board()


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
                square = chessboard.get_square(row, col)
                moved_piece = square.get_piece()
                moved_piece.valid_moves(chessboard)
        
                # finish this later for moving pieces
                

                         
        chessboard.draw(WIN)
        pygame.display.update()
        clock.tick(FPS)
        

if __name__ == "__main__":
    main()
    