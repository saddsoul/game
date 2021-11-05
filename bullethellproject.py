import pygame
from pygame.constants import KEYDOWN

#zmienne

worldx = 1600
worldy = 900
fps = 60
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255) 

#klasy

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("ship3.png").convert()
        img.convert_alpha()
        img.set_colorkey((255, 255 ,255))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        
    def move(self, x, y):
        self.movex += x
        self.movey += y 
           
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.rect.clamp_ip(screen_rect)
    
    def shoot(self):
        self.bullets
        
    def moving(self,key):
        if key == pygame.K_RIGHT:
            player.move(steps, 0)
        if key == pygame.K_LEFT:
            player.move(-steps, 0)
        if key == pygame.K_UP:
            player.move(0, -steps)
        if key == pygame.K_DOWN:
            player.move(0, steps)

class Bullets(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        
        self.images = []
        bulletimage = pygame.image.load("bullet.png").convert()
        self.images.append(bulletimage)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        

# Setup

pygame.display.set_caption("bullethellproject")
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load("background.jpg") 
backdropbox = world.get_rect()
screen_rect = pygame.Rect((0, 0), (1600, 900))
pygame.mouse.set_visible(False)
# gracz

player = Player()
player.rect.x = 800
player.rect.y = 450
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 3



#bullets

bullets = Bullets()
bullets.rect.x = 0
bullets.rect.y = 0
bullets_list = pygame.sprite.Group()
bullets_list.add(bullets)

#main

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                player.moving(event.key)
                             
        player.update()
        bullets.update()
        world.blit(backdrop, backdropbox)
        player_list.draw(world)
        pygame.display.flip()
        clock.tick(fps)
main()