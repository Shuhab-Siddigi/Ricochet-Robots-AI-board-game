import pygame
from game.constants import MARGIN, TILE_SIZE

class Player(pygame.sprite.Sprite):
    """A player object for the game """
    def __init__(self):
        super().__init__()
       
        self.image = pygame.Surface((TILE_SIZE-MARGIN,TILE_SIZE-MARGIN)) # screen surface
        #self.image = pygame.Surface(SCREEN_SIZE) # screen surface
        #self.image.set_alpha(0)
        self.image.fill('White')
        self.rect =  pygame.Rect(0, TILE_SIZE*15, TILE_SIZE, TILE_SIZE)
        # animation
        # Load spritesheet
        image = pygame.image.load("Resources/playersheet.jpg").convert_alpha()
        
        self.actions = ["UP","DOWN","LEFT","RIGHT"]
        self.move = "LEFT"
        self.isCollision = False
        self.collisionObjects = []
        # Move animation lists
        self.animations = []
        for x in range(9):
            for y in range(4):
                self.animations.append([x])
                self.animations[x].append([y])
                surface = pygame.Surface((TILE_SIZE-MARGIN,TILE_SIZE-MARGIN))
                surface.fill('White')
                self.animations[x][y] = surface
                self.animations[x][y].blit(image,(0,0),(x*50,y*50,50,50))
        
        self.walkleft_frame = 0
        self.walkright_frame = 0
        self.walkdown_frame = 0
        
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 500
        
        self.image.blit(image,(0,0),(50,50,50,50))
        print(self.image.get_size())
        self.grid = [[]]
        self.X = 0
        self.Y = 0
    
    
    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.Y -= 1
            self.rect.center = self.grid[self.X][self.Y]
            self.image= self.animations[0][0]
        if key[pygame.K_DOWN]:
            self.Y += 1
            self.rect.center = self.grid[self.X][self.Y]
            self.image= self.animations[0][0]
        if key[pygame.K_LEFT]:
            self.X -= 1
            self.rect.center = self.grid[self.X][self.Y]
            self.image= self.animations[0][0]
        if key[pygame.K_RIGHT]:
            self.X += 1
            self.rect.center = self.grid[self.X][self.Y]
            self.image= self.animations[0][0]


    def addGrid(self,grid):
        self.grid = grid



    def update(self):
        self.input()
        #self.collision()
        pygame.draw.rect(self.image,'Black', self.rect, 5)
    
    def destroy(self):
        self.kill()
   
    def set_walls(self,walls):
        self.walls = walls    
        
    


    #  def collision(self):
    #     collision_tolerence = 0
    #     # if self.isCollision:
    #     #     print("HIT")
        
    #     # for wall in self.walls:
    #     #     if self.rect.colliderect(wall): 
    #     #         if abs(wall.left - self.rect.right) < collision_tolerence: # Moving right; Hit the left side of the wall
    #     #             print("HIT RIGHT")
    #     #         if abs(self.rect.left - wall.right) < collision_tolerence:
    #     #             print("HIT LEFT")
    #     #         if abs(wall.top - self.rect.bottom) < collision_tolerence:
    #     #             print("HIT BOTTOM")
    #     #         if abs(wall.bottom - self.rect.top) < collision_tolerence:
    #     #             print("HIT TOP")
    #     #     if self.isCollision():
    #     #         print("Hit")
