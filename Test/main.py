import pygame
import game
import configuration
#import configuration
import input

def main():
    """
    Ricochet Robot AI board game
    """
    # Import the static configurations of the game
    c = configuration
    # Import Game
    b = game.board()
    # Initialize pygame
    pygame.init()
    # Set screen size of game
    screen = pygame.display.set_mode(c.WINDOW_SIZE)
    # Set title of screen
    pygame.display.set_caption(c.TITLE)
    # Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while not done:
        # Set the screen background
        screen.fill(c.BLACK)
        # Input event
        for event in pygame.event.get():  # All user events
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     input.mouse(event)
            elif event.type == pygame.KEYDOWN:
                input.keyboard(event)
        # Canvas Update
        b.grid(pygame)
    
        # Limit to 60 frames per second
        clock.tick(60)
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()