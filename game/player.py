from typing import Dict
import pygame
from game.constants import TILE_SIZE
from game.images import PlayerAnimations
from logic.algorithms import check_down, check_left, check_right, check_up


class Player(pygame.sprite.Sprite):
    """A player object for the game """

    def __init__(self, graph: Dict, position, color: int):
        super().__init__()

        self.graph = graph
        # Set first animation frame
        self.animations = PlayerAnimations()
        self.color = color
        self.frame = 3 * self.color
        self.action = 0  # 0 down,1 left, 2 right, 3 up
        self.image = self.animations[self.frame][self.action]

        # Create collision rectangle
        self.rect = self.image.get_rect()
        self.rect.x = position[0] * TILE_SIZE
        self.rect.y = position[1] * TILE_SIZE
        # set player positions
        self.position = (self.rect.x // TILE_SIZE, self.rect.y // TILE_SIZE)

        self.is_active = False
        # Movement
        self.player_positions = [None] * 4
        # Animation setup
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 40
        self.speed = 5
        self.is_walking = False

    def travel(self, checktype, position):
        target = position
        has_next = False
        for next in self.graph[position]:
            if checktype(position, next):
                if not any(next == p for p in self.player_positions):
                    has_next = True
                    target = next
        if has_next:
            return self.travel(checktype, target)
        else:
            return target

    def up(self):
        self.position = self.travel(check_up, self.position)
        self.is_walking = True

    def down(self):
        self.position = self.travel(check_down, self.position)
        self.is_walking = True

    def left(self):
        self.position = self.travel(check_left, self.position)
        self.is_walking = True

    def right(self):
        self.position = self.travel(check_right, self.position)
        self.is_walking = True

    def add_players(self, players):
        self.players = players

    def input(self, target):
        rect_position = (target[0] // TILE_SIZE, target[1] // TILE_SIZE)

        if not self.is_walking:
            if check_up(self.position, rect_position):  # Up
                self.up()
            elif check_down(self.position, rect_position):  # Down
                self.down()
            elif check_left(self.position, rect_position):  # Left
                self.left()
            elif check_right(self.position, rect_position):  # Right
                self.right()
            else:
                print("invalid move or arrow not pressed")

    def movement(self):
        rect_position = (self.rect.x, self.rect.y)
        target = (self.position[0] * TILE_SIZE, self.position[1] * TILE_SIZE)

        if rect_position != target:
            self.is_walking = True
            if check_up(rect_position, target):
                self.action = 3
                self.rect.centery -= self.speed
            elif check_down(rect_position, target):
                self.action = 0
                self.rect.centery += self.speed
            elif check_left(rect_position, target):
                self.action = 1
                self.rect.centerx -= self.speed
            elif check_right(rect_position, target):
                self.action = 2
                self.rect.centerx += self.speed
        else:
            self.is_walking = False

    def animate(self):
        now = pygame.time.get_ticks()
        if self.is_walking and now - self.last_update > self.animation_cooldown:
            self.last_update = now
            self.frame = (self.frame + 1) % 3
            self.image = self.animations[self.frame +
                                         3 * self.color][self.action]

    def update_positions(self):
        self.player_positions = [player.position for player in self.players]

    def update(self):
        self.movement()
        self.animate()
        self.update_positions()

    def destroy(self):
        self.kill()
