# Simple pygame program

# Import and initialize the pygame library
import pygame
import configurations
import colors

class Engine:
    
    color = colors
    config = configurations
    game = pygame
    running = False
    window = game.display
    def __init__(self):
        # Initialize Pygame
        self.game.init()
        # Set up th drawing window
        self.window = self.game.display.set_mode((
            self.config.DISPLAY_WIDTH, 
            self.config.DISPLAY_HEIGHT
            )
        )
        self.running = True

    def startGame(self) -> None:
        # Run until the user asks to quit
       
        while self.running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the background with white
            screen.fill((255, 255, 255))

            # Draw a solid blue circle in the center
            pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

            # Flip the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()
