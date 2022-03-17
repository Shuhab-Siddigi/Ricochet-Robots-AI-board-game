import random

import pygame
import sys
from game import levels
from game.board import Board
from game.constants import BOARD_HEIGHT, BOARD_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player
from logic import algorithms
from logic.datastructures import optimize_adjacency_list


def main():
    """ Ricochet Robot AI board game """
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set screen size of game
    surface = pygame.Surface(screen.get_size())  # screen surface
    surface = surface.convert()  # Convert it to a pygame object
    surface.fill('White')  # Fill the first canvas white

    pygame.display.set_caption("  Ricochet Robot AI board game Group 13")  # Set title of screen
    clock = pygame.time.Clock()  # Used to manage how fast the screen updates

    board_group = pygame.sprite.Group()
    board = Board(levels.Level0)
    for obstacle in board.obstacles:
        board_group.add(obstacle)
    
    player_group = pygame.sprite.Group()
    players = [
        Player(board.graph, 0, 0, 0), 
        Player(board.graph, 5, 2, 2),
        Player(board.graph, 6, 4, 1),
        Player(board.graph, 7, 3, 0)
    ]

    for player in players:
        player_group.add(player)

    token = random.choice(list(board.tokens.keys()))
    goal = board.tokens[token]
    print(goal)

    actions = algorithms.solve("BFS", board.graph, players, goal)

    def handle_events() -> None:
        """Handles all the different events in the game"""
        for event in pygame.event.get():  # All user events
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if board.inside_board(pos):
                    players[0].input(pos)

    def draw():
        # Draw first screen
        screen.blit(surface, (0, 0))
        surface.blit(board,(0,0))
        board_group.draw(surface)
        player_group.draw(surface)
        

    def update():
        # Update Objects
        positions = []
        for player in players:
            positions.append(player.position)
        for player in players:
            player.update_player_positions(positions)
      
        board.move_players(players,actions)

        # Update objects
        player_group.update()
        # Updates everything
        pygame.display.update()
        clock.tick(60)

    # -------- Main Program Loop -----------
    while True:
        # Handle events
        handle_events()
        # Draw on screen
        draw()

        update()




if __name__ == "__main__":
    main()

 