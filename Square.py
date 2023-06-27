import pygame

class Square:
    

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.occupying_piece = None
        self.x = 0
        self.y = 0

    def position(self):
        self.x = SQUARE_SIZE 

    def get_coordinates(self):
        file = 'ABCDEFGH'
        
        
        # pygame.draw.rect()
        # pygame

