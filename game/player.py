from typing import Dict
import pygame
from game.constants import TILE_SIZE
from game.images import PlayerAnimations


class Player(pygame.sprite.Sprite):
    """A player object for the game """

    def __init__(self, graph: Dict, pos_x: int, pos_y: int, color: int):
        super().__init__()

        self.graph = graph
        # Set first animation frame
        self.animations = PlayerAnimations()
        self.color = color
        self.frame = 3 * self.color
        self.action = 0 # 0 down,1 left, 2 right, 3 up
        self.image = self.animations[self.frame][self.action]
        
        # Create collision rectangle
        self.rect = self.image.get_rect()
        
        # set player positions
        self.position = (pos_x, pos_y)
        self.isActive = False
        # Movement
        self.moves = []
        self.target = self.rect
        
        # Animation setup
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 40
        self.speed = 5
        
    
    def check_up(self,position,next):
        return next[0] == position[0] and next[1] < position[1] # up
    def check_down(self,position,next):
        return next[0] == position[0] and next[1] > position[1] # down
    def check_left(self,position,next):
        return next[0] < position[0] and next[1] == position[1] # left
    def check_right(self,position,next):
        return next[0] > position[0] and next[1] == position[1] # right

    def traverse_up(self,position):
        for next in self.graph[position]:
            if self.check_up(position,next): # up
                print("Got up node", next)
                self.moves.append(next)
                self.traverse_up(next)
    
    def traverse_down(self,position):
        for next in self.graph[position]:
            if self.check_down(position,next): # down
                print("Got down node", next)
                self.moves.append(next)
                self.traverse_down(next)
    def traverse_left(self,position):
        for next in self.graph[position]:
            if self.check_left(position,next): # left
                print("Got left node", next)
                self.moves.append(next)
                self.traverse_left(next)
 
    
    def traverse_right(self,position):
        for next in self.graph[position]:
            if self.check_right(position,next): # right
                print("Got right node", next)
                self.moves.append(next)
                self.traverse_right(next)
 
    def input(self,target):
        x = target[0]//TILE_SIZE
        y = target[1]//TILE_SIZE
        
        if not self.rect.center != self.target.center:
            if self.check_up(self.position,(x,y)): # Up
                self.traverse_up(self.position)
            
            elif self.check_down(self.position,(x,y)): # Down
                self.traverse_down(self.position)
            
            elif self.check_left(self.position,(x,y)): # Left
                self.traverse_left(self.position)
            
            elif self.check_right(self.position,(x,y)): # Right
                self.traverse_right(self.position)
    
    def update(self):
        now = pygame.time.get_ticks()
        position = self.rect.center
        target = self.target.center
        if position != target:
            print(position,target)
            if now - self.last_update > self.animation_cooldown:
                self.last_update = now
                self.frame = (self.frame + 1) % 3
                self.image = self.animations[self.frame + 3 * self.color][self.action]
                if self.check_up(position,target):
                    self.action = 3
                    self.rect.centery -= self.speed 
                elif self.check_down(position,target):
                    self.action = 0
                    self.rect.centery += self.speed 
                elif self.check_left(position,target):
                    self.action = 1
                    self.rect.centerx -= self.speed 
                elif self.check_right(position,target):
                    self.action = 2
                    self.rect.centerx += self.speed
        elif len(self.moves) != 0:
                ("Updating list")
                target = self.moves.pop(0)
                self.target = pygame.Rect(
                    target[0]*TILE_SIZE,
                    target[1]*TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                )
        else:
            self.position = (self.target.x//TILE_SIZE,self.target.y//TILE_SIZE)

    def destroy(self):
        self.kill()
