import pygame

from game.constants import COLS, MARGIN, ROWS, TILE_SIZE
from game.images import Images
from logic.datastructures import Board_graph
from logic.algorithms import check_down, check_left, check_right, check_up
from game.images import Images


class Arrow(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(self.rect.x, self.rect.y, TILE_SIZE, TILE_SIZE)
        self.rect.x = x + MARGIN * 2
        self.rect.y = y + MARGIN * 2

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(
            pygame.mouse.get_pos())


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Board(pygame.sprite.Group):
    """A Board object for the game """

    def __init__(self, level: list):
        super().__init__()
        # Load Images
        self.images = Images()
        # Create adjacency list
        self.graph = Board_graph()
        # Create a list to hold all tokens for collision detection
        self.tokens = {}
        # Create list of players
        self.players = []
        # add objects to board
        self.arrows = pygame.sprite.Group()

        for y in range(ROWS):
            for x in range(COLS):
                self.graph.add_edge(level, x, y)

                wall = level[y][x][:2]
                token = level[y][x][2:4]
                wall_image = self.images[wall]

                # Create a copy of image
                image = wall_image.copy()

                if token != "--":
                    token_image = self.images[token]
                    rect = image.get_rect(
                        centerx=token_image.get_width() + MARGIN,
                        centery=token_image.get_height() + MARGIN)
                    image.blit(token_image, rect)
                    if token not in self.tokens:
                        self.tokens[token] = None
                    self.tokens[token] = (x, y)

                self.add(Obstacle(image, x * TILE_SIZE, y * TILE_SIZE))

        emblem = pygame.image.load("resources/DTU-logo.jpg")
        emblem = pygame.transform.scale(emblem,
                                        (1.7 * TILE_SIZE, 1.7 * TILE_SIZE))
        self.add(Obstacle(emblem, 7 * TILE_SIZE + 8, 7 * TILE_SIZE + 8))

    def add_players(self, players):
        self.players = players
        self.add(players)

    def events(self,mouse_position):
        if not any(player.is_walking for player in self.players):
            
            for player in self.players:
                if player.rect.collidepoint(mouse_position):
                    [arrow.kill() for arrow in self.arrows]
                    player.is_active = True
                    self.create_arrows(player)

                if self.has(self.arrows) and player.is_active:
                    for arrow in self.arrows:
                        if arrow.is_clicked() and player.is_active:
                            player.input(mouse_position)
                            [arrow.kill() for arrow in self.arrows]

        if len(self.arrows.spritedict) == 0:
            for player in self.players:
                player.is_active = False

    def create_arrows(self, player):

        self.arrows = pygame.sprite.Group()

        target = player.travel(check_up, player.position)
        start = player.rect.y - TILE_SIZE
        end = target[1] * TILE_SIZE
        for position in range(start, end - TILE_SIZE, -TILE_SIZE):
            self.arrows.add(Arrow(self.images["UP"], player.rect.x, position))

        target = player.travel(check_down, player.position)
        start = player.rect.y + TILE_SIZE
        end = target[1] * TILE_SIZE
        for position in range(start, end + TILE_SIZE, TILE_SIZE):
            self.arrows.add(Arrow(self.images["DOWN"], player.rect.x,
                                  position))

        target = player.travel(check_right, player.position)
        start = player.rect.x + TILE_SIZE
        end = target[0] * TILE_SIZE
        for position in range(start, end + TILE_SIZE, TILE_SIZE):
            self.arrows.add(
                Arrow(self.images["RIGHT"], position, player.rect.y))

        target = player.travel(check_left, player.position)
        start = player.rect.x - TILE_SIZE
        end = target[0] * TILE_SIZE
        for position in range(start, end - TILE_SIZE, -TILE_SIZE):
            self.arrows.add(Arrow(self.images["LEFT"], position,
                                  player.rect.y))

        self.add(self.arrows)

    def commands(self, commands, players):
        if not any(player.is_walking for player in players):
            if len(commands) != 0:
                command = commands.pop(0)
                player = command[0]
                action = command[1]
                p = players[player]

                if action == "Up":
                    p.up()
                if action == "Down":
                    p.down()
                if action == "Left":
                    p.left()
                if action == "Right":
                    p.right()