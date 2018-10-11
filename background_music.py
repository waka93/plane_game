import pygame

from setting import *


class BGM:

    def __init__(self):
        self.music = pygame.mixer.music.load(BGM_1)
        pygame.mixer.music.set_volume(BGM_VOLUME)

    @staticmethod
    def play():
        pygame.mixer.music.play()

    @staticmethod
    def set_endevent(event):
        pygame.mixer.music.set_endevent(event)

    @staticmethod
    def rewind():
        pygame.mixer.music.rewind()
