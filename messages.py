import pygame.font


class Result:
    def __init__(self, settings, screen, stats, play_button):
        self.screen = screen

        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 30)

        self.prep_msg(play_button)

    def prep_msg(self, play_button):
        score_str = str(self.stats.score)
        msg_str = "Aw, you got Trumped. You scored {}".format(score_str)
        self.msg_image = self.font.render(msg_str, True, self.text_color, self.settings.bg_color)

        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.screen_rect.center
        self.msg_rect.bottom = play_button.rect.top - 20

    def show_msg(self):
        self.screen.blit(self.msg_image, self.msg_rect)


class LevelUp:
    def __init__(self, settings, screen, stats):
        self.screen = screen

        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 30)

        self.prep_level_up_msg()

    def prep_level_up_msg(self):
        level_str = str(self.stats.level)
        msg_str = "Tremendous! You are up to level {}".format(level_str)
        self.msg_image = self.font.render(msg_str, True, self.text_color, self.settings.bg_color)

        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.screen_rect.center
        # self.msg_rect.top = self.screen_rect.top

    def show_level_up_msg(self):
        self.screen.blit(self.msg_image, self.msg_rect)

