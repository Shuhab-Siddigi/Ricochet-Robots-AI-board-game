from this import d

from pygame import Surface
import pygame
from SpriteImages.spritesheet import Spritesheet


class Knuckles:
    # Positions
    PosX = 0
    PosY = 0
    # Movements
    
    def __init__(self):
        sp = Spritesheet("./CharacterSpriteSheets/Knuckles.png")
        self.LEFT =  sp.getSprite(0,0,186,186)
        self.RIGHT = pygame.transform.flip(self.LEFT,True, False)
        self.UP = sp.getSprite(300,186*2,186,186)
        self.DOWN = sp.getSprite(0,0,190,190)
        self.GLIDERIGHT = sp.getSprite(40,190*2,190,190)
        self.GLIDELEFT = pygame.transform.flip(self.GLIDERIGHT,True, False)
    
        