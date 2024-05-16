import pygame
import Settings as s
from pygame.sprite import Sprite


class Score(Sprite):
    def __init__(self):
        super(Score, self).__init__()
        # setting the font
        self.value = 0
        self.font_size = 40
        self.color = (0,0,0)
        self.font = pygame.font.Font("Assists/computer-says-no.ttf", self.font_size)
        self.image = self.font.render(str(f'Score: {self.value}'), False, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 0

    def update(self):
        pass


    def update_socre(self, value):
        self.value += value
        # we need new image bcs we updated the score value
        self.image = self.font.render(str(f'Score: {self.value}'), False, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 0

    def reset(self):
        self.value = 0
        self.image = self.font.render(str(f'Score: {self.value}'), False, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 0






