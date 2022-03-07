import pygame
from game.constants import COLS, MARGIN, ROWS, TILE_SIZE

from logic import Graph

class Player(pygame.sprite.Sprite):
    """A player object for the game """   
   
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((TILE_SIZE-MARGIN,TILE_SIZE-MARGIN)) # screen surface
        #self.image.set_alpha(0)
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()

        image = pygame.image.load("Resources/AI.png").convert_alpha()
        image = pygame.transform.scale(image, self.image.get_size())
        self.image.blit(image,(0,0))
        print(self.image.get_size())
        self.grid = [[]]
        self.X = 0
        self.Y = 0
        

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.actions("LEFT")
        if key[pygame.K_RIGHT]:
            self.actions("RIGHT")
        if key[pygame.K_UP]:
            self.actions("UP")
        if key[pygame.K_DOWN]:
            self.actions("DOWN")

    def actions(self,move:str):
        if move == "UP":
            if self.Y > 0:
                self.Y -= 1
                self.rect.center = self.grid[self.X][self.Y]
        if move == "LEFT":
            if self.X > 0:
                self.X -= 1
                self.rect.center = self.grid[self.X][self.Y]
        if move == "DOWN":
            if self.Y < ROWS-1:
                self.Y += 1
                self.rect.center = self.grid[self.X][self.Y]
        if move == "RIGHT":
            if self.X < COLS-1:
                self.X += 1
                self.rect.center = self.grid[self.X][self.Y]

    def addGrid(self,grid):
        self.grid = grid

    def collision(self):
        collision_tolerence = 5
        for wall in self.walls:
            if self.rect.colliderect(wall): 
                if abs(wall.left - self.rect.right) < collision_tolerence: # Moving right; Hit the left side of the wall
                    print("HIT RIGHT")
                if abs(wall.right - self.rect.left) < collision_tolerence:
                    print("HIT LEFT")
                if abs(wall.top - self.rect.bottom) < collision_tolerence:
                    print("HIT BOTTOM")
                if abs(wall.bottom - self.rect.top) < collision_tolerence:
                    print("HIT TOP")

    def update(self):
        self.input()
        self.collision()
        #pygame.draw.rect(self.image,'Black', self.rect, 2)
    
    def destroy(self):
        self.kill()
   
    def set_walls(self,walls):
        self.walls = walls    
        