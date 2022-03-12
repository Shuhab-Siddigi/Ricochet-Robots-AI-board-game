import pprint
import pygame

from game.constants import BOARD_HEIGHT, BOARD_POSITION_X, BOARD_POSITION_Y, BOARD_WIDTH, COLS, ROWS, TILE_SIZE
from game.images import Images
from logic.datastructures import Graph

class Board(pygame.surface.Surface):
    """A Board object for the game """
    def __init__(self, level: list):
        super().__init__((BOARD_WIDTH, BOARD_HEIGHT))
        # Create board surface
        self.fill('White')
        # Load Images
        images = Images()
        # Create adjacency list        
        self.graph = Graph()
        # Create list to hold all tiles for collison detection
        self.obstacles = []

        # Draw objects on board
        for y in range(ROWS):
            for x in range(COLS):
                wall = level[y][x][:2]
                image = images[wall]
                self.blit(image, (x * TILE_SIZE, y * TILE_SIZE))
                self.graph.add_edge(level, x, y)


        emblem = pygame.image.load("resources/DTU-logo.jpg")
        emblem = pygame.transform.scale(emblem, (1.7 * TILE_SIZE, 1.7 * TILE_SIZE))
        self.blit(emblem, (7 * TILE_SIZE + 8, 7 * TILE_SIZE + 8))

