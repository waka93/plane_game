import random

from game_sprite import GameSprite
from setting import *


class Enemy(GameSprite):

    def update(self, *args):
        super().update()
        if self.rect.y >= BACKGROUND_SIZE_Y:
            self.kill()

    def fire(self):
        pass

    def explode(self):
        pass
