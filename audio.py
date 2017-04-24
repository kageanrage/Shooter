import pygame
import os
import random


class Audio:
    def __init__(self):
        self.shot = pygame.mixer.Sound(os.path.join('sound','shot.wav'))  # load sound
        self.baddie_ded = pygame.mixer.Sound(os.path.join('sound','baddie_ded.wav'))  # load sound
        self.player_ded = pygame.mixer.Sound(os.path.join('sound','player_ded.wav'))  # load sound
        self.baddie_spawn = pygame.mixer.Sound(os.path.join('sound','baddie_spawn.wav'))  # load sound


    def play_trump_soundbite(self):
        filenames = ['african-americans-love-me', 'are-you-running', 'but-mr-trump-youre-not-a-nice-person', 'democracy-we-cant-have-it-anymore', 'he-got-schlonged', 'holy-mack-eral', 'i-dont-care', 'Swearing-hes-a-pussy', 'Swearing-listen-you-motherfuckers', 'who-is-the-best-president']
        trump = pygame.mixer.Sound(os.path.join('sound', 'trump_audio', '{}.wav'.format(random.choice(filenames))))
        trump.play()

