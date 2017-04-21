import pygame
import os


class Audio:
    def __init__(self):
        self.shot = pygame.mixer.Sound(os.path.join('sound','shot.wav'))  # load sound
        self.baddie_ded = pygame.mixer.Sound(os.path.join('sound','baddie_ded.wav'))  # load sound
        self.player_ded = pygame.mixer.Sound(os.path.join('sound','player_ded.wav'))  # load sound
        self.baddie_spawn = pygame.mixer.Sound(os.path.join('sound','baddie_spawn.wav'))  # load sound
