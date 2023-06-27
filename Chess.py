# Class represents the state of the game, keeps track of turns as well as which player
import Square as Square

import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

fps = 60

running = True
test_surface = pygame.Surface((100, 100))
test_surface.fill('Red')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (0, 0))
    pygame.display.update()
    clock.tick(60)

    square = Square()
    square.draw()


