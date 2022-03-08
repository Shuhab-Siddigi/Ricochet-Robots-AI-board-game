from typing import List
import pygame
from game.constants import COLS, MARGIN, ROWS, TILE_SIZE

class Player(pygame.sprite.Sprite):
    """A player object for the game """
    def __init__(self):
        super().__init__()
       
        spreedsheet = pygame.image.load("Resources/playersheet.jpg").convert_alpha()
        
        self.image = pygame.Surface((TILE_SIZE+MARGIN,TILE_SIZE+MARGIN)) # screen surface
        self.image.fill('White')
        self.image.blit(spreedsheet,(0,0),(50,50,50,50))
        
        self.rect =  pygame.Rect(0, TILE_SIZE*0, TILE_SIZE, TILE_SIZE)
        self.X = 0
        self.Y = 0

        self.states = ["IDLE","UP","DOWN","LEFT","RIGHT"]
        self.state = "IDLE"
        # TOP,BOTTOM,LEFT,RIGHT
        self.hitbox = [bool,bool,bool,bool]
        
        self.positions = []
        for x in range(ROWS):
            self.positions.append([x])
            for y in range(COLS):
                self.positions[x].append([y])
                self.positions[x][y] = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        
        # Move animation lists
        self.animations = []
        for x in range(9):
            self.animations.append([x])
            for y in range(4):
                self.animations[x].append([y])
                surface = pygame.Surface((TILE_SIZE,TILE_SIZE))
                surface.fill('White')
                self.animations[x][y] = surface
                self.animations[x][y].blit(spreedsheet,(0,0),(x*50,y*50,50,50))
        
        self.frame_index = 0
        self.frame_action = 0
        
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 500
        
    def input(self):
        key = pygame.key.get_pressed()
        if self.state == "IDLE":
            if key[pygame.K_UP]:
                self.state = self.states[1]    
                self.image= self.animations[0][0]
            if key[pygame.K_DOWN]:
                self.state = self.states[2]
                self.image= self.animations[0][0]
            if key[pygame.K_LEFT]:
                self.state = self.states[3]
                self.image= self.animations[0][0]
            if key[pygame.K_RIGHT]:
                self.state = self.states[4]
                self.image= self.animations[0][0]
   
    def collision(self,wall:pygame.rect):
        collision_tolerence = MARGIN
        if self.rect.colliderect(wall):
            if abs(wall.rect.bottom - self.rect.top) < collision_tolerence:
                print("HIT TOP")
                self.hitbox[0] = True
            if abs(wall.rect.top - self.rect.bottom) < collision_tolerence:
                print("HIT BOTTOM")
                self.hitbox[1] = True
            if abs(wall.rect.right - self.rect.left) < collision_tolerence:
                print("HIT LEFT")
                self.hitbox[2] = True
            if abs(wall.rect.left - self.rect.right) < collision_tolerence:
                print("HIT RIGHT")
                self.hitbox[3] = True
    
    def movement(self):
        if self.state == "UP" and self.Y > 0 and not self.hitbox[0]:
            self.Y -= 1
        elif self.state == "DOWN" and self.Y < COLS-1 and not self.hitbox[1]:
            self.Y += 1
        elif self.state == "LEFT" and self.X > 0 and not self.hitbox[2]:
            self.X -= 1
        elif self.state == "RIGHT" and self.X < ROWS-1 and not self.hitbox[3]:
            self.X += 1
        else:
            self.state = "IDLE"
            for x in range(4):
                self.hitbox[x] = False


    def update(self):
        # OPS must be in this order!
        self.input()
        self.movement()
        self.rect.topleft = self.positions[self.X][self.Y].topleft
    
    def destroy(self):
        self.kill()