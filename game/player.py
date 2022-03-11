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
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x*TILE_SIZE,pos_y*TILE_SIZE)

        # Animation setup
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100

    
    
    def right(self):
        pass
    def left(self):
        pass
    def up(self):
        pass
    def down(self):
        pass


    def input(self):
        if pygame.mouse.get_pressed()[0]:
            print(pygame.mouse.get_pos())

        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.action = 3 # UP
            self.rect.y -= 5
            self.idle = False
        elif key[pygame.K_DOWN]:
            self.action = 0 # Down
            self.rect.y += 5
            self.idle = False
        elif key[pygame.K_LEFT]:
            self.action = 1 # Left
            self.rect.x -= 5
            self.idle = False
        elif key[pygame.K_RIGHT]:
            self.action = 2 # Right
            self.rect.x += 5
            self.right()
            self.idle = False
        else:
            self.idle = True


    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_cooldown:
            self.last_update = now
            if not self.idle: 
                self.frame = (self.frame + 1) % 3
                self.image = self.animations[self.frame][self.action]
            
    def update(self):
        # OPS must be in this order!
        self.input()
        #self.moveTo()
        self.animate()
        # self.movement()
        #self.rect.center = self.positions[self.X][self.Y].center

    def destroy(self):
        self.kill()



    # def collision(self, sprite_group: pygame.sprite.Group):

    #     collision_tolerence = MARGIN

    #     for sprite in sprite_group:
    #         if self.rect.colliderect(sprite):
    #             if abs(sprite.rect.bottom - self.rect.top) < collision_tolerence:
    #                 print("HIT TOP")
    #                 self.hitbox[0] = True
    #             if abs(sprite.rect.top - self.rect.bottom) < collision_tolerence:
    #                 print("HIT BOTTOM")
    #                 self.hitbox[1] = True
    #             if abs(sprite.rect.right - self.rect.left) < collision_tolerence:
    #                 print("HIT LEFT")
    #                 self.hitbox[2] = True
    #             if abs(sprite.rect.left - self.rect.right) < collision_tolerence:
    #                 print("HIT RIGHT")
    #                 self.hitbox[3] = True

    # # applicable moves
    # def movement(self):
    #     # Check for board bounds
    #     # if self.states[1] and self.Y > 0 and not self.hitbox[0]:
    #     #     self.Y -= 1
    #     # elif self.states[2] and self.Y < COLS - 1 and not self.hitbox[1]:
    #     #     self.Y += 1
    #     # elif self.states[3] and self.X > 0 and not self.hitbox[2]:
    #     #     self.X -= 1
    #     # elif self.states[4] and self.X < ROWS - 1 and not self.hitbox[3]:
    #     #     self.X += 1
    #     # else:
    #     #     for x in range(5):
    #     #         self.states[x] = False
    #     #     for x in range(4):
    #     #         self.hitbox[x] = False
    #         self.states[0] = True
