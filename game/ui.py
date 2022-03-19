import pygame

from game.constants import BOARD_WIDTH, MARGIN, TILE_SIZE, UI_HEIGHT, UI_WIDTH
from game.images import Images

class Counter(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.font =  pygame.font.Font("resources/Atarian.ttf", 50)
        self.number = 0
        self.image = self.font.render(str(self.number), True, 'White')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.image = self.font.render(str(self.number), True, 'White')

class Token(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((2*TILE_SIZE,2*TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.token = None
    
    def update(self):
        if self.token != None:
            self.image = self.token

class Display():
    def __init__(self):
        self.surface = pygame.Surface((UI_WIDTH,UI_HEIGHT))
        self.surface.fill('White')
        
        self.sprite_group = pygame.sprite.Group()
        
        self.images = Images()
        
        # Images for UI 
        target_text = self.get_font("Target", 40, 'White')
        player_text = self.get_font("Player      AI  ", 32, 'White')
        boarder = self.target_boarder(self.images)
        knucles = pygame.image.load("resources/knuckles.png")
        knucles = pygame.transform.scale(knucles,(TILE_SIZE,TILE_SIZE-MARGIN))
        ai = pygame.image.load("resources/robot.png")
        ai = pygame.transform.scale(ai,(TILE_SIZE-MARGIN,TILE_SIZE-MARGIN))
        
        # Create background
        self.background(self.surface,self.images)
        # Draw images on surface
        self.surface.blit(target_text,(self.surface.get_width()//2-target_text.get_width()//2,0))
        self.surface.blit(boarder,(self.surface.get_width()//2-boarder.get_width()//2,50))
        self.token = Token(BOARD_WIDTH+2*MARGIN+self.surface.get_width()//2-boarder.get_width()//2,60)
        self.surface.blit(player_text,(self.surface.get_width()//2-player_text.get_width()//2,165))
        self.surface.blit(knucles,(self.surface.get_width()//4-knucles.get_width()//2,210))        
        x = self.surface.get_width()//2+self.surface.get_width()//4
        self.surface.blit(ai,(x-ai.get_width()//2,210))

        # add sprites
        self.sprite_group.add(self.token)
    
    def background(self,surface,images):
        E  = pygame.transform.scale(images["E-"],(2*TILE_SIZE,2*TILE_SIZE))
        W  = pygame.transform.scale(images["W-"],(2*TILE_SIZE,2*TILE_SIZE))
        SW  = pygame.transform.scale(images["SW"],(2*TILE_SIZE,2*TILE_SIZE))
        SE  = pygame.transform.scale(images["SE"],(2*TILE_SIZE,2*TILE_SIZE))
  
        for y in range(0,TILE_SIZE*2*7,TILE_SIZE*2):
            surface.blit(W,(0,y))
            surface.blit(E,(TILE_SIZE*2,y))

        surface.blit(SW,(0,TILE_SIZE*2*7))
        surface.blit(SE,(TILE_SIZE*2,TILE_SIZE*2*7))

    def get_font(self,text, size, color):
        # Get UI Font
        font = pygame.font.Font("resources/Atarian.ttf", size)
        # Render text
        return font.render(text, True, color)

    def target_boarder(self,images):
        surface = pygame.Surface((2*TILE_SIZE,2*TILE_SIZE))
        surface.blit(images["NW"],(0,0))
        surface.blit(images["NE"],(TILE_SIZE,0))
        surface.blit(images["SW"],(0,TILE_SIZE))
        surface.blit(images["SE"],(TILE_SIZE,TILE_SIZE))
        return surface
    
    def set_token(self,token):
        token = self.images[token]
        self.token.image = pygame.transform.scale(token,(2*TILE_SIZE-MARGIN*4,2*TILE_SIZE-MARGIN*4))
    
    def update(self):
        self.sprite_group.update()
    
    def draw(self,screen):
        screen.blit(self.surface,(BOARD_WIDTH,0))
        self.sprite_group.draw(screen)
