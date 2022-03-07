
import pygame
from game.constants import *
class Board(pygame.sprite.Sprite):

    # wall positions
    walls = []

    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((16*TILE_SIZE, 16*TILE_SIZE))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.grid = []
        
        # GRID    
        for x in range(16):
            self.grid.append([x])
            for y in range(16):
                self.grid[x].append([y])
                rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.image, (120, 120, 120), rect, 1)
                self.grid[x][y] = rect.center
                # if y not in self.grid[x]:
                #     self.grid[x][y] = rect.center 

        middle_square = pygame.Rect(7*TILE_SIZE, 7*TILE_SIZE, TILE_SIZE*2, TILE_SIZE*2)
        pygame.draw.rect(self.image,'White', middle_square)
        pygame.draw.rect(self.image,'Black', middle_square,5)
        
 

    # Rect around the board
        pygame.draw.rect(self.image, (0, 0, 0), self.rect, 5)

