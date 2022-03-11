import pprint
import pygame

from game.constants import BOARD_HEIGHT, BOARD_POSITION_X, BOARD_POSITION_Y, BOARD_WIDTH, COLS, ROWS, TILE_SIZE
from game.images import Images
from logic.datastructures import Graph


class Board(pygame.sprite.Sprite):
    """A Board object for the game """

    def __init__(self, level: list):
        super().__init__()
        # Create board surface
        self.image = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))  # screen surface
        self.image.fill('White')
        self.rect = self.image.get_rect()
        # Load Images
        images = Images()
        # Create adjacency list        
        self.graph = Graph()

        # Draw objects on board
        for y in range(ROWS):
            for x in range(COLS):
                wall = level[y][x][:2]
                image = images[wall]
                self.image.blit(image, (x * TILE_SIZE, y * TILE_SIZE))
                # Create possible moves for x,y position
                self.graph.add_edge(level, x, y)


        emblem = pygame.image.load("resources/DTU-logo.jpg")
        emblem = pygame.transform.scale(emblem, (1.7 * TILE_SIZE, 1.7 * TILE_SIZE))
        self.image.blit(emblem, (7 * TILE_SIZE + 8, 7 * TILE_SIZE + 8))


class GUI(pygame.sprite.Group):
    """A Board object for the game """

    def __init__(self, level: list):
        super().__init__()
        board = Board(level)
        board.rect.x = BOARD_POSITION_X
        board.rect.y = BOARD_POSITION_Y
        self.graph = board.graph
        self.add(board)
