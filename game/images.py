import pprint
from typing import Dict
import pygame

from game.constants import TILE_SIZE

class Images(Dict):
            
    def __init__(self):
        super().__init__()
        walls = [
            "C-", # Clear
            "N-", # North
            "E-", # East
            "S-", # South
            "W-", # West
            "NW", # North West
            "NE", # North East
            "SE", # South East
            "SW"  # South West  
        ]

        for wall in walls:
            # Wall
            image_str = "resources/tiles/{}.png".format(wall)
            image = pygame.image.load(image_str)
            self[wall] = pygame.transform.scale(image, (TILE_SIZE,TILE_SIZE))