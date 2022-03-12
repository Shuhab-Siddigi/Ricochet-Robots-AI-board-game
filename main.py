import pygame
import sys
from game import levels
from game.board import Board
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player


def main():
    """ Ricochet Robot AI board game """
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set screen size of game
    surface = pygame.Surface(screen.get_size())  # screen surface
    surface = surface.convert()  # Convert it to a pygame object
    surface.fill('White')  # Fill the first canvas white

    pygame.display.set_caption("  Ricochet Robot AI board game Group 13")  # Set title of screen
    clock = pygame.time.Clock()  # Used to manage how fast the screen updates

    obstacle_group = pygame.sprite.Group()
    board = Board(levels.Level0)
    player_group = pygame.sprite.Group()
    player = Player(board.graph, 4, 0, 0)
    player_group.add(player)

    def handle_events() -> None:
        """Handles all the different events in the game"""
        for event in pygame.event.get():  # All user events
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # clicked_sprites = [s for s in obstacle_group if s.rect.collidepoint(pos)]
            #     for sprite in clicked_sprites:
            #         print(sprite.rect)
            # for block in obstacle_group:
            #     if(pygame.sprite.collide_rect(player, block)):
            #         print(block.rect)
               
      # get a list of all sprites that are under the mouse cursor
    

    def draw():
        # Draw first screen
        screen.blit(surface, (0, 0))
        surface.blit(board,(0,0))
        obstacle_group.draw(surface)
        player_group.draw(surface)
        #board.draw(surface)

    def update():
        # Update Objects
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
        # Update objects
        update()


if __name__ == "__main__":
    main()
