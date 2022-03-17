import pprint
import pygame

from game.constants import BOARD_HEIGHT, BOARD_WIDTH, COLS, MARGIN, ROWS, TILE_SIZE
from game.images import Images
from logic.datastructures import Board_graph

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Board(pygame.surface.Surface):
    """A Board object for the game """
    def __init__(self, level: list):
        super().__init__((BOARD_WIDTH, BOARD_HEIGHT))
        # Create board surface
        self.fill('White')
        # Load Images
        images = Images()
        # Create adjacency list        
        self.graph = Board_graph()
        # Create list to hold all tiles for collison detection
        self.obstacles = []

        # Draw objects on board
        for y in range(ROWS):
            for x in range(COLS):
                wall = level[y][x][:2]
                token = level[y][x][2:4]
                wall_image = images[wall]
                
                self.graph.add_edge(level, x, y)

                if token != "--":
                    token_image = images[token]
                    merged_image = wall_image.copy()
                    rect = merged_image.get_rect(centerx=token_image.get_width()+MARGIN,centery=token_image.get_height()+MARGIN)
                    #token_image.set_colorkey((255,255,255))
                    merged_image.blit(token_image,rect)
                    self.blit(merged_image, (x * TILE_SIZE, y * TILE_SIZE))
                elif wall == 'C-':
                    # Draw Wall
                    self.blit(wall_image, (x * TILE_SIZE, y * TILE_SIZE))
                else:
                    self.obstacles.append(Obstacle(wall_image,x * TILE_SIZE, y * TILE_SIZE))
                        
                
        emblem = pygame.image.load("resources/DTU-logo.jpg")
        emblem = pygame.transform.scale(emblem, (1.7 * TILE_SIZE, 1.7 * TILE_SIZE))
        self.obstacles.append(Obstacle(emblem,7 * TILE_SIZE + 8, 7 * TILE_SIZE + 8))
