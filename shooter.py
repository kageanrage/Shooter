# Shooter.py - a self-designed baddie shooting game

# next steps:

import pygame

from player import Player
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from audio import Audio
from button import Button
from messages import Result, LevelUp


def run_game():
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)  # setup mixer to avoid sound lag
    pygame.display.set_caption("Get Trumped")
    audio = Audio()
    settings = Settings()
    stats = GameStats(settings)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    player = Player(screen)
    bullets = Group()
    baddies = Group()
    sb = Scoreboard(settings, screen, stats)
    play_button = Button(settings, screen, "Play")
    end_msg = Result(settings, screen, stats, play_button)
    level_up_msg = LevelUp(settings, screen, stats)
    addbaddie = pygame.USEREVENT + 1
    pygame.time.set_timer(addbaddie, settings.baddie_interval)

    while True:
        if not stats.game_active:
            gf.check_events_whilst_inactive(player, bullets, baddies, stats, play_button)
            gf.update_screen_whilst_inactive(screen, sb, stats, end_msg, play_button)
        if stats.game_active:
            gf.check_events(player, screen, settings, bullets, baddies, audio, addbaddie, stats, level_up_msg)
            gf.no_longer_first_round(stats)   # just an inelegant flag tied to 'you're dead' message
            gf.move(player)
            gf.update_bullets(bullets)
            gf.check_bullet_collisions(baddies, bullets, stats, audio, settings, level_up_msg)
            gf.update_baddies(baddies, settings, stats)
            gf.check_baddie_player_collisions(baddies, player, stats, bullets, audio)
            gf.check_baddie_screen_bottom(screen, stats, player, bullets, baddies, audio)
            gf.update_screen(player, screen, bullets, baddies, sb, stats, level_up_msg, settings)


run_game()
