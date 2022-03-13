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
        self.frame = 3 * color
        self.action = 0 # 0 down,1 left, 2 right, 3 up
        self.image = self.animations[self.frame][self.action]
        
        # Create collision rectangle
        self.rect = self.image.get_rect()
        
        # set player positions
        self.position = (pos_x, pos_y)
        
        # Movement
        self.moves = []
        self.path_found = False
        self.target = self.position
        self.is_walking = False

        # Animation setup
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 50
        
    
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
        
        if not self.is_walking:
            if self.check_up(self.position,(x,y)):
                self.traverse_up(self.position)
            
            elif self.check_down(self.position,(x,y)):
                self.traverse_down(self.position)
            
            elif self.check_left(self.position,(x,y)):
                self.traverse_left(self.position)
            
            elif self.check_right(self.position,(x,y)):
                self.traverse_right(self.position)
    
    
    def movement(self):
        
        if self.position != self.target:
            if self.check_up(self.position,self.target):
                self.rect.y -= TILE_SIZE
            elif self.check_down(self.position,self.target):
                self.rect.y += TILE_SIZE
            elif self.check_left(self.position,self.target):
                self.rect.x -= TILE_SIZE
            elif self.check_right(self.position,self.target):
                self.rect.x += TILE_SIZE
        else:
            if len(self.moves) != 0:
                self.target = self.moves.pop(0)
                self.is_walking = True
            else:
                self.is_walking = False
        # Update position
        self.position = (self.rect.x//TILE_SIZE,self.rect.y//TILE_SIZE)

    # def animate(self):
    #     if self.path_found:
    #         now = pygame.time.get_ticks()
    #         if now - self.last_update > self.animation_cooldown:
    #             self.last_update = now
    #             self.frame = (self.frame + 1) % 3
    #             self.image = self.animations[self.frame][self.action]

    
    def update(self):
        # OPS must be in this order!
        self.movement()
        #self.animate()
        print(self.moves,self.target,self.position)

    def destroy(self):
        self.kill()
