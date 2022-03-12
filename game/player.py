from typing import Dict

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
        self.action = 0
        self.image = self.animations[self.frame][self.action]
        
        # Create collision rectangle
        self.X, self.Y = pos_x, pos_y
        self.rect = self.image.get_rect()
        
        # Animation setup
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.states = [bool,bool,bool,bool,bool]
    
    def position(self):
        if self.rect.topleft != (self.X,self.Y):
            self.rect.topleft = (self.X,self.Y)
    
    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.action = 3 # UP
            self.Y -= 1
        if key[pygame.K_DOWN]:
            self.action = 0 # Down
            self.Y += 1
        if key[pygame.K_LEFT]:
            self.action = 1 # Left
            self.X -= 1
        if key[pygame.K_RIGHT]:
            self.action = 2 # Right
            self.X += 1
        
        self.position()
     
    def animate(self):
        if not self.states[0]:
            now = pygame.time.get_ticks()
            if now - self.last_update > self.animation_cooldown:
                self.last_update = now
                self.frame = (self.frame + 1) % 3
                self.image = self.animations[self.frame][self.action]

    def update(self):
        # OPS must be in this order!
        self.input()
        
        self.animate()
        pygame.draw.rect(self.image,'Red',self.rect,5)
#        self.movement()

    def destroy(self):
        self.kill()
