# Class represents the state of the game, keeps track of turns as well as which player


import pygame
import numpy as np

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Chess')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

