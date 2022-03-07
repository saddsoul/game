import pygame
from pygame import sprite
from pygame.constants import KEYDOWN
from player import Player
from obstacles import Obstacles
from pygame.locals import K_q
import random
import time
from bullets import Bullets

# Setup

timer = 0
worldx = 1600
worldy = 900
fps = 144
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

# player

player = Player(800, 450)       #spawning player at coordinates
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 3

# obstacles 

obstacles_list = pygame.sprite.Group() # creating groups for multiple objects to update them simultaneously
bullets_list = pygame.sprite.Group()

#main
def spawning_bullets(key):      # function for spawning and shooting bullets - cons - cant address a single bullet?
    if key == pygame.K_z:
        pewpew = Bullets(player.rect.x, player.rect.y)
        bullets_list.add(pewpew)
        pewpew.shooting(pygame.K_SPACE)

def spawning_obstacles():           # function for repeated spawning of obstacles - cons - cant address a single obstacle at a time?
    y = Obstacles(random.randint(0,1600), 0)
    obstacles_list.add(y)
    y.falling(K_q)  

def highscore_display(x, y):        # function for highscore saving and displaying current score
    score = font.render("Score :" + str(timer), True, (255, 255, 255))
    world.blit(score, (x, y))
    hs_file = open("highscores.txt","r+")
    highscore = font.render("Highscore :" + str(hs_file.read()), True, (255, 255, 255))
    world.blit(highscore, (x+100, y+100))
    hs_file.close()
    
def main():
    running = True
    while running:
        
        global timer
        timer = timer + 1   #timer for spawning obstacles + primitive way to keep track of a highscore 
        
        if timer % 8 == 0:
            spawning_obstacles()    #spawning a lot of obstacles every second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN: #player movement 
                player.moving(event.key, steps)
                spawning_bullets(event.key)

        if pygame.sprite.spritecollide(player, obstacles_list, True):    # collision detection that simultaneously ends the game and saves highscore to a txt file       
            hs_file = open("highscores.txt","r+")
            highscore = hs_file.read()
            if timer>int(highscore):
                hs_file.seek(0)
                hs_file.truncate(0)
                hs_file.write(str(timer))
            hs_file.close()
            running = False

        if pygame.sprite.groupcollide(obstacles_list, bullets_list, True, True): # bullet-obstacle collision detection, collision=removal from list
            timer = timer - 500 #punishing players for shooting

        bullets_list.update()
        obstacles_list.update()             #updating sprites
        player.update()
        world.blit(backdrop, backdropbox)    #draws backdrop file background onto the backdropbox (game rect)
        highscore_display(10, 10)       
        player_list.draw(world)             #drawning sprites
        obstacles_list.draw(world)
        bullets_list.draw(world)
        pygame.display.flip()               
        clock.tick(fps)
main()