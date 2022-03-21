import pygame

from game.constants import BOARD_WIDTH, MARGIN, TILE_SIZE, UI_HEIGHT, UI_WIDTH
from game.images import Images
from game.board import Board

class Button(pygame.sprite.Sprite):
    def __init__(self, pos,width,height,first_color,second_color,first_text,second_text,size,callback):
        super().__init__()
        # Attributes
        self.font =  pygame.font.Font("resources/Atarian.ttf", size)
        self.width = width
        self.height = height
        self.background_1 = first_color
        self.background_2 = second_color
        self.text_1 = first_text
        self.text_2 = second_text
        self.callback = callback
        self.is_clicked = False
        # Sprite definitions
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=pos)
    
    def draw_button(self,text,background_color,text_color):
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0,0,1))
        self.image.set_colorkey((0,0,1))
        image = self.font.render(text, True, text_color)
        rect = pygame.Rect(
            self.image.get_width()//8,
            self.image.get_height()//8,
            self.width-self.width//4,
            self.height-self.height//4,
        )
        pygame.draw.rect(self.image,background_color, rect, border_radius = 10)
        self.image.blit(image,(
            self.image.get_width()//2-image.get_width()//2,
            self.image.get_height()//2-image.get_height()//2)
        )

    def handle_event(self, event):
        self.draw_button(self.text_1,(0,0,1),'White')
     
        if not event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.draw_button(self.text_1,'Red','Black')
        elif event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()):
            if event.button == 1:
                self.draw_button(self.text_2,'Green','Black')
                if self.rect.collidepoint(event.pos):
                    self.callback()

class Counter(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.font =  pygame.font.Font("resources/Atarian.ttf", 90)
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
    def __init__(self,board:Board):
        
        self.board = board

        self.surface = pygame.Surface((UI_WIDTH,UI_HEIGHT))
        self.surface.fill('White')
        
        self.sprite_group = pygame.sprite.Group()
        
        self.images = Images()
        
        # Images for UI 
        target_text = self.get_font("Target", 40, 'White')
        player_text = self.get_font("Player      AI  ", 32, 'White')
        moves_text = self.get_font("Moves counter", 30, 'White')
        boarder = self.target_boarder(self.images)
        knucles = pygame.image.load("resources/knuckles.png")
        knucles = pygame.transform.scale(knucles,(TILE_SIZE,TILE_SIZE))
        robot = pygame.image.load("resources/robot.png")
        ai = pygame.image.load("resources/robot.png")
        
        # Create background
        self.background(self.surface,self.images)
        # Draw images on surface
        for x in range(4):
            if x == 0:
                text = self.get_font(str(x+1),25,'White')
                self.surface.blit(text,(x*45+31,10))
                pygame.draw.circle(self.surface, 'Red', (x*45+33,50),10)
            if x == 1:
                text = self.get_font(str(x+1),25,'White')
                self.surface.blit(text,(x*45+28,10))
                pygame.draw.circle(self.surface, 'Blue', (x*45+33,50),10)
            if x == 2:
                text = self.get_font(str(x+1),25,'White')
                self.surface.blit(text,(x*45+27,10))
                pygame.draw.circle(self.surface, 'Green', (x*45+33,50),10)
            if x == 3:
                text = self.get_font(str(x+1),25,'White')
                self.surface.blit(text,(x*45+26,10))
                pygame.draw.circle(self.surface, 'Yellow', (x*45+33,50),10)

        self.surface.blit(target_text,(self.surface.get_width()//2-target_text.get_width()//2,60))
        self.surface.blit(boarder,(self.surface.get_width()//2-boarder.get_width()//2,110))
        self.token = Token(BOARD_WIDTH+2*MARGIN+self.surface.get_width()//2-boarder.get_width()//2,120)

        self.surface.blit(player_text,(self.surface.get_width()//2-player_text.get_width()//2,210))
        self.surface.blit(knucles,(self.surface.get_width()//4-knucles.get_width()//2,240))        
        x = self.surface.get_width()//2+self.surface.get_width()//4
        self.surface.blit(ai,(x-ai.get_width()//2,245))


        x = BOARD_WIDTH-5+self.surface.get_width()//2+self.surface.get_width()//4
        width = 100
        height = 25
        pos = (x-width//2,310)
        self.bfs_button = Button(pos,width,height,'Red','Green',"BFS","OK",30,board.bfs)
        pos = (x-width//2,360)
        self.astar_button = Button(pos,width,height,'Red','Green',"A-Star","OK",30,board.a_star)
        
        self.surface.blit(moves_text,(self.surface.get_width()//2-player_text.get_width()//2,400))
        self.counter = Counter(BOARD_WIDTH-18+self.surface.get_width()//2,430)

        x = BOARD_WIDTH+self.surface.get_width()//2
        width = 120
        height = 50
        pos = (x-width//2,UI_HEIGHT-height-MARGIN*2)
        self.reset_button = Button(pos,width,height,'Red','Green',"Reset","OK",30,self.reset)

        # add sprites
        self.sprite_group.add(self.token)
        self.sprite_group.add(self.reset_button)
        self.sprite_group.add(self.bfs_button)
        self.sprite_group.add(self.astar_button)
        self.sprite_group.add(self.counter)
    
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
    
    def set_token(self):
        token = self.images[self.board.token]
        self.token.image = pygame.transform.scale(token,(2*TILE_SIZE-MARGIN*4,2*TILE_SIZE-MARGIN*4))

    def reset(self):
        self.board.players[0].reset()
        self.board.players[1].reset()  
        self.board.players[2].reset()  
        self.board.players[3].reset()      
        self.board.history = []
           
    def events(self,event):
        self.reset_button.handle_event(event)
        self.bfs_button.handle_event(event)
        self.astar_button.handle_event(event)

    def update(self):
        self.sprite_group.update()
        self.set_token()
        self.counter.number = len(self.board.history)
    
    def draw(self,screen):
        screen.blit(self.surface,(BOARD_WIDTH,0))
        self.sprite_group.draw(screen)
