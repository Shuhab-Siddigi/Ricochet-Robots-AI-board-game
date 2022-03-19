from turtle import width
from matplotlib.font_manager import get_font
import pygame

from game.constants import BOARD_WIDTH, TILE_SIZE, UI_HEIGHT, UI_WIDTH
from game.images import Images
from game.ui import get_font

def get_font(text, size, color):
    # Get UI Font
    font = pygame.font.Font("resources/Atarian.ttf", size)
    # Render text
    return font.render(text, True, color)

class Tile(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale(image, (TILE_SIZE*2, TILE_SIZE*2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Button(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Counter(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.number = 0
        
    def update(self):
        self.image = get_font(str(self.number),60,'White')
        if self.number > 9:
            self.rect.x =  BOARD_WIDTH + UI_WIDTH // 2-20
        

class UI(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        images = Images()
        
        self.background(images)
        
        self.moves = get_font("Moves", 40, 'White')
        self.button = Button(self.moves, BOARD_WIDTH + UI_WIDTH // 2 - self.moves.get_width() // 2, 15)
        
        
        self.counter = Counter(
            get_font(str(0),60,'White'),
            BOARD_WIDTH + UI_WIDTH // 2-10, 
            50
        )
        
        self.add(self.button)
        self.add(self.counter)
        # Draw text
        #self.blit(moves,(UI_WIDTH//2-moves.get_width()//2,15))

        #font = pygame.font.Font("resources/Atarian.ttf",30)
        #self.moves = font.render('CHOSE PLAYER' , True , 'White')
        #self.blit(moves,(UI_WIDTH//2-moves.get_width()//2,100))

    
    def background(self,images):
        self.add(Tile(images["NW"],BOARD_WIDTH,0))
        self.add(Tile(images["NE"],BOARD_WIDTH+TILE_SIZE*2,0))
        
        for y in range(0,TILE_SIZE*2*7,TILE_SIZE*2):
            self.add(Tile(images["W-"],BOARD_WIDTH,y))
            self.add(Tile(images["E-"],BOARD_WIDTH+TILE_SIZE*2,y))

        self.add(Tile(images["SW"],BOARD_WIDTH,TILE_SIZE*2*7))
        self.add(Tile(images["SE"],BOARD_WIDTH+TILE_SIZE*2,TILE_SIZE*2*7))


    def events(self, mouse_pos):
        if self.button.rect.collidepoint(mouse_pos):
            print("mouse is over moves")
    
