import pygame

from game_sprite import GameSprite
from missile import Missile
from setting import *


class Player(GameSprite):

    def __init__(self, path, speed):
        super().__init__(path, speed)
        self.image_group = {
            "stay": self.image,
            "move": pygame.image.load(PLAYER_IMAGE_PATH_MOVE),
            "explode": [pygame.image.load(path) for path in PLAYER_IMAGE_PATH_EXPLODE]
        }
        self.rect.x = PLAYER_START_POSITION_X
        self.rect.y = PLAYER_START_POSITION_Y
        self.direction = [0, 0]
        self.missile_group = pygame.sprite.Group()
        self.fire_cool_down = PLAYER_FIRE_COOL_DOWN
        self.cool_down_timer = 0
        self.explode_timer = PLAYER_EXPLODE_TIMER
        self.hp = PLAYER_HP

    def update(self, *args):
        if self.direction[0] != 0 or self.direction[1] != 0:
            self.image = self.image_group["move"]
        else:
            self.image = self.image_group["stay"]
        self.rect.x += self.direction[0] * self.speed
        self.rect.x = max(self.rect.x, 0-PLAYER_IMAGE_EDGE)
        self.rect.x = min(self.rect.x, BACKGROUND_SIZE_X-PLAYER_SIZE_X+PLAYER_IMAGE_EDGE)
        self.rect.y -= self.direction[1] * self.speed
        self.rect.y = max(self.rect.y, 0-PLAYER_IMAGE_EDGE)
        self.rect.y = min(self.rect.y, BACKGROUND_SIZE_Y-PLAYER_SIZE_Y+PLAYER_IMAGE_EDGE)
        if self.hp <= 0:
            if self.explode_timer == PLAYER_EXPLODE_TIMER:
                pygame.event.post(pygame.event.Event(PLAYER_EXPLODE_EVENT))
            self.explode()

    def fire(self):
        if self.cool_down_timer <= 0:
            pygame.event.post(pygame.event.Event(PLAYER_SHOOT_EVENT))
            m = Missile()
            m.rect.centerx = self.rect.centerx
            m.rect.y = self.rect.top - MISSILE_SIZE_Y//2
            self.missile_group.add(m)
            self.cool_down_timer = self.fire_cool_down
            return m
        return None

    def explode(self):
        n = len(self.image_group["explode"])
        self.image = self.image_group["explode"][n - self.explode_timer//(PLAYER_EXPLODE_TIMER//n) - 1]
        self.explode_timer -= 1
        if self.explode_timer == 0:
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))
