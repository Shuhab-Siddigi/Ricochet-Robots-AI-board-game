import pygame
from game.constants import BOARD_HEIGHT, BOARD_WIDTH, COLS, MARGIN, ROWS, TILE_SIZE

class Player(pygame.sprite.Sprite):
    """A player object for the game """
    def __init__(self,pos_x:int,pos_y:int,color:int):
        super().__init__()

        # Load player spredsheet
        spreedsheet = pygame.image.load("Resources/playersheet.jpg").convert_alpha()
        spreedsheet.set_colorkey((255,255,255))
        
        # Create a grid of posible positions
        self.positions = []
        for x in range(ROWS):
            self.positions.append([x])
            for y in range(COLS):
                self.positions[x].append([y])
                self.positions[x][y] = pygame.Rect(x*TILE_SIZE+MARGIN, y*TILE_SIZE+MARGIN, TILE_SIZE, TILE_SIZE)
        
        # Move animation lists
        self.animations = []
        for x in range(9):
            self.animations.append([x])
            for y in range(4):
                self.animations[x].append([y])
                surface = pygame.Surface((TILE_SIZE-MARGIN,TILE_SIZE-MARGIN))
                surface.fill('White')
                self.animations[x][y] = surface
                self.animations[x][y].blit(spreedsheet,(0,0),(x*48,y*48,50,50))
        
        self.frame = 3*color
        self.action = 0
        # Set first animation frame
        self.image = self.animations[self.frame][self.action]
        
        # Create collision rectangle
        self.X = pos_x
        self.Y = pos_y
        self.rect = self.image.get_rect()
        self.rect.center = self.positions[self.X][self.Y].center
        self.collision_group = []
        #              idle,up  ,down,left,right
        self.states = [bool,bool,bool,bool,bool]
        self.states[0] = True
        #              up  ,down,left,right 
        self.hitbox = [bool,bool,bool,bool]

        
    #     self.last_update = pygame.time.get_ticks()
    #     self.animation_cooldown = 500
        
    def input(self):
        key = pygame.key.get_pressed()
        if self.states[0]:
            if key[pygame.K_UP]:
                self.states[0] = False
                self.states[1] = True
                #self.image = self.animations[self.frame][self.action]
            if key[pygame.K_DOWN]:
                self.states[0] = False
                self.states[2]= True
                #self.image = self.animations[self.frame][self.action]
            if key[pygame.K_LEFT]:
                self.states[0] = False
                self.states[3] = True
                #self.image = self.animations[self.frame][self.action]
            if key[pygame.K_RIGHT]:
                self.states[0] = False
                self.states[4] = True
                #self.image = self.animations[self.frame][self.action]
    
    def collision(self,sprite_group:pygame.sprite.Group):
        
        collision_tolerence = MARGIN
        
        for sprite in sprite_group:
          if self.rect.colliderect(sprite):
            if abs(sprite.rect.bottom - self.rect.top) < collision_tolerence:
                print("HIT TOP")
                self.hitbox[0] = True
            if abs(sprite.rect.top - self.rect.bottom) < collision_tolerence:
                print("HIT BOTTOM")
                self.hitbox[1] = True
            if abs(sprite.rect.right - self.rect.left) < collision_tolerence:
                print("HIT LEFT")
                self.hitbox[2] = True
            if abs(sprite.rect.left - self.rect.right) < collision_tolerence:
                print("HIT RIGHT")
                self.hitbox[3] = True

    # applicable moves
    def movement(self):
        # Check for board bounds
        if self.states[1] and self.Y > 0 and not self.hitbox[0]:
            self.Y -= 1
        elif self.states[2] and self.Y < COLS-1 and not self.hitbox[1]:
            self.Y += 1
        elif self.states[3] and self.X > 0 and not self.hitbox[2]:
            self.X -= 1
        elif self.states[4] and self.X < ROWS-1 and not self.hitbox[3]:
            self.X += 1
        else:
            for x in range(5):
                self.states[x] = False
            for x in range(4):
                self.hitbox[x] = False
            self.states[0] = True

    def update(self):
        # OPS must be in this order!
        self.input()
        self.movement()
        self.rect.center = self.positions[self.X][self.Y].center
        
    
    def destroy(self):
        self.kill()





  
