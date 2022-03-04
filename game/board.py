import pygame

from game.constants import BOARD_HEIGHT, BOARD_WIDTH, COLS, MARGIN, ROWS, SQUARE_SIZE
from test import SCREEN_HEIGHT, SCREEN_WIDTH


class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((BOARD_WIDTH,BOARD_WIDTH))                       # Create top surface (Canvas)
        #self.image = self.image.convert_alpha()                                                 # Convert it to a pygame object
        self.image.fill('White')
        # #     SCREEN_WIDTH-BOARD_WIDTH,   # Start X position
        #     SCREEN_HEIGHT-BOARD_HEIGHT) # Start Y posistion
        pygame.draw.rect(self.image, 'Black', pygame.Rect(
             SCREEN_WIDTH-BOARD_WIDTH,
             SCREEN_HEIGHT-BOARD_HEIGHT,
                10, 
                10
                ),  2)
        #pygame.draw.rect(self.image, 'Black', pygame.Rect(30, 30, 60, 60),  2)
        self.rect = self.image.get_rect()
    # def draw_cubes(self,surface:pygame.Surface):
    #     surface.fill('WHITE')


# for row in range(10):
#         for column in range(10):
#             color = WHITE
#             if grid[row][column] == 1:
#                 color = GREEN
#             pygame.draw.rect(screen,
#                              color,
#                              [(MARGIN + WIDTH) * column + MARGIN,
#                               (MARGIN + HEIGHT) * row + MARGIN,
#                               WIDTH,
#                               HEIGHT])
 