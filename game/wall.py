import pygame

from game.constants import WALL_HEIGHT, WALL_WIDTH


class Wall(pygame.sprite.Sprite):
    """A player object for the game """
    def __init__(self,direction:str,posX:int,posY:int):
        # initiate sprite class
        super().__init__()
        if direction == "vertical":
            self.image = pygame.Surface([WALL_HEIGHT,WALL_WIDTH])
            self.image.fill('Black')
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.Surface([WALL_WIDTH,WALL_HEIGHT])
            self.image.fill('Black')
            self.rect = self.image.get_rect()
        
    def isCollision(self) -> bool:
        return self.rect.colliderect

    def update(self):
        self.input()
    
    def destroy(self):
        self.kill()
