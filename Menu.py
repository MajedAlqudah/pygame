# Create a Menu class
import pygame
import Settings as s
import sys

class Menu:
    def __init__(self):
        self.image = pygame.image.load("Assists/menu_00000.png")
        self.start_button = pygame.Rect(s.screen_width // 2 - 100, s.screen_height // 2 - 25, 200, 50)
        self.font = pygame.font.Font(None, 36)
        self.is_game_started = False

    def render(self, screen):
        screen.blit(self.image, (0 ,0))



    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.collidepoint(event.pos):
                    self.is_game_started = True