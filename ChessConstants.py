import pygame
from .ChessConstants import ROWS, COLS


WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

LIGHT = (220, 208, 194)
DARK = (53, 53, 53)
COLOR1 = (100, 249, 83)
COLOR2 = (0, 228, 10)

CROWN = pygame.transform.scale(pygame.image.load('checker_module\\assets\crown.png'), (45, 25))