import pygame
from pygame.sprite import Sprite
from Bullets import Bullet
import Settings as s
from enemy import *
from Hp import Hp
from heart_icon import HeartIcon
from lives import Lives


class Ship(Sprite):
    def __init__(self,display):
        # Needed settings for the boarders
        self.screen=display
        self.screen_rect=self.screen.get_rect()

        super(Ship,self).__init__()
        #load player image / used convert method to reduce the lag
        self.images=[pygame.image.load("Assists/vero1.png"),pygame.image.load("Assists/vero2.png").convert_alpha(),pygame.image.load("Assists/vero3.png").convert_alpha()]
        self.images = [pygame.transform.scale(image, (image.get_width() // 6, image.get_height() // 6)) for image in self.images]
        self.image=self.images[0]
        # Setting the bullets obj
        self.bullets=pygame.sprite.Group()
        #settings for the player
        self.max_hp=3
        self.player_hp = self.max_hp
        self.lives = 3
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height + 170
        self.rect.centerx = 100
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 6
        # HUD settings
        self.hp=Hp(self.player_hp)
        self.hp_group= pygame.sprite.Group()
        self.hp_group.add(self.hp)
        self.heart_icon = HeartIcon()
        self.icons_group = pygame.sprite.Group()
        self.icons_group.add(self.heart_icon)
        # lives counter settings
        self.live = Lives(self.lives)
        self.lives_group = pygame.sprite.Group()
        self.lives_group.add(self.live)
        # respawn shield
        self.is_invincible = False
        self.max_inv_timer = 60  # inv for 1 sec
        self.inv_timer = 0
        # gameover settings
        self.is_alive = True




    def update(self):
        self.bullets.update()
        self.hp_group.update()
        self.icons_group.update()
        self.lives_group.update()
        # Removing bullets from memory
        for bullet in self.bullets:
            if bullet.rect.x >= 1500:
                self.bullets.remove(bullet)

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # Ensure the ship stays within the screen boundaries
        # Top boundary
        if self.rect.top < 45:
            self.rect.top = 45
        # Bottom boundary
        elif self.rect.bottom > self.screen_rect.height - 40:
            self.rect.bottom = self.screen_rect.height - 40
        # Update HUD position relative to the ship
        self.hp.rect.x = self.rect.x + -10# You may adjust the offset as needed
        self.hp.rect.y = self.rect.y + self.rect.height -100 # Adjust the vertical offset as needed
        self.hp.update()
        self.heart_icon.rect.x = self.rect.x - 25
        self.heart_icon.rect.y = self.rect.y + self.rect.height - 90
        # Check for invincibility
        if self.inv_timer > 0 :
            self.inv_timer -= 1
        else:
            if self.is_alive:
               self.is_invincible = False



    def shoot(self):
        if self.is_alive:
            new_bullet = Bullet()
            new_bullet.rect.x = self.rect.x + (self.rect.width // 2)
            new_bullet.rect.y = self.rect.y + (self.rect.height // 2)
            self.bullets.add(new_bullet)

    def get_hit(self):
        if self.is_alive:
          self.player_hp-=1
          self.hp.decrease_hp()
          # after getting hit 3 times the player will lose a live
          if self.player_hp <=0:
            self.player_hp=0
            self.death()
          print("hp:",self.player_hp)

    def death(self):
        self.lives-=1
        print("lives:",self.lives)
        if self.lives<=0:
            self.lives=0
            self.is_alive = False
            self.image = pygame.Surface((0, 0))
        # after the player lose a life the hp par will resest
        self.player_hp=self.max_hp
        self.hp.reset_hp()
        self.live.decrement_lives()
        # recenter the player after he loses a life
        self.rect.y = self.rect.height + 170
        # set a shield for the player
        self.is_invincible = True
        self.inv_timer = self.max_inv_timer

    def reset(self):
        # Reset the ship's position
        self.rect.y = self.rect.height + 170
        self.rect.centerx = 100
        # Reset health, lives, and invincibility
        self.player_hp = self.max_hp
        self.lives = 3
        self.is_invincible = False
        self.inv_timer = 0
        self.is_alive = True
        self.image = self.images[0]  # Reset the ship's image

        # Reset HUD elements
        self.hp.reset_hp()
        self.live.reset_lives()











