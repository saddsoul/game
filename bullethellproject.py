import pygame
from pygame import sprite
from pygame.constants import KEYDOWN
from player import Player
from obstacles import Obstacles
from pygame.locals import K_q
import random

# Setup

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

# obstacles

obstacle1 = Obstacles(-300, 0) 
obstacles_list = pygame.sprite.Group()
obstacles_list.add(obstacle1)
obstacle2 = Obstacles(800, 0)
obstacles_list.add(obstacle2)

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
                    obstacle1.falling(event.key)
                    obstacle2.falling(event.key) 
        if obstacle1.rect.y > worldy:
            obstacle1.rect.y = 0 - obstacle1.rect.height
            obstacleposition = random.randint(-900, 100)
            obstacle1.rect.x = obstacleposition
            obstacle2position = obstacleposition + 1100
            if obstacle2.rect.y > worldy:
                obstacle2.rect.y = 0 - obstacle2.rect.height
                obstacle2.rect.x = obstacle2position  
            
        obstacle1.update()
        obstacle2.update()
        player.update()
        world.blit(backdrop, backdropbox)
        player_list.draw(world)
        obstacles_list.draw(world)
        pygame.display.flip()
        clock.tick(fps)
main()