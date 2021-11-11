import pygame

class Obstacles(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load("obstacles.png").convert_alpha()
        img.set_colorkey((255, 255, 255))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movey = 0

    def move(self, y):
        self.movey +=y     

    def update(self):
        self.rect.y = self.rect.y + self.movey

    def falling(self, key):
        if key == pygame.K_q:
            self.move(5)
        if key == pygame.K_a:
            self.move(10)
        if key == pygame.K_z:
            self.move(15)        