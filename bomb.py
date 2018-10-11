import pygame
from pygame.locals import *

from game_sprite import GameSprite
from setting import *


class Bomb(GameSprite):

    def __init__(self):
        super().__init__(BOMB_IMAGE_PATH[0], speed=0)
        self.__num = 3
        self.image_group = [self.image]
        self.image_group.append(pygame.image.load(BOMB_IMAGE_PATH[1]))
        self.rect.x = BOMB_POSITION_X
        self.rect.y = BOMB_POSITION_Y
        self.font = pygame.font.Font(BOMB_FONT, BOMB_FONT_SIZE)
        self.__text = self.font.render(str(self.__num), True, (0, 0, 0))

    def add(self):
        self.__num += 1
        self.__num = min(BOMB_MAX_NUM, self.__num)

    def subtract(self):
        self.__num -= 1
        self.__num = max(0, self.__num)

    def get_remains(self):
        return self.__num

    def get_text(self):
        return self.__text

    def update(self, *args):
        super().update()
        self.__text = self.font.render(str(self.__num), True, (0, 0, 0))
        if self.__num == 0:
            self.image = self.image_group[1]
        else:
            self.image = self.image_group[0]
