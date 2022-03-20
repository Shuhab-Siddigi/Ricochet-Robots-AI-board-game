import pprint
import random
import sys

import pygame

from game import levels
from game.board import Board
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player
from game.ui import Display
from logic import ai
from logic.datastructures import get_astar_heuristic_dict


def main():
    """ Ricochet Robot AI board game """
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))  # Set screen size of game
    pygame.display.set_caption(
        "  Ricochet Robot AI board game Group 13")  # Set title of screen
    clock = pygame.time.Clock()  # Used to manage how fast the screen updates

    board = Board(levels.Level0)
    display = Display()
    counter = 0

    #start_positions = [(0, 0), (5, 2), (6, 4), (7, 3)]
    start_positions = []

    for _ in range(4):
        start_positions.append((random.randint(0, 15), random.randint(0, 15)))

    players = [
        Player(board.graph, start_positions[0], 0),
        Player(board.graph, start_positions[1], 2),
        Player(board.graph, start_positions[2], 1),
        Player(board.graph, start_positions[3], 0)
    ]

    # add players to other players
    [player.add_players(players) for player in players]
    # Add players to board
    board.add_players(players)

    # Create a list of commands for the players
    commands = []

    token = random.choice(list(board.tokens.keys()))
    token_color = token
    goal = board.tokens[token]

    commands = ai.solve("BFS", board.graph, players, token_color, goal)
    test = get_astar_heuristic_dict(board.graph, goal)
    print("goal: ", goal)
    pprint.pprint(test)

    def handle_events() -> None:
        """Handles all the different events in the game"""
        for event in pygame.event.get():  # All user events
            board.events(event)
            display.events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw():
        # Draw first screen
        board.draw(screen)
        display.draw(screen)
 
    def update():
        board.commands(commands, players)
        # Update all objects in board
        board.update()
        display.update()
        display.set_token(token)
 
        pygame.display.update()
        clock.tick(60)

    # -------- Main Program Loop -----------
    while True:
        # Handle events
        handle_events()
        # Draw on screen
        draw()
        # Update
        update()


if __name__ == "__main__":
    main()
