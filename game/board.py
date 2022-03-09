import pygame

from game.constants import BOARD_HEIGHT, BOARD_WIDTH, COLS, MARGIN, ROWS, TILE_SIZE

class BoardGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        # Create the border for the game
        boarder = Boarder()
        self.add(boarder)
        # Create the board for the game
        board = Board()
        board.rect.x = MARGIN
        board.rect.y = MARGIN
        self.add(board)
        # Create the midle emblem for the game
        emblem = Emblem()
        emblem.rect.x = MARGIN+TILE_SIZE*7
        emblem.rect.y = MARGIN+TILE_SIZE*7
        self.add(emblem)

class Boarder(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BOARD_WIDTH+MARGIN*2, BOARD_HEIGHT+MARGIN*2))
        self.image.fill('White')
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,'Black',self.rect, 5)

class Board(pygame.sprite.Sprite):
    """A Board object for the game """
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))
        self.image.fill('White')
        self.rect = self.image.get_rect()
        for rows in range(ROWS):
            for columns in range(COLS):
                rect = pygame.Rect(rows*TILE_SIZE, columns*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.image, (120, 120, 120), rect, 1)

class Emblem(pygame.sprite.Sprite):
    """A Emblem object for the game """
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((TILE_SIZE*2,TILE_SIZE*2))
        self.image.fill('White')
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,'Black',self.rect, 5)