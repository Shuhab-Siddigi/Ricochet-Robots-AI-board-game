from turtle import width
from matplotlib.font_manager import get_font
import pygame

from game.constants import BOARD_WIDTH, MARGIN, TILE_SIZE, UI_HEIGHT, UI_WIDTH
from game.images import Images
from game.ui import get_font

def get_font(text, size, color):
    # Get UI Font
    font = pygame.font.Font("resources/Atarian.ttf", size)
    # Render text
    return font.render(text, True, color)

class Player(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_active = False
    
    def update(self):
        if self.is_active:
            pass

class Tile(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale(image, (TILE_SIZE*2, TILE_SIZE*2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Object(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Target(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.target = None
    def update(self):
        if self.target != None:
            self.image.blit(self.target,(
                MARGIN*2,
                MARGIN*2
            ))

    

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

        self.images = Images()
        
        self.background()

        image = get_font(" Player      AI", 31, 'White')
        self.player_text = Object(image, BOARD_WIDTH + MARGIN*3, 10)
        self.add(self.player_text)
        
        knucles = pygame.image.load("resources/knuckles.png")
        knucles = pygame.transform.scale(knucles,(TILE_SIZE,TILE_SIZE-MARGIN))
        player_image = Player(knucles,BOARD_WIDTH+28,45)
        self.add(player_image)

        ai = pygame.image.load("resources/robot.png")
        ai = pygame.transform.scale(ai,(TILE_SIZE-MARGIN,TILE_SIZE-MARGIN))
        ai_image = Player(ai,BOARD_WIDTH+125,45)
        self.add(ai_image)

        image = get_font("Target", 40, 'White')
        self.moves = Object(image, BOARD_WIDTH + UI_WIDTH // 2 - image.get_width() // 2, 100)
        self.add(self.moves)

        self.target = self.target()
        self.add(self.target)
        
        # self.moves = Object(image, BOARD_WIDTH + UI_WIDTH // 2 - image.get_width() // 2, 100)
        # self.add(self.moves)
    
    def background(self):
        self.add(Tile(self.images["NW"],BOARD_WIDTH,0))
        self.add(Tile(self.images["NE"],BOARD_WIDTH+TILE_SIZE*2,0))
        
        for y in range(0,TILE_SIZE*2*7,TILE_SIZE*2):
            self.add(Tile(self.images["W-"],BOARD_WIDTH,y))
            self.add(Tile(self.images["E-"],BOARD_WIDTH+TILE_SIZE*2,y))

        self.add(Tile(self.images["SW"],BOARD_WIDTH,TILE_SIZE*2*7))
        self.add(Tile(self.images["SE"],BOARD_WIDTH+TILE_SIZE*2,TILE_SIZE*2*7))

    def target(self):
        surface = pygame.Surface((TILE_SIZE*2,TILE_SIZE*2))
        surface.blit(self.images["NW"],(0,0))
        surface.blit(self.images["NE"],(TILE_SIZE,0))
        surface.blit(self.images["SW"],(0,TILE_SIZE))
        surface.blit(self.images["SE"],(TILE_SIZE,TILE_SIZE))
        return Target(surface,BOARD_WIDTH+UI_WIDTH // 4,150)

    def set_target(self,target):
        image = pygame.transform.scale(self.images[target],(TILE_SIZE*2-MARGIN*4,TILE_SIZE*2-MARGIN*4))
        self.target.target = image
    
    def events(self, mouse_pos):
        if self.moves.rect.collidepoint(mouse_pos):
            #print("mouse is over moves")
            pass
    
#    self.counter = Counter(get_font(str(0),60,'White'), BOARD_WIDTH + UI_WIDTH // 2-10, 49)
#         self.add(self.counter)