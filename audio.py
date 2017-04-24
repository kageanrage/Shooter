import pygame
import os
import random


class Audio:
    def __init__(self):
        self.shot = pygame.mixer.Sound(os.path.join('sound','blip1.wav'))  # load sound
        self.baddie_ded = pygame.mixer.Sound(os.path.join('sound','baddie_ded.wav'))  # load sound
        self.player_ded = pygame.mixer.Sound(os.path.join('sound', 'trump_audio', 'donald-trump-is-a-genius.wav'))  # load sound
        self.baddie_spawn = pygame.mixer.Sound(os.path.join('sound','baddie_spawn.wav'))  # load sound

        self.shot.set_volume(0.1)
        self.baddie_ded.set_volume(0.1)
        self.player_ded.set_volume(1)
        self.baddie_spawn.set_volume(0.1)

    def play_trump_soundbite(self):
        filenames = ['african-americans-love-me', 'are-you-running', 'but-mr-trump-youre-not-a-nice-person', 'democracy-we-cant-have-it-anymore', 'he-got-schlonged', 'holy-mack-eral', 'i-dont-care', 'Swearing-hes-a-pussy', 'Swearing-listen-you-motherfuckers', 'who-is-the-best-president']
        trump = pygame.mixer.Sound(os.path.join('sound', 'trump_audio', '{}.wav'.format(random.choice(filenames))))
        trump.set_volume(1)
        trump.play()

