import pygame
from pygame.locals import *


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_path, speed=1):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed

