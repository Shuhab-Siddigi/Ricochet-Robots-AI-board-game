# Simple pygame program
# Follow this tutorial for pygame
# https://www.youtube.com/watch?v=ePiMYe7JpJo

# Follow this tutorial for pygame
# https://www.youtube.com/watch?v=ePiMYe7JpJo

# Import and initialize the pygame library
import pygame
from SpriteImages.spritesheet import Spritesheet
from Players.Player import Knuckles
class Game:
    game = pygame
    screen = pygame.display
    DISPLAY_HEIGHT = 600
    DISPLAY_WIDTH  = 600
    running = False

    def __init__(self):
        
        # Initialize game
        self.game.init()
        # Set up the drawing window
        self.screen = self.game.display.set_mode((
                self.DISPLAY_HEIGHT,
                self.DISPLAY_WIDTH
            )
        )

        knuckles = Knuckles()
        # Start the game
        self.running = True

        while self.running:

            # Close game by presseing close icon on window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Fill the background with white
            self.screen.fill((255, 255, 255))

            # Add the boy!
            # self.screen.blit(self.knuckles,(0,0))
            self.screen.blit(knuckles.LEFT,(0,0))
            self.updateAll()      

        # Done! Time to quit.
        pygame.quit()
    
    def update(self):
        """Update Portion of the screen"""
        self.screen.update()
    
    def updateAll(self):
        """Update Everything on the screen"""
        self.game.display.flip()