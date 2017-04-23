

class GameStats:
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()

        self.lives_remaining = self.settings.lives_limit
        self.score = 0

        self.level = 1
        self.baddie_drop_speed = self.settings.starting_baddie_drop_speed

        self.game_active = False
        self.is_first_round = True

    def reset_stats(self):
        self.lives_remaining = self.settings.lives_limit
        self.score = 0
        self.level = 1
        self.baddie_drop_speed = self.settings.starting_baddie_drop_speed
