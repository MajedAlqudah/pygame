import pygame
import Settings as s
from pygame.sprite import Sprite
import random
import pygame.time

class Enemy(Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.images=[pygame.image.load("Assists/bluebird1.png"),pygame.image.load("Assists/bluebird2.png")]
        self.images = [pygame.transform.scale(image, (60, 45) )for image in
                       self.images]
        self.image = self.images[0]
        self.hp = 2
        self.snd_hit = pygame.mixer.Sound("Assists/hit.mp3")
        self.snd_hit.set_volume(0.3)


        self.rect= self.image.get_rect()
        self.vel_x= -3
        self.vel_y=0
        self.animation_speed = 100 # Adjust this value to control animation speed
        self.animation_index = 0  # Current frame of animation
        self.last_update = pygame.time.get_ticks()  # Time since last frame change
        # score things.. :)
        self.point_value = 1
    def update(self):
        # Handle animation
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.animation_index = (self.animation_index + 1) % len(self.images)
            self.image = self.images[self.animation_index]

        self.rect.x += self.vel_x
        self.rect.y +=self.vel_y

    def flip_images(self):
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.flip(self.images[i], True, False)

    def get_hit(self):
        self.snd_hit.play()
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()

class Enemy2(Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()
        self.images = [pygame.image.load("Assists/yellow1.png"), pygame.image.load("Assists/yellow2.png")]
        self.images = [pygame.transform.scale(image, (60, 45)) for image in
                           self.images]
        self.image = self.images[0]
        self.hp = 1
        self.snd_hit = pygame.mixer.Sound("Assists/hit.mp3")
        self.snd_hit.set_volume(0.3)

        self.rect = self.image.get_rect()
        self.vel_x = -5
        self.vel_y = 0
        self.animation_speed = 100 # Adjust this value to control animation speed
        self.animation_index = 0  # Current frame of animation
        self.last_update = pygame.time.get_ticks()  # Time since last frame change
        # score things.. :)
        self.point_value = 1
    def update(self):
        # Handle animation
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.animation_index = (self.animation_index + 1) % len(self.images)
            self.image = self.images[self.animation_index]

        self.rect.x += self.vel_x
        self.rect.y +=self.vel_y

    def flip_images(self):
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.flip(self.images[i], True, False)

    def get_hit(self):
        self.snd_hit.play()
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()

class Enemy3(Sprite):
    def __init__(self):
        super(Enemy3, self).__init__()
        self.images = [pygame.image.load("Assists/dizzybird2.png"), pygame.image.load("Assists/dizzybird1.png")]
        self.images = [pygame.transform.scale(image, (60, 45)) for image in
                           self.images]
        self.image = self.images[0]
        self.hp=3
        self.snd_hit= pygame.mixer.Sound("Assists/hit.mp3")
        self.snd_hit.set_volume(0.3)

        self.rect = self.image.get_rect()
        self.vel_x = -2
        self.vel_y = 0
        self.animation_speed = 100 # Adjust this value to control animation speed
        self.animation_index = 0  # Current frame of animation
        self.last_update = pygame.time.get_ticks()  # Time since last frame change
        # score things.. :)
        self.point_value = 1



    def update(self):
        # Handle animation
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.animation_index = (self.animation_index + 1) % len(self.images)
            self.image = self.images[self.animation_index]

        self.rect.x += self.vel_x
        self.rect.y +=self.vel_y

    def flip_images(self):
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.flip(self.images[i], True, False)

    def get_hit(self):
        self.snd_hit.play()
        self.hp -= 1
        if self.hp <= 0 :
            self.destroy()


    def destroy(self):
        self.kill()