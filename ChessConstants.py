import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

WHITE = (220, 208, 194)
BLACK = (53, 53, 53)
COLOR1 = (100, 249, 83)
COLOR2 = (0, 228, 10)


BLACK_BISHOP = pygame.transform.scale(pygame.image.load('imgs\\black bishop.png'), (45, 25))
BLACK_KING = pygame.transform.scale(pygame.image.load('imgs\\black king.png'), (45, 25))
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load('imgs\\black knight.png'), (45, 25))
BLACK_PAWN = pygame.transform.scale(pygame.image.load('imgs\\black pawn.png'), (45, 25))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load('imgs\\black queen.png'), (45, 25))
BLACK_ROOK = pygame.transform.scale(pygame.image.load('imgs\\black rook.png'), (45, 25))

WHITE_BISHOP = pygame.transform.scale(pygame.image.load('imgs\\white bishop.png'), (45, 25))
WHITE_KING = pygame.transform.scale(pygame.image.load('imgs\\white king.png'), (45, 25))
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load('imgs\\white knight.png'), (45, 25))
WHITE_PAWN = pygame.transform.scale(pygame.image.load('imgs\\white pawn.png'), (45, 25))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load('imgs\\white queen.png'), (45, 25))
WHITE_ROOK = pygame.transform.scale(pygame.image.load('imgs\\white rook.png'), (45, 25))