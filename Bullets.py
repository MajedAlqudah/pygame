import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self):
        super(Bullet,self).__init__()
        # Scaling bullets without any image
        self.width=12
        self.hieght=6
        self.size=(self.width,self.hieght)
        self.image=pygame.Surface(self.size)
        self.color=(255,200,100)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.vel_x=8
        self.vel_y=0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y




