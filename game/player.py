from typing import Dict
from matplotlib import animation

import pygame
from game.constants import COLS, MARGIN, ROWS, TILE_SIZE
from game.images import PlayerAnimations


class Player(pygame.sprite.Sprite):
    """A player object for the game """

    def __init__(self, graph: Dict, pos_x: int, pos_y: int, color: int):
        super().__init__()

        self.graph = graph
        # Set first animation frame
        self.animations = PlayerAnimations()
        self.frame = 3 * color
        self.action = 0 # 0 down,1 left, 2 right, 3 up
        self.image = self.animations[self.frame][self.action]
        
        # Create collision rectangle
        self.X, self.Y = pos_x, pos_y
        self.rect = self.image.get_rect()
        
        # Animation setup
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.states = [
            bool, # Idle
            bool, # Up
            bool, # Down
            bool, # Left
            bool  # Right 
        ]
    

    def input(self,position:tuple):
        self.X = position[0]//TILE_SIZE
        self.Y = position[1]//TILE_SIZE
        print(self.X,self.Y)
        # key = pygame.key.get_pressed()
        # if key[pygame.K_UP]:
        #     self.action = 3 # UP
        #     self.Y -= 1
        # if key[pygame.K_DOWN]:
        #     self.action = 0 # Down
        #     self.Y += 1
        # if key[pygame.K_LEFT]:
        #     self.action = 1 # Left
        #     self.X -= 1
        # if key[pygame.K_RIGHT]:
        #     self.action = 2 # Right
        #     self.X += 1
    def animate(self):
        if not self.states[0]:
            now = pygame.time.get_ticks()
            if now - self.last_update > self.animation_cooldown:
                self.last_update = now
                self.frame = (self.frame + 1) % 3
                self.image = self.animations[self.frame][self.action]
    
    def movement(self):
        if self.rect.y > self.Y*TILE_SIZE: # Up
            self.states[0] = False
            self.states[1] = True
            self.action = 3
            self.rect.y -= 5
        elif self.rect.y < self.Y*TILE_SIZE: # Down
            self.states[0] = False
            self.states[2] = True
            self.action = 0
            self.rect.y += 5
        elif self.rect.x > self.X*TILE_SIZE: # Left 
            self.states[0] = False
            self.states[3] = True
            self.action = 1
            self.rect.x -= 5
        elif self.rect.x < self.X*TILE_SIZE: # Right
            self.states[0] = False
            self.states[4] = True
            self.action = 2
            self.rect.x += 5
        else:
            for state in range(1,5):
                self.states[state] = False
            self.states[0] = True


    
    
    # def update_position(self):
    #     if self.rect.topleft != (self.X*TILE_SIZE,self.Y*TILE_SIZE):
    #         self.animate()
    
   

    def update(self):
        # OPS must be in this order!
        #self.input()
        #self.update_position()
        self.movement()
        self.animate()
        #self.update_position()
        #self.movement()

    # def destroy(self):
    #     self.kill()
