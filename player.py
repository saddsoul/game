import pygame
from pygame.constants import KEYDOWN
import math


screen_rect = pygame.Rect((0, 0), (1600, 900))

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load("ship3.png").convert_alpha()
        img.set_colorkey((255, 255 ,255))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movex = 0
        self.movey = 0
        
    def move(self, x, y):
        self.movex += x
        self.movey += y 
           
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.rect.clamp_ip(screen_rect)
        
    def moving(self, key, steps):
        if key == pygame.K_RIGHT:
            if self.movex < 0:
                self.movex = 0
            self.move(steps, 0)
        if key == pygame.K_LEFT:
            if self.movex > 0:
                self.movex = 0
            self.move(-steps, 0)
        if key == pygame.K_UP:
            if self.movey > 0:
                self.movey = 0
            self.move(0, -steps)
        if key == pygame.K_DOWN:
            if self.movey < 0:
                self.movey = 0
            self.move(0, steps)

    