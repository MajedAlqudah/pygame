'''''''''
Name : Majed Jameel Alqudah
ID : 146969
Project : FlappyShooter
'''''''''
import pygame
import sys
import math
from Ship import Ship
import game_fun as fun
from pygame.sprite import Sprite
import Settings as s
from enemy_spawner import EnemySpawner
from Score import Score
from Alert_box import AlertBox
from Menu import Menu


def run_game():
    pygame.mixer.pre_init(44100,-16,4,512)
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    game_over = False  # Add a game over flag
    game_over_music_ = False

    # music Setting
    key_sound = pygame.mixer.Sound("Assists/pew.mp3")
    key_sound.set_volume(0.3)
    pygame.mixer.music.load("Assists/theme.mp3")
    pygame.mixer.music.set_volume(0.03)
    pygame.mixer.music.play(-1)
    game_over_music = pygame.mixer.Sound("Assists/gameover.mp3")
    game_over_music.set_volume(0.5)

    # Display setup
    display = pygame.display.set_mode((s.screen_width, s.screen_height))
    pygame.display.set_caption("FlappyShooter")
    icon_image=pygame.image.load("Assists/icon.png")
    pygame.display.set_icon(icon_image)
    fps = 60
    clock = pygame.time.Clock()
    running = True
    # Objects setup
    msg = "Game Over !!"
    alertbox= AlertBox(msg)
    alertbox_group = pygame.sprite.Group()
    player = Ship(display)
    sprit_group = pygame.sprite.Group()
    sprit_group.add(player)
    enemy_spawner= EnemySpawner()
    score = Score()
    score_group = pygame.sprite.Group()
    score_group.add(score)

    # load bg
    background = pygame.image.load("Assists/skyee.png").convert()
    bg_width=background.get_width()
    #bg_rect=background.get_rect()

    # setting variables
    scroll=0
    tiles=math.ceil(s.screen_width / bg_width)+1

    # Create a Menu instance
    menu = Menu()

    while running:
        # If the game hasn't started yet, show the menu
        if not menu.is_game_started:
            menu.handle_events()
            display.fill((0, 0, 0))  # Clear the screen
            menu.render(display)
            pygame.display.flip()

        # If the game has started, run the game loop
        else:
            # tick clock to maintain the frame rate
            clock.tick(fps)
            # handle event to run the game :)
            fun.check_event(player, key_sound)
            # making scrolling background
            for i in range(0, tiles):
                display.blit(background, (i * bg_width + scroll, 0))

                # bg_rect.x=i * bg_width + scroll
                # pygame.draw.rect(display,(0,255,0),bg_rect,1)

            # scroll background
            scroll -= 8
            # reset scroll
            if abs(scroll) > bg_width:
                scroll = 0

            # update the objects
            sprit_group.update()
            enemy_spawner.update()
            score_group.update()
            alertbox_group.update()

            # check  collision
            collieded = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemies_group, True, False)
            for bullet, enemy in collieded.items():
                enemy[0].get_hit()
                score.update_socre(enemy[0].point_value)
            collieded1 = pygame.sprite.groupcollide(sprit_group, enemy_spawner.enemies_group, False, True)
            for player, enemy in collieded1.items():
                if not player.is_invincible:
                    enemy[0].get_hit()
                    enemy[0].hp = 0
                    player.get_hit()

            # Check for gameOver
            if not player.is_alive:
                enemy_spawner.clear_enemies()
                alertbox_group.add(alertbox)
                game_over = True
                # Stop the current music
                pygame.mixer.music.stop()

                # Play the game over music
                game_over_music.play()
                game_over_music_ = True
            # Check for mouse click to restart the game
            if game_over:

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Check if the mouse click is within the boundaries of the "Game Over" message
                        if alertbox.rect.collidepoint(event.pos):
                            # Reset the game
                            game_over = False
                            game_over_music.stop()  # Stop game over music
                            game_over_music_ = False
                            player.reset()
                            enemy_spawner.reset()
                            score.reset()
                            alertbox_group.empty()  # Remove the game over message

                            pygame.mixer.music.load("Assists/theme.mp3")  # reset the music
                            pygame.mixer.music.set_volume(0.03)
                            pygame.mixer.music.play(-1)
            #Check if the enemy passed the boarder
            for enemy in enemy_spawner.enemies_group:
                 if enemy.rect.x <= -100:
                     player.death()

            # render the screen

            enemy_spawner.enemies_group.draw(display)
            player.bullets.draw(display)
            sprit_group.draw(display)
            player.hp_group.draw(display)
            player.icons_group.draw(display)
            score_group.draw(display)
            player.lives_group.draw(display)
            alertbox_group.draw(display)
            pygame.display.update()


run_game()
