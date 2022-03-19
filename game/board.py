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
        # Commands list
        self.history = []

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

    def create_arrows(self, player):

        self.arrows = pygame.sprite.Group()

        target = player.travel(check_up, player.position)
        start = player.rect.y - TILE_SIZE
        end = target[1] * TILE_SIZE
        for position in range(start, end - TILE_SIZE, -TILE_SIZE):
            if player == self.players[0]:
                self.arrows.add(Arrow(self.images["RUP"], player.rect.x, position))
            elif player == self.players[1]:
                self.arrows.add(Arrow(self.images["BUP"], player.rect.x, position))
            elif player == self.players[2]:
                self.arrows.add(Arrow(self.images["GUP"], player.rect.x, position))
            elif player == self.players[3]:
                self.arrows.add(Arrow(self.images["YUP"], player.rect.x, position))

        target = player.travel(check_down, player.position)
        start = player.rect.y + TILE_SIZE
        end = target[1] * TILE_SIZE
        for position in range(start, end + TILE_SIZE, TILE_SIZE):
            if player == self.players[0]:
                self.arrows.add(Arrow(self.images["RDOWN"], player.rect.x,position))
            elif player == self.players[1]:
                self.arrows.add(Arrow(self.images["BDOWN"], player.rect.x,position))
            elif player == self.players[2]:
                self.arrows.add(Arrow(self.images["GDOWN"], player.rect.x,position))
            elif player == self.players[3]:
                self.arrows.add(Arrow(self.images["YDOWN"], player.rect.x,position))

        target = player.travel(check_right, player.position)
        start = player.rect.x + TILE_SIZE
        end = target[0] * TILE_SIZE
        for position in range(start, end + TILE_SIZE, TILE_SIZE):
            if player == self.players[0]:
                self.arrows.add(Arrow(self.images["RRIGHT"], position, player.rect.y))
            elif player == self.players[1]:
                self.arrows.add(Arrow(self.images["BRIGHT"], position, player.rect.y))
            elif player == self.players[2]:
                self.arrows.add(Arrow(self.images["GRIGHT"], position, player.rect.y))
            elif player == self.players[3]:
                self.arrows.add(Arrow(self.images["YRIGHT"], position, player.rect.y))

        target = player.travel(check_left, player.position)
        start = player.rect.x - TILE_SIZE
        end = target[0] * TILE_SIZE
        for position in range(start, end - TILE_SIZE, -TILE_SIZE):
            if player == self.players[0]:
                self.arrows.add(Arrow(self.images["RLEFT"], position,player.rect.y))
            elif player == self.players[1]:
                self.arrows.add(Arrow(self.images["BLEFT"], position,player.rect.y))
            elif player == self.players[2]:
                self.arrows.add(Arrow(self.images["GLEFT"], position,player.rect.y))
            elif player == self.players[3]:
                self.arrows.add(Arrow(self.images["YLEFT"], position,player.rect.y))

        self.add(self.arrows)
    
    def draw_arrows(self,player,mouse_position):
        if player.rect.collidepoint(mouse_position):
                [arrow.kill() for arrow in self.arrows]
                player.is_active = True
                self.create_arrows(player)

        elif self.has(self.arrows) and player.is_active:
            for arrow in self.arrows:
                if arrow.is_clicked() and player.is_active:
                    move = player.input(mouse_position)
                    [arrow.kill() for arrow in self.arrows]
                    if player == self.players[0]:
                        self.history.append((0,move))
                    if player == self.players[1]:
                        self.history.append((1,move))
                    if player == self.players[2]:
                        self.history.append((3,move))
                    if player == self.players[3]:
                        self.history.append((4,move))
        

        elif len(self.arrows.spritedict) == 0:
                for player in self.players:
                    player.is_active = False
    
    def events(self,mouse_position):
        if not any(player.is_walking for player in self.players):
            for player in self.players:
                self.draw_arrows(player,mouse_position)

    def commands(self, commands, players):
        if not any(player.is_walking for player in players):
            if len(commands) != 0:
                command = commands.pop(0)
                self.history.append(command)
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