import pygame
from game.constants import COLS, ROWS, TILE_SIZE

from logic import Graph

class Player(pygame.sprite.Sprite):
    """A player object for the game """   
   
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("Resources/AI.png").convert_alpha()
        self.rect = self.image.get_rect()
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
        collision_tolerence = 3
        for wall in self.walls:
            if self.rect.colliderect(wall):
                if abs(wall.left - self.rect.right) < collision_tolerence: # Moving right; Hit the left side of the wall
                    print("HIT")
  
    def update(self):
        self.input()
        self.collision()
        pygame.draw.rect(self.image,'Black', self.rect)
    
    def destroy(self):
        self.kill()
   
    def set_walls(self,walls):
        self.walls = walls    
        

      # for wall in self.walls:
        #     if abs(wall.left - self.rect.right) < collision_tolerence:
        #         print("HIT RIGHT")
        #     if abs(wall.left - self.rect.right) < collision_tolerence:
        #          print("HIT")
        #     if abs(wall.left - self.rect.left) < collision_tolerence:
        #          print("HIT")

        # def hitLeft(wall):
        #     
        
        # def hitRight(wall):
        #     


        # if self.rect.colliderect(self.walls[0][5]):
        #     wall = self.walls[0][5]
        #     hitLeft(wall)
        #     hitRight(wall)
                
        # if self.rect.colliderect(self.walls[0][12]):
        #     wall = self.walls[0][12]
        #     hitLeft(wall)
        #     hitRight(wall)
    
        # if self.rect.colliderect(self.walls[1][7]):
        #     wall = self.walls[1][7]
        #     hitLeft(wall)

       