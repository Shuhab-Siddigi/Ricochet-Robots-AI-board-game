import pygame
from game.constants import COLS, MARGIN, ROWS, SCREEN_SIZE, TILE_SIZE

from logic import Graph

class Player(pygame.sprite.Sprite):
    """A player object for the game """   
    
    def addImage(self,image,imagelist,index,y):
            surface = pygame.Surface((TILE_SIZE-MARGIN,TILE_SIZE-MARGIN))
            surface.fill('White')
            imagelist.append(surface)
            imagelist[index].blit(image,(0,0),(index*50,y*50,50,50))

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
                self.image= self.walkup[0]
        if move == "LEFT":
            if self.X > 0:
                self.X -= 1
                self.rect.center = self.grid[self.X][self.Y]
                self.image= self.walkleft[0]
        if move == "DOWN":
            if self.Y < ROWS-1:
                self.Y += 1
                self.rect.center = self.grid[self.X][self.Y]
                
                self.image= self.walkdown[0]
        if move == "RIGHT":
            if self.X < COLS-1:
                self.X += 1
                self.rect.center = self.grid[self.X][self.Y]
                self.image= self.walkright[0]

    def addGrid(self,grid):
        self.grid = grid

    def collision(self):
        collision_tolerence = 5
        for wall in self.walls:
            if self.rect.colliderect(wall): 
                if abs(wall.left - self.rect.right) < collision_tolerence: # Moving right; Hit the left side of the wall
                    print("HIT RIGHT")
                if abs(self.rect.left - wall.right) < collision_tolerence:
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
        
    
    def __init__(self):
        super().__init__()
        
        # Load spritesheet
        image = pygame.image.load("Resources/playersheet.jpg").convert_alpha()
        # Move animation lists
        self.walkleft = []
        self.walkright = []
        self.walkdown = []
        self.walkup = []
        
        for index in range(9):
            self.addImage(image,self.walkdown,index,0)
            self.addImage(image,self.walkleft,index,1)
            self.addImage(image,self.walkright,index,2)
            self.addImage(image,self.walkup,index,3)
        
       
        self.image = pygame.Surface((TILE_SIZE-MARGIN,TILE_SIZE-MARGIN)) # screen surface
        #self.image = pygame.Surface(SCREEN_SIZE) # screen surface
        #self.image.set_alpha(0)
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()

        #image = pygame.image.load("Resources/AI.png").convert_alpha()
        
        #image = pygame.transform.scale(image, self.image.get_size())
        self.image.blit(image,(0,0),(50,50,50,50))
        print(self.image.get_size())
        self.grid = [[]]
        self.X = 0
        self.Y = 0
    
    

 