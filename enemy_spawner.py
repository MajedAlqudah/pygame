import pygame
from enemy import *
import random
import Settings as s
class EnemySpawner:
    def __init__(self):
        self.enemies_group=pygame.sprite.Group()
        self.spawn_timer= random.randrange(60,120)

    def update(self):
        self.enemies_group.update()
        if self.spawn_timer == 0:
            self.spawn_enemy()
            self.spawn_timer = random.randrange(60,120)
        else:
            self.spawn_timer -= 1
        # Remove enemies that have gone off the left side of the screen
        for enemy in self.enemies_group.copy():
            if enemy.rect.x <= -101:

                    self.enemies_group.remove(enemy)





    def spawn_enemy(self):
        enemy_type = random.choice([Enemy, Enemy2, Enemy3])  # Choose a random enemy type
        new_enemy = enemy_type()  # Create an instance of the chosen enemy type
        new_enemy.flip_images()  # Flip the images if needed
        self.spawn_timer = random.choice([120,180,240])
        self.enemies_group.add(new_enemy)
        # Set the x-coordinate to the right of the screen
        new_enemy.rect.x = s.screen_width

        # Randomize the y-coordinate within the visible screen area
        new_enemy.rect.y = random.choice([50,150,250,350,450])

    def clear_enemies(self):
        for enemy in self.enemies_group:
            enemy.kill()

    def reset(self):
        self.enemies_group.empty()  # Clear all existing enemies
        self.spawn_timer = random.randrange(60, 120)

