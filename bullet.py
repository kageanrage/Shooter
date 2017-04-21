import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, player, screen, settings):

        super().__init__()
        self.screen = screen

        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)

        self.rect.centerx = player.rect.centerx
        self.rect.bottom = player.rect.top    # make the bullet appear at the top of where the player is

        self.color = (0, 0, 30)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        if self.rect.y >= 0:
            self.rect.y -= 1
