import random

import pygame

from game_sprite import GameSprite
from setting import *


class MissileSupply(GameSprite):

    def __init__(self):
        super().__init__(MISSILE_IMAGE_PATH_SUPPLY, speed=MISSILE_SUPPLY_SPEED)
        self.rect.x = random.randint(0, BACKGROUND_SIZE_X-MISSILE_SUPPLY_SIZE_X)
        self.rect.y = -MISSILE_SUPPLY_SIZE_Y

    def update(self, *args):
        super().update()
