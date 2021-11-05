import pygame
from pygame import sprite
from pygame.constants import KEYDOWN
from player import Player
from obstacles import Obstacles
from pygame.locals import K_q
import random
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
screen_rect = pygame.Rect((0, 0), (worldx, worldy))
pygame.mouse.set_visible(False)
# gracz

player = Player(800, 450)

player_list = pygame.sprite.Group()
player_list.add(player)
steps = 3


obstacle = Obstacles(0, 0) 
obstacles_list = pygame.sprite.Group()
obstacles_list.add(obstacle)

# obstacles



#main

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                player.moving(event.key, steps)
                if event.key == K_q: #113 = q 
                    obstacle.falling(event.key) 
        if obstacle.rect.y > worldy:
            obstacle.rect.y = 0 - obstacle.rect.height
             
        obstacle.update()
        player.update()
        world.blit(backdrop, backdropbox)
        player_list.draw(world)
        obstacles_list.draw(world)
        pygame.display.flip()
        clock.tick(fps)
main()