import pygame
import sys
from game.board import Board
from game.constants import *
from game.player import Player
from logic import Graph

def main():
    """ Ricochet Robot AI board game """
    pygame.init() # Initialize pygame 
    screen = pygame.display.set_mode(SCREEN_SIZE) # Set screen size of game
    
    surface = pygame.Surface(screen.get_size()) # screen surface
    surface = surface.convert() # Convert it to a pygame object
    surface.fill('White') # Fill the first canvas white

    pygame.display.set_caption("  Ricochet Robot AI board game Group 13") # Set title of screen
    pygame.display.set_icon( # Set the left corner icon
        pygame.image.load("Resources/AI.png") # input image
    )

    clock = pygame.time.Clock() # Used to manage how fast the screen updates
    # Create Game Sprites 
    board_group = pygame.sprite.Group()
    board = Board()
    board_group.add(board)
    
    player = Player()
    player.set_walls(board.walls)
    board_group.add(player)
    
    

    
    def handle_events() -> None:
        """Handles all the different events in the game"""
        for event in pygame.event.get():  # All user events
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    #def update():
        #if player.rect.colliderect(rect):
            #print("HIT")

    def draw() -> None:
        """Draws objects on the screen"""
        # Draw board Group
        screen.blit(surface,(0,0))
        board_group.draw(screen)
 
    # -------- Main Program Loop -----------
    while True:
        # Handle events
        handle_events()
        # Draw on screen
        draw()
        # Update objects
        player.update()
        # Updates everything
        #pygame.display.flip
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()


 # image = pygame.image.load('Resources/board.png').convert_alpha()
    # board_surface = pygame.transform.scale(image, screen.get_size())
    #board_surface = pygame.Surface(screen.get_size())
    # maze_surface = pygame.Surface(screen.get_size())
    # maze_surface.fill('White')
    # Create a grid
    ### Initialize Game objects