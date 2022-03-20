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
#from logic.datastructures import get_astar_heuristic_dict


def main():
    """ Ricochet Robot AI board game """
    # Initialize pygame
    pygame.init() 
    # Set title of screen
    pygame.display.set_caption("  Ricochet Robot AI board game Group 13")
    # Set screen size of game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # Board can also be defined with prefixed values.
    start_positions = [(0, 0), (5, 2), (6, 4), (7, 3)]
    token = "GC"
    board = Board(levels.Level0,positions=start_positions,token=token)
    
    # Create a board
    #board = Board(levels.Level0)
    # Create right UI for player
    display = Display(board)
    
    # Test AI (Prefix has to be set)
    #goal = board.tokens[token]
    #board.commands = ai.solve("a_star", board.graph, board.players, token, goal)
    
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
        # Update all objects in board
        board.update()
        display.update()
        # Update display 
        pygame.display.update()
        # Define max FPS
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


 
    #token_color = token
    #goal = board.tokens[token]

    #print("token: ", goal)

    #test = ai.solve("BFS", board.graph, players, token_color, goal)

    # players[0].position = start_positions[0]
    # players[1].position = start_positions[1]
    # players[2].position = start_positions[2]
    # players[3].position = start_positions[3]

    #

    # commands = ai.solve("BFS", board.graph, players, token_color, goal)
    # test = get_astar_heuristic_dict(board.graph, goal)
    # print("goal: ", goal)
    # pprint.pprint(test)