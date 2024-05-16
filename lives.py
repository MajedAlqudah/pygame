import pygame
import Settings as s
from pygame.sprite import Sprite

class Lives(Sprite):
    def __init__(self, number_lives):
        super(Lives, self).__init__()
        self.num_live = number_lives
        # Ship icon Settings
        self.width = 100
        self.height = 50
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)# The plat form we gonna use to put the icon and the txt on
        self.image.set_colorkey((0, 0, 0))
        self.ship_img = pygame.image.load("Assists/heart.png").convert_alpha()
        self.ship_img = pygame.transform.scale(self.ship_img, (self.ship_img.get_width() , self.ship_img.get_height()))
        self.image.blit(self.ship_img, (0, 0))
        # TXT settings
        self.font_size = 40
        self.font_color = (255, 0, 0)
        self.font = pygame.font.Font("Assists/computer-says-no.ttf", self.font_size)
        self.lives_counter = self.font.render(f'x {self.num_live}',False, self.font_color, False)
        self.image.blit(self.lives_counter, (40, 12))
        # rectangle Settings
        self.rect = self.image.get_rect()
        self.rect.x = s.screen_width - self.rect.width




    def update(self):
        pass

    def decrement_lives(self):
        self.num_live -= 1
        # we don't want the counter goes into the negatives saw we set it to 0
        if self.num_live < 0:
            self.num_live = 0
        # Redraw the counter
        else:
            self.image = pygame.Surface(self.size)  # The plat form we gonna use to put the icon and the txt on
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(self.ship_img, (0, 0))
            self.lives_counter = self.font.render(f'x {self.num_live}', False, self.font_color, False)
            self.image.blit(self.lives_counter, (40, 12))

    def redraw_counter(self):
        self.image = pygame.Surface(self.size)
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(self.ship_img, (0, 0))
        self.lives_counter = self.font.render(f'x {self.num_live}', False, self.font_color, False)
        self.image.blit(self.lives_counter, (40, 12))
    def reset_lives(self):
        self.num_live = 3
        self.redraw_counter()









