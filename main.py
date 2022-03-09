import pygame
import sys
from game.constants import *
from game.player import Player
from game.wall import MiddleSquare, WallGroup

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
    player_group = pygame.sprite.Group()
    player = Player(5,0)
    player_group.add(player)
    emblem_group = pygame.sprite.Group()
    wall_group = WallGroup()


    def handle_events() -> None:
        """Handles all the different events in the game"""
        for event in pygame.event.get():  # All user events
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for wall in wall_group:
            player.collision(wall)

        

    def draw() -> None:
        """Draws objects on the screen"""        
        screen.blit(surface,(0,0))
        # Draw board Grid   
        for x in range(16):
            for y in range(16):
                rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(surface, (120, 120, 120), rect, 1)

        player_group.draw(screen)
        wall_group.draw(screen)
        emblem_group.draw(screen)


    # -------- Main Program Loop -----------
    while True:
        # Handle events
        handle_events()
        # Draw on screen
        draw()
        # Update objects
        player.update()
        wall_group.update()
        emblem_group.update()
        # Updates everything
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()

#if pygame.sprite.spritecollideany(player,wall_group):
# image = pygame.image.load('Resources/board.png').convert_alpha()
# board_surface = pygame.transform.scale(image, screen.get_size())
#board_surface = pygame.Surface(screen.get_size())
# maze_surface = pygame.Surface(screen.get_size())
# maze_surface.fill('White')
# Create a grid
### Initialize Game objects

# if pygame.sprite.spritecollideany(player,wall_group):
#     print("HIT")


# emblem = pygame.sprite.Sprite()
# emblem.image = pygame.Surface((TILE_SIZE*2, TILE_SIZE*2))
# emblem.image.fill('White')
# emblem.rect = pygame.Rect(*surface.get_rect().center, 0, 0).inflate(TILE_SIZE*2, TILE_SIZE*2)
# image = pygame.image.load("Resources/DTU-logo.jpg").convert_alpha()
# emblem.image = pygame.transform.scale(image, (TILE_SIZE*2, TILE_SIZE*2))


# # emblem.rect = pygame.Rect(*surface.get_rect().center, 0, 0).inflate(TILE_SIZE*2, TILE_SIZE*2)