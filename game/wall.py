
import pygame
from game.constants import *
class VerticalWall(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        
        self.image = pygame.Surface((5, TILE_SIZE))
        self.rect = pygame.Rect(x*TILE_SIZE-2.5, y*TILE_SIZE, 5, TILE_SIZE)
        pygame.draw.rect(self.image,'Black', self.rect)
 
class HorizontalWall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, 5))
        self.rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE-2.5, TILE_SIZE, 5)
        pygame.draw.rect(self.image,'Black', self.rect)

class WallGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        
        # # WALL START TOP LEFT CORNER -> 
        self.add(VerticalWall(5,0))
        self.add(VerticalWall(13,0))
        self.add(HorizontalWall(14,1))
        self.add(VerticalWall(14,1))
        self.add(VerticalWall(7,1))
        self.add(HorizontalWall(6,2))
        self.add(HorizontalWall(1,2))
        self.add(VerticalWall(1,2))
        self.add(VerticalWall(10,2))
        self.add(HorizontalWall(9,3))
        self.add(HorizontalWall(15,4))
        self.add(HorizontalWall(6,5))
        self.add(VerticalWall(7,5))
        self.add(VerticalWall(14,5))
        self.add(HorizontalWall(0,6))  
        self.add(HorizontalWall(11,6))     
        self.add(HorizontalWall(14,6))
        self.add(VerticalWall(3,6))
        self.add(VerticalWall(12,6))
        self.add(HorizontalWall(3,7))
        self.add(HorizontalWall(5,8))
        self.add(VerticalWall(6,8))
        self.add(VerticalWall(2,9))
        self.add(HorizontalWall(1,10))
        self.add(HorizontalWall(15,10))
        self.add(VerticalWall(4,10))
        self.add(VerticalWall(9,10))
        self.add(HorizontalWall(4,11))
        self.add(HorizontalWall(8,11))
        self.add(HorizontalWall(13,11))
        self.add(VerticalWall(13,11))
        self.add(HorizontalWall(0,12))
        self.add(HorizontalWall(5,13))
        self.add(VerticalWall(6,13))
        self.add(VerticalWall(9,13))
        self.add(HorizontalWall(3,14))
        self.add(HorizontalWall(9,14))
        self.add(HorizontalWall(14,14))
        self.add(VerticalWall(3,14))
        self.add(VerticalWall(15,14))
        self.add(VerticalWall(7,15))
        self.add(VerticalWall(12,15))
