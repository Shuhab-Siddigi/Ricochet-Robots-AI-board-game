import configuration
class board:
    """The board is a plane where 4 pieces can be set in different orderes """
    def __init__(self,width=60,height=60):
        """Initialize the grid of the whole board"""
        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = width 
        self.HEIGHT = height
        # This sets the margin between each cell
        self.MARGIN = 5

        # Create a 2 dimensional array as the grid
        grid = []
        for row in range(10):
            # Add an empty array that will hold each cell
            # in this row
            grid.append([])
            for column in range(10):
                grid[row].append(0)  # Append a cell
    # def kvadrant_1():
    # def kvadrant_2():
    # def kvadrant_3():
    # def kvadrant_4():
    def grid(self,pygame):
        for row in range(10):
            for column in range(10):
                color = c.WHITE
                if self.grid[row][column] == 1:
                    color = c.GREEN
                pygame.draw.rect(screen,
                                color,
                                [(c.MARGIN + c.WIDTH) * column + c.MARGIN,
                                (c.MARGIN + c.HEIGHT) * row + c.MARGIN,
                                c.WIDTH,
                                c.HEIGHT])
