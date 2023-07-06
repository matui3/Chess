import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

WHITE = (220, 208, 194)
BLACK = (53, 53, 53)
COLOR1 = (100, 249, 83)
COLOR2 = (0, 228, 10)


FILES = 'ABCDEFGH'

BLACK_BISHOP = pygame.transform.scale(pygame.image.load('imgs\\Black Bishop.png'), (80, 80))
BLACK_KING = pygame.transform.scale(pygame.image.load('imgs\\Black King.png'), (80, 80))
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load('imgs\\Black Knight.png'), (80, 80))
BLACK_PAWN = pygame.transform.scale(pygame.image.load('imgs\\Black Pawn.png'), (80, 80))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load('imgs\\Black Queen.png'), (80, 80))
BLACK_ROOK = pygame.transform.scale(pygame.image.load('imgs\\Black Rook.png'), (80, 80))

WHITE_BISHOP = pygame.transform.scale(pygame.image.load('imgs\\White Bishop.png'), (80, 80))
WHITE_KING = pygame.transform.scale(pygame.image.load('imgs\\White King.png'), (80, 80))
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load('imgs\\White Knight.png'), (80, 80))
WHITE_PAWN = pygame.transform.scale(pygame.image.load('imgs\\White Pawn.png'), (80, 80))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load('imgs\\White Queen.png'), (80, 80))
WHITE_ROOK = pygame.transform.scale(pygame.image.load('imgs\\White Rook.png'), (80, 80))