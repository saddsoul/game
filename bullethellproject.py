import pygame
from pygame import sprite
from pygame.constants import KEYDOWN
from player import Player
from obstacles import Obstacles
from pygame.locals import K_q
import random
import time

# Setup

timer = 0
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
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)

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

obstacles_list = pygame.sprite.Group()

#main
def spawning_obstacles():           
        y = Obstacles(random.randint(0,1600), 0)
        obstacles_list.add(y)
        y.falling(K_q)  

def highscore_display(x, y):
    score = font.render("Score :" + str(timer), True, (255, 255, 255))
    world.blit(score, (x, y))
    hs_file = open("highscores.txt","r+")
    highscore = font.render("Highscore :" + str(hs_file.read()), True, (255, 255, 255))
    world.blit(highscore, (x+100, y+100))
    hs_file.close()
    
def main():
    running = True
    while running:
        hs_file = open("highscores.txt","r+")
        global timer
        timer = timer + 1
        if timer % 8 == 0:
            
            spawning_obstacles()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                player.moving(event.key, steps)
                if event.key == K_q:
                    spawning_obstacles()

        if pygame.sprite.spritecollide(player, obstacles_list, True):            
            highscore = hs_file.read()
            if timer>int(highscore):
                hs_file.seek(0)
                hs_file.truncate(0)
                hs_file.write(str(timer))
            hs_file.close()
            running = False
    
        obstacles_list.update()
        player.update()
        world.blit(backdrop, backdropbox)
        highscore_display(10, 10)
        player_list.draw(world)
        obstacles_list.draw(world)
        pygame.display.flip()
        clock.tick(fps)
main()