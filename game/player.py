import pygame

class Player(pygame.sprite.Sprite):
    """A player object for the game """
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
        
    def isCollision(self) -> bool:
        return self.rect.colliderect

    def update(self):
        self.input()
    
    def destroy(self):
        self.kill()