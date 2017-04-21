import pygame
import random
from pygame.sprite import Sprite


class Baddie(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(select_image())
        self.rect = self.image.get_rect()

        self.rect.y = 0
        self.rect.x = random.randint(0, settings.screen_width - 70)

        self.y = float(self.rect.y)  # storing y position as float so it can store decimal


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, stats):
        self.y += stats.baddie_drop_speed
        self.rect.y = self.y


def select_image():
    filenames = ['Trump1', 'Trump2', 'Trump3']
    file_with_path = "images/{}.bmp".format(random.choice(filenames))
    return file_with_path
