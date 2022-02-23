import pygame 

class Spritesheet:

    def __init__(self,filename:str):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()

    def getSprite(self,x,y,w,h) -> pygame.Surface:
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h))
        return sprite
    
