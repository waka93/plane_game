import random

import pygame

from game_sprite import GameSprite
from setting import *


class BombSupply(GameSprite):

    def __init__(self):
        super().__init__(BOMB_IMAGE_PATH_SUPPLY, speed=BOMB_SUPPLY_SPEED)
        self.rect.x = random.randint(0, BACKGROUND_SIZE_X-BOMB_SUPPLY_SIZE_X)
        self.rect.y = -BOMB_SUPPLY_SIZE_Y

    def update(self, *args):
        super().update()
