
import pygame
from game.constants import *
class Wall(pygame.sprite.Sprite):

    def __init__(self,start_x,start_y,end_x,end_y):
        super().__init__()
        
        self.image = pygame.Surface((16*TILE_SIZE, 16*TILE_SIZE))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        
        # GRID    
        for x in range(16):
            for y in range(16):
                rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.image, (128, 128, 128), rect, 1)
    
    #   pygame.draw.line(surface, RGB, FROM (x,y), TO (x,y), thickness)
        # LEFT LINE
        pygame.draw.line(self.image, (0, 0, 0), (7*TILE_SIZE, 7*TILE_SIZE), (7*TILE_SIZE, 9*TILE_SIZE), 5)
        # BOTTOM LINE
        pygame.draw.line(self.image, (0, 0, 0), (7*TILE_SIZE, 9*TILE_SIZE), (9*TILE_SIZE, 9*TILE_SIZE), 5)
        # RIGHT LINE
        pygame.draw.line(self.image, (0, 0, 0), (9*TILE_SIZE, 9*TILE_SIZE), (9*TILE_SIZE, 7*TILE_SIZE), 5)
        # TOP LINE
        pygame.draw.line(self.image, (0, 0, 0), (7*TILE_SIZE, 7*TILE_SIZE), (9*TILE_SIZE, 7*TILE_SIZE), 5)

    # WALL START TOP LEFT CORNER -> 
        # 5,0
        pygame.draw.line(self.image, (0, 0, 0), (5*TILE_SIZE, 0*TILE_SIZE), (5*TILE_SIZE, 1*TILE_SIZE), 5)
        # 12,0
        pygame.draw.line(self.image, (0, 0, 0), (12*TILE_SIZE, 0*TILE_SIZE), (12*TILE_SIZE, 1*TILE_SIZE), 5)

    # Rect around the board
        pygame.draw.rect(self.image, (0, 0, 0), self.rect, 5)