import pygame
from pygame.locals import *

from game_sprite import GameSprite
from setting import *


class Bomb(GameSprite):

    def __init__(self):
        super().__init__(BOMB_IMAGE_PATH, speed=0)
        self.num = 1
