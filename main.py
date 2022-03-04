import pygame
import sys
from game.board import Board
from game.constants import *
from game.player import Player

def main():
    """ Ricochet Robot AI board game """
    pygame.init()                                                           # Initialize pygame 
    screen = pygame.display.set_mode(SCREEN_SIZE,0,32)                      # Set screen size of game
    clock = pygame.time.Clock()                                             # Used to manage how fast the screen updates
    surface = pygame.Surface(screen.get_size())                             # Create top surface (Canvas)
    surface = surface.convert()                                             # Convert it to a pygame object
    surface.fill('White')                                                   # Fill the first canvas white
    pygame.display.set_caption("  Ricochet Robot AI board game Group 13")   # Set title of screen
    pygame.display.set_icon( pygame.image.load("Resources/AI.png") )        # Set the left corner icon

    ### Initialize Game objects
    # board = pygame.Surface((BOARD_WIDTH,BOARD_WIDTH))                       # Create top surface (Canvas)
    # board = board.convert()                                                 # Convert it to a pygame object
    # board.fill('White')
    board_group = pygame.sprite.Group()
    board = Board()
    board_group.add(board)
    
    player = Player()
    board_group.add(player)

    def handle_events() -> None:
        """Handles all the different events in the game"""
        for event in pygame.event.get():  # All user events
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw() -> None:
        """Draws objects on the screen"""
        # Draw the first canvas
        screen.blit(surface,(0,0))
        board_group.draw(surface)
        # screen.blit(board,(
        #     SCREEN_WIDTH-BOARD_WIDTH,   # Start X position
        #     SCREEN_HEIGHT-BOARD_HEIGHT) # Start Y posistion
        # )
        #board.draw(surface)
        #b.draw_cubes(screen)
        #p.draw(screen)
        #b.draw(screen)
        #p.update()
        #board.update()
        #p.update(surface)

        #wall_group.draw(screen)
    def update():
        board.update()
        player.update()
    
    # -------- Main Program Loop -----------
    while True:
        # Handle events
        handle_events()
        # Draw on screen
        draw()
        # Update objects
        update()
        
        # Updates everything
        #pygame.display.flip
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()

  #board = pygame.image.load("Resources/board.svg")
    # Instantiate objects
    #b = pygame.sprite.Group()
    #b.add(board(SCREEN_WIDTH,SCREEN_HEIGTH,GRIDSIZE))
    #b = Board()
    #p = pygame.sprite.GroupSingle()
    #p.add(player())
    #wall = Wall(50,50,100,100)

    #wall_group = pygame.sprite.Group()
    #wall_group.add(wall)
