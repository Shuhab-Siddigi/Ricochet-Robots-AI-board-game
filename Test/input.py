import pygame

class keyboard():
    def input(event):
        if event.key == pygame.K_LEFT:
            print("Pushed RIGHT")
        if event.key == pygame.K_RIGHT:
            print("Pushed LEFT")
        if event.key == pygame.K_UP:
            print("Pushed UP")
        if event.key == pygame.K_DOWN:
            print("Pushed DOWN")

# class mouse():
#         # User clicks the mouse. Get the position
#     pos = pygame.mouse.get_pos()
#     # Change the x/y screen coordinates to grid coordinates
#     column = pos[0] // (WIDTH + MARGIN)
#     row = pos[1] // (HEIGHT + MARGIN)
#     # Set that location to one
#     grid[row][column] = 1
#     print("Click ", pos, "Grid coordinates: ", row, column)