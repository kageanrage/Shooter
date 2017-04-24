import pygame
import sys

from bullet import Bullet
from baddie import Baddie
import time


def check_events_whilst_inactive(player, bullets, baddies, stats, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(player, bullets, baddies, stats, play_button, mouse_x, mouse_y)


def check_events(player, screen, settings, bullets, baddies, audio, ADDBADDIE, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, player, screen, settings, bullets, baddies, audio, stats)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, player)
        if event.type == ADDBADDIE:
            create_baddie(screen, baddies, settings, audio)


def check_keydown_events(event, player, screen, settings, bullets, baddies, audio, stats):
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    if event.key == pygame.K_LEFT:
        player.moving_left = True
    if event.key == pygame.K_UP:
        player.moving_up = True
    if event.key == pygame.K_DOWN:
        player.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(player, screen, settings, bullets, audio)
    if event.key == pygame.K_b:
        create_baddie(screen, baddies, settings, audio)
    if event.key == pygame.K_l:
        level_up(stats, audio)


def check_keyup_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    if event.key == pygame.K_LEFT:
        player.moving_left = False
    if event.key == pygame.K_UP:
        player.moving_up = False
    if event.key == pygame.K_DOWN:
        player.moving_down = False


def move(player):
    if player.moving_right:
        if player.rect.right <= player.screen_rect.right:
            player.rect.x += 1
    if player.moving_left:
        if player.rect.left >= player.screen_rect.left:
            player.rect.x -= 1
    if player.moving_up:
        if player.rect.top >= player.screen_rect.top:
            player.rect.y -= 1
    if player.moving_down:
        if player.rect.bottom <= player.screen_rect.bottom:
            player.rect.y += 1


def fire_bullet(player, screen, settings, bullets, audio):
    new_bullet = Bullet(player, screen, settings)
    if len(bullets) < settings.max_bullets:
        bullets.add(new_bullet)
        audio.shot.play()

def update_screen(player, screen, bullets, baddies, sb, stats, end_msg, play_button):
    screen.fill((255, 255, 255))
    sb.prep_score()
    sb.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    player.blitme()
    for baddie in baddies.sprites():
        baddie.blitme()
    if not stats.game_active:
        play_button.draw_button()
        if not stats.is_first_round:
            end_msg.prep_msg(play_button)
            end_msg.show_msg()
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)


def check_bullet_collisions(baddies, bullets, stats, audio, settings):
    collisions = pygame.sprite.groupcollide(baddies, bullets, True, True)
    if collisions:
        stats.score += 1
        # audio.baddie_ded.play()
        if stats.score > 0:
            if (stats.score % settings.baddies_per_round) == 0:
                level_up(stats, audio)


def create_baddie(screen, baddies, settings, audio):
    new_baddie = Baddie(screen, settings)
    baddies.add(new_baddie)
    # audio.baddie_spawn.play()


def level_up(stats, audio):
    stats.level += 1
    stats.baddie_drop_speed *= 1.1
    audio.play_trump_soundbite()


def update_baddies(baddies, settings, stats):
    baddies.update(stats)
    for baddie in baddies.copy():
        if baddie.rect.y >= settings.screen_height:
            baddies.remove(baddie)


def check_baddie_player_collisions(baddies, player, stats, bullets, audio):
    if pygame.sprite.spritecollideany(player, baddies):
        life_lost(stats, player, bullets, baddies, audio)


def check_baddie_screen_bottom(screen, stats, player, bullets, baddies, audio):
    screen_rect = screen.get_rect()
    for baddie in baddies:
        if baddie.rect.bottom >= screen_rect.bottom:
            life_lost(stats, player, bullets, baddies, audio)


def life_lost(stats, player, bullets, baddies, audio):
    if stats.lives_remaining >= 1:
        stats.lives_remaining -= 1
    else:
        end_game(stats)
    audio.player_ded.play()
    time.sleep(0.2)
    reset_positions(player, bullets, baddies)


def reset_positions(player, bullets, baddies):
    player.reset_position()
    bullets.empty()
    baddies.empty()


def end_game(stats):
    stats.game_active = False


def check_play_button(player, bullets, baddies, stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.reset_stats()
        reset_positions(player, bullets, baddies)
        stats.game_active = True


def no_longer_first_round(stats):
    stats.is_first_round = False
