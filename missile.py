from game_sprite import GameSprite
from setting import *


class Missile(GameSprite):

    def __init__(self, path):
        super().__init__(path, speed=-MISSILE_SPEED)
        self.attack = BASIC_ATTACK

    def update(self, *args):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
