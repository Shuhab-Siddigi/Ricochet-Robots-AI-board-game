import pygame
import sys
from game import levels
from game.board import GUI
from game.constants import BOARD_HEIGHT, BOARD_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player

def main():

    """ Ricochet Robot AI board game """
    pygame.init() # Initialize pygame 
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # Set screen size of game
    surface = pygame.Surface(screen.get_size()) # screen surface
    surface = surface.convert() # Convert it to a pygame object
    surface.fill('White') # Fill the first canvas white

    pygame.display.set_caption("  Ricochet Robot AI board game Group 13") # Set title of screen
    clock = pygame.time.Clock() # Used to manage how fast the screen updates

    gui = GUI(levels.Level0)
    player = Player(0,0,0)
    gui.add(player)
    
    def handle_events() -> None:
        """Handles all the different events in the game"""
        for event in pygame.event.get():  # All user events
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def draw():
        # Draw first screen
        screen.blit(surface,(0,0))
        gui.draw(surface)
        
    def update():
        # Update Objects
        gui.update()
        # Updates everything
        pygame.display.update()
        clock.tick(30)
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
