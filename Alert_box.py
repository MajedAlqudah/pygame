import pygame
from pygame.sprite import Sprite
import Settings as s

class AlertBox(Sprite):
    def __init__(self, msg):
        super(AlertBox, self).__init__()
        self.font_size = 70
        self.color = (255, 0, 0)
        self.font = pygame.font.Font("Assists/computer-says-no.ttf", self.font_size)
        self.msg = msg
        self.image = self.font.render(self.msg, 0, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = s.screen_width // 2 - self.rect.width // 2
        self.rect.y = s.screen_height // 2 - self.rect.height// 2

        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

