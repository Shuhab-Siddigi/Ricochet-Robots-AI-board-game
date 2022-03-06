# Game Constatns
SCREEN_WIDTH, SCREEN_HEIGHT = 1920,1080
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

# Board Constants
BOARD_WIDTH,BOARD_HEIGHT = 800,800
BOARD_SIZE = (BOARD_WIDTH,BOARD_HEIGHT)
# 16 for Tiles, 16 for edges
ROWS = 16
COLS = 16
BOARD_MARGIN = 2
TILE_SIZE = (BOARD_WIDTH//COLS,BOARD_HEIGHT//COLS)

# Wall Constants
MARGIN = 3
VERTICAL_WALL_SIZE = (MARGIN,BOARD_HEIGHT//COLS)
HORIZONTAL_WALL_SIZE = (TILE_SIZE[0],MARGIN)