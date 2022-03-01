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
    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 20
    HEIGHT = 20
    # This sets the margin between each cell
    MARGIN = 5
    running = False
    board = []
    for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
        board.append([])
        for column in range(10):
            board[row].append(0)  # Append a cell

    def __init__(self):
        
       

        # Initialize game
        self.game.init()
        # Set up the drawing window
        self.screen = self.game.display.set_mode((
                self.DISPLAY_HEIGHT,
                self.DISPLAY_WIDTH
            )
        )
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()
        # Set Title
        self.game.display.set_caption("Ricochet Robot AI Game")
        # Set favicon
        favicon = self.game.image.load("Icons/favicon.png")
        self.game.display.set_icon(favicon)
        
        # Create players
        knuckles = Knuckles()
        knucklesAction = knuckles.LEFT
        # Start the game
        self.running = True
        index = 0
        # Game loop
        while self.running:
            # Close game by presseing close icon on window
            for event in pygame.event.get():
                # To be able to quit the game
                if event.type == pygame.QUIT:
                    self.running = False
                # Key Input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        knuckles.PosX -= 1
                        knucklesAction = knuckles.LEFT
                    if event.key == pygame.K_RIGHT:
                        knuckles.PosX += 1
                        knucklesAction = knuckles.RIGHT
                    if event.key == pygame.K_UP:
                         knuckles.PosY -= 1
                         knucklesAction = knuckles.UP
                    if event.key == pygame.K_DOWN:
                         knuckles.PosY += 1
                         knucklesAction = knuckles.GLIDERIGHT

            # Fill the background with white
            self.screen.fill((255, 255, 255))

            # Add the boy!
            # self.screen.blit(self.knuckles,(0,0))
            self.screen.blit(knucklesAction,(knuckles.PosX,knuckles.PosY))
            self.updateAll()      

        # Done! Time to quit.
        pygame.quit()
    
    def update(self):
        """Update Portion of the screen"""
        self.screen.update()
    
    def updateAll(self):
        """Update Everything on the screen"""
        self.game.display.flip()
    