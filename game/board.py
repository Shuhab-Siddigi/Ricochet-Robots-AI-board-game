
import pygame
from game.constants import *
class Board(pygame.sprite.Sprite):

    # wall positions
    walls = {dict:{pygame.Rect}}

    def __init__(self):
        super().__init__()
        
        image = pygame.image.load('Resources/board.png').convert_alpha()
        self.image = pygame.transform.scale(image, BOARD_SIZE)
        # self.image = pygame.Surface((BOARD_WIDTH,BOARD_HEIGHT))              
                                              # Convert it to a pygame object
        self.rect = self.image.get_rect()
        
        x = y = 0
        for rows in range(16):
            if rows not in self.walls:
                self.walls[rows] = {}
            for col in range(16):
                rect  = pygame.Rect(x,y, TILE_SIZE[0],TILE_SIZE[0])
                if col not in self.walls:
                    self.walls[rows][col] = rect
                #walls[rows][col] = rect
                pygame.draw.rect(self.image,(220,220,220),rect,1)
                x += TILE_SIZE[0]
            y += TILE_SIZE[1]
            x = 0

        pygame.draw.rect(self.image, 'Black', pygame.Rect(0, 0, BOARD_WIDTH,BOARD_HEIGHT),  BOARD_MARGIN)
