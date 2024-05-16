import pygame
from pygame.sprite import Sprite
import Settings as s
from heart_icon import HeartIcon



class Hp(Sprite):
    def __init__(self,player_hp):
        super(Hp, self).__init__()
        self.max_hp = player_hp
        self.player_hp = player_hp
        self.orginal_image = pygame.image.load("Assists/par3.png").convert_alpha()
        self.image = self.orginal_image
        self.image = pygame.transform.scale(self.image, (90, 50))
        self.max_width = self.image.get_width()


        self.rect = self.image.get_rect()
        self.rect.y= 0
        self.rect.x= 0

        self.vel_x= 0
        self.vel_y= 0


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


    def decrease_hp(self):
        self.player_hp-=1
        # scalling the image after the damage
        self.image = pygame.transform.scale(self.orginal_image,(self.max_width* self.player_hp // self.max_hp,self.rect.height))
        x=self.rect.x
        y=self.rect.y
        self.rect= self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def reset_hp(self):
        self.player_hp = self.max_hp
        self.image = pygame.transform.scale(self.orginal_image,
                                             (self.max_width * self.player_hp // self.max_hp, self.rect.height))
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        self.reset_hp()

