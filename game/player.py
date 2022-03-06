import pygame

from logic import Graph

class Player(pygame.sprite.Sprite):
    """A player object for the game """

    walls = [[]]
    adjacency_list = Graph(16*16)

    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("Resources/AI.png").convert_alpha()
        self.rect = self.image.get_rect()

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.left -= 2
        if key[pygame.K_RIGHT]:
            self.rect.right += 2
        if key[pygame.K_UP]:
            self.rect.top -= 2
        if key[pygame.K_DOWN]:
            self.rect.bottom += 2

    def update(self):
        self.input()
        self.collision()
    
    def destroy(self):
        self.kill()

    def collision(self):
        collision_tolerence = 3

        def hitLeft(wall):
            if abs(wall.left - self.rect.right) < collision_tolerence:
                print("HIT")
        
        def hitRight(wall):
            if abs(wall.left - self.rect.left) < collision_tolerence:
                print("HIT")


        if self.rect.colliderect(self.walls[0][5]):
            wall = self.walls[0][5]
            hitLeft(wall)
            hitRight(wall)
                
        if self.rect.colliderect(self.walls[0][12]):
            wall = self.walls[0][12]
            hitLeft(wall)
            hitRight(wall)
    
        if self.rect.colliderect(self.walls[1][7]):
            wall = self.walls[1][7]
            hitLeft(wall)

       

           
            #print("player",self.rect.right)
            #print("box",self.myrect.left)
                
   
    def set_walls(self,walls):
        self.walls = walls    
        


        