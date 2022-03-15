import pprint
from typing import Dict
import pygame

from game.constants import TILE_SIZE, MARGIN


class Images(Dict):

    def __init__(self):
        super().__init__()
        walls = [
            "C-",  # Clear
            "N-",  # North
            "E-",  # East
            "S-",  # South
            "W-",  # West
            "NW",  # North West
            "NE",  # North East
            "SE",  # South East
            "SW"  # South West  
        ]

        for wall in walls:
            # Wall
            image_str = "resources/tiles/{}.png".format(wall)
            image = pygame.image.load(image_str)
            self[wall] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

class PlayerAnimations(list):
    # Move animation lists
    def __init__(self):
        spreedsheet = pygame.image.load("Resources/playersheet.jpg").convert_alpha()

        for x in range(9):
            self.append([x])
            for y in range(4):
                self[x].append([y])
                # Create a surface for the image
                surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
                # Fill white
                surface.fill('White')
                # Make transparent
                surface.set_colorkey((255,255,255))
                # add surface in list
                self[x][y] = surface
                # Load part of the spreedsheet
                image = spreedsheet.subsurface((x * 48, y * 48, 50, 50))
                # Should make it more understandable for pygame
                image.convert_alpha()
                # Remove all white color
                image.set_colorkey((255,255,255))
                # Transform the image to a valid size
                image = pygame.transform.scale(image, (TILE_SIZE-MARGIN*2, TILE_SIZE-MARGIN*2))
                # place image on surface
                self[x][y].blit(image,(MARGIN, MARGIN//2))
                