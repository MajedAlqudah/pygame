import pygame
import Settings as s
from pygame.sprite import Sprite

class HeartIcon(Sprite):
    def __init__(self):
        super(HeartIcon, self).__init__()
        self.img_heart_01 = pygame.image.load("Assists/heart.png").convert_alpha()
        self.img_heart_02 = pygame.image.load("Assists/heart1.png").convert_alpha()
        self.img_heart_03 = pygame.image.load("Assists/heart2.png").convert_alpha()
        self.img_heart_04 = pygame.image.load("Assists/heart3.png").convert_alpha()
        self.img_heart_05 = pygame.image.load("Assists/heart4.png").convert_alpha()
        # scaling the imgs
        self.img_heart_01= pygame.transform.scale(self.img_heart_01, (30, 30))
        self.img_heart_02 = pygame.transform.scale(self.img_heart_02, (30, 30))
        self.img_heart_03 = pygame.transform.scale(self.img_heart_03, (30, 30))
        self.img_heart_04 = pygame.transform.scale(self.img_heart_04, (30, 30))
        self.img_heart_05 = pygame.transform.scale(self.img_heart_05, (30, 30))
        self.anim_list = [self.img_heart_01, self.img_heart_02, self.img_heart_03, self.img_heart_03, self.img_heart_04, self.img_heart_05]
        self.anim_index = 0
        self.max_index = len(self.anim_list)-1
        self.max_duration = 4
        self.frame_dur = self.max_duration
        self.image = self.anim_list[self.anim_index]
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 30

    def update(self):
        # Handling animation
        if self.frame_dur == 0:
            self.anim_index += 1
            if self.anim_index > self.max_index:
                self.anim_index = 0
            self.image = self.anim_list[self.anim_index]
            self.frame_dur = self.max_duration
        self.frame_dur -= 1




