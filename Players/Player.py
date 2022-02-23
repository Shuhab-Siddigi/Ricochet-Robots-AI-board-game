from this import d

from pygame import Surface
from SpriteImages.spritesheet import Spritesheet


class Knuckles:
    LEFT = Surface
    TALK = []
    
    def __init__(self):
        sp = Spritesheet("./CharacterSpriteSheets/Knuckles.png")
        self.LEFT =  sp.getSprite(0,0,190,190)
        for i in range(3):
            self.TALK.append(sp.getSprite(i*188,0,190,190))
    # def getLeft(self):
    #     return self.knuckles