from game_sprite import GameSprite
from setting import *


class Background(GameSprite):

    def __init__(self, path, is_alt=False):
        super().__init__(path)
        if is_alt:
            self.rect.y = BACKGROUND_SIZE_Y

    def update(self, *args):
        super().update()

        if self.rect.y >= BACKGROUND_SIZE_Y:
            self.rect.y = -BACKGROUND_SIZE_Y

