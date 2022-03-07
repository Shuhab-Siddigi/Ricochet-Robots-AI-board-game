
import pygame
from game.constants import *
class Board(pygame.sprite.Sprite):

    # wall positions
    walls = {dict:{pygame.Rect}}

    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((16*TILE_SIZE, 16*TILE_SIZE))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        
        # GRID    
        for x in range(16):
            for y in range(16):
                rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.image, (120, 120, 120), rect, 1)

        middle_square = pygame.Rect(7*TILE_SIZE, 7*TILE_SIZE, TILE_SIZE*2, TILE_SIZE*2)
        pygame.draw.rect(self.image,'White', middle_square)
        pygame.draw.rect(self.image,'Black', middle_square,5)
        
        def drawHorizontalRect(x,y):
            rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE-2.5, TILE_SIZE, 5)
            pygame.draw.rect(self.image,'Black', rect)
        
        def drawVerticalRect(x,y):
            rect = pygame.Rect(x*TILE_SIZE-2.5, y*TILE_SIZE, 5, TILE_SIZE)
            pygame.draw.rect(self.image,'Black', rect)
        # # Draw Middle square
        # # LEFT LINE
        
        # drawLine(7,7,7,9)
        # # BOTTOM LINE
        # drawLine(7,9,9,9)
        # # RIGHT LINE
        # drawLine(9,9,9,7)
        # # TOP LINE
        # drawLine(7,7,9,7)

        
        # # WALL START TOP LEFT CORNER -> 
        drawVerticalRect(5,0)
        drawVerticalRect(13,0)

        drawHorizontalRect(14,1)
        drawVerticalRect(14,1)
        drawVerticalRect(7,1)
        
        drawHorizontalRect(6,2)
        drawHorizontalRect(1,2)
        drawVerticalRect(1,2)
        drawVerticalRect(10,2)
        
        drawHorizontalRect(9,3)

        drawHorizontalRect(15,4)

        drawHorizontalRect(6,5)
        drawVerticalRect(7,5)
        drawVerticalRect(14,5)



        drawHorizontalRect(0,6)  
        drawHorizontalRect(11,6)     
        drawHorizontalRect(14,6)
        drawVerticalRect(3,6)
        drawVerticalRect(12,6)

        drawHorizontalRect(3,7)
        
        drawHorizontalRect(5,8)
        drawVerticalRect(6,8)

        drawVerticalRect(2,9)
        drawHorizontalRect(1,10)
        drawHorizontalRect(15,10)

        drawVerticalRect(4,10)
        drawVerticalRect(9,10)

        drawHorizontalRect(4,11)
        drawHorizontalRect(8,11)

        drawHorizontalRect(13,11)
        drawVerticalRect(13,11)

        drawHorizontalRect(0,12)

        drawHorizontalRect(5,13)
        drawVerticalRect(6,13)
        drawVerticalRect(9,13)
        
        drawHorizontalRect(3,14)
        drawHorizontalRect(9,14)
        drawHorizontalRect(14,14)

        drawVerticalRect(3,14)
        drawVerticalRect(15,14)

        drawVerticalRect(7,15)
        drawVerticalRect(12,15)


    # Rect around the board
        pygame.draw.rect(self.image, (0, 0, 0), self.rect, 5)

