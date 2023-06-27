import pygame

class Square:
    

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP' ,'bP', 'bP', 'bP', 'bP'],
            ['','','','','','','',''],
            ['','','','','','','','']
            ['','','','','','','','']
            ['','','','','','','','']
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]

    
    def get_coordinates(self):
        file = 'ABCDEFGH'
    

    def draw(self):
        rect_surf = pygame.Surface((100, 100))
        rect_surf.fill('red')
        rectangle = rect_surf.get_rect()
        
        
        # pygame.draw.rect()
        # pygame

