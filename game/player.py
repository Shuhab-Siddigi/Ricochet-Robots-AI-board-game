from turtle import position
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
        # Create possible positions
        self.position = (pos_x, pos_y)
        self.target = (pos_x, pos_y)
        self.next = self.position

        # Animation setup
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.state = "IDLE"

    # def find_next(self,position):
    #     if self.target != self.position and self.states[0]:
    #         for next in self.graph[position]:
    #             if next[0] == self.target[0] and next[1] >= self.target[1]: # Up 
    #                 self.position = next
    #             elif  next[0] == self.target[0] and next[1] <= self.target[1]: # Down
    #                 self.position = next
    #             elif  next[0] >= self.target[0] and next[1] == self.target[1]: # Left
    #                 self.position = next
    #             elif next[0] <= self.target[0] and next[1] == self.target[1]: # Right
    #                 self.position = next
    
      
    def input(self,target):
        x = target[0]//TILE_SIZE
        y = target[1]//TILE_SIZE
        print(x,y)
        if y < self.position[1]:
            self.state = "UP"
        elif y > self.position[1]:
            self.state = "DOWN"
        elif x < self.position[0]:
            self.state = "LEFT"
        elif x > self.position[0]:
            self.state = "RIGHT"
    #def movement(self):  
        
        # if self.target != self.position: # Right
        #     self.find_next(self.position)
        #     if self.next != None:
        #         print("Got next", self.next)
        #         if  self.next[1]*TILE_SIZE < self.rect.y: # Up
        #             self.states[0] = False
        #             self.states[1] = True
        #             self.action = 3
        #             self.rect.y = self.next[1]*TILE_SIZE
                
        #         elif self.next[1]*TILE_SIZE > self.rect.y: # Down
        #             self.states[0] = False
        #             self.states[2] = True
        #             self.action = 0
        #             self.rect.y = self.next[1]*TILE_SIZE
                
        #         elif self.next[0]*TILE_SIZE < self.rect.x: # Left 
        #             self.states[0] = False
        #             self.states[3] = True
        #             self.action = 1
        #             self.rect.x = self.next[0]*TILE_SIZE
                
        #         elif self.next[0]*TILE_SIZE >  self.rect.x : # Right
        #             self.states[0] = False
        #             self.states[4] = True
        #             self.action = 2
        #             self.rect.x = self.next[0]*TILE_SIZE
        #         else:
                    # self.position = (self.rect.x//TILE_SIZE,self.rect.y//TILE_SIZE)
            # else:
            #     for state in range(1,5):
            #         self.states[state] = False
            #     self.states[0] = True
        
    # def animate(self):
    #     if not self.states[0]:
    #         now = pygame.time.get_ticks()
    #         if now - self.last_update > self.animation_cooldown:
    #             self.last_update = now
    #             self.frame = (self.frame + 1) % 3
    #             self.image = self.animations[self.frame][self.action]
     

  
    def update(self):
        # OPS must be in this order!
        #self.movement()
        for next in self.graph[self.position]:
            if self.state == "UP":
                if next[0] == self.position[0] and next[1] < self.position[1]: # up
                    print("UP got next left", next)
                    self.position = next

            if self.state == "DOWN":
                if next[0] == self.position[0] and next[1] > self.position[1]: # down
                    print("DOWN got next left", next)
                    self.position = next

            if self.state == "LEFT":
                if next[0] < self.position[0] and next[1] == self.position[1]: # left
                    print("LEFT got next left", next)
                    self.position = next
        
            if self.state == "RIGHT":
                print(self.position)
                if next[0] > self.position[0] and next[1] == self.position[1]: # right
                    print("RIGHT got next left", next)
                    self.position = next

        self.rect.x = self.position[0]*TILE_SIZE
        self.rect.y = self.position[1]*TILE_SIZE
        #self.update_position()
        #self.animate()
        #self.update_position()
        #self.movement()

    # def destroy(self):
    #     self.kill()
