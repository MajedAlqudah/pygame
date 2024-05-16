import pygame
import sys


def check_event(player,key_sound):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        #player movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.vel_y = -player.speed
                if player.lives <= 0:
                    player.lives = 0
                    player.image = pygame.Surface((0, 0))
                else:

                    player.image=player.images[2]

            elif event.key == pygame.K_s:
                player.vel_y = +player.speed
                if player.lives <= 0:
                    player.lives = 0
                    player.image = pygame.Surface((0, 0))
                else:
                    player.image = player.images[1]

            if event.key == pygame.K_SPACE:
                if player.is_alive:
                   key_sound.play()
                   player.shoot()



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.vel_y = 0
                if player.lives <= 0:
                    player.lives = 0
                    player.image = pygame.Surface((0, 0))
                else:

                    player.image = player.images[0]
            elif event.key == pygame.K_s:
                player.vel_y = 0
                if player.lives <= 0:
                    player.lives = 0
                    player.image = pygame.Surface((0, 0))
                else:

                    player.image = player.images[0]







