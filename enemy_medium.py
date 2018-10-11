import random

import pygame

from enemy import Enemy
from missile import Missile
from setting import *


class EnemyMedium(Enemy):

    def __init__(self):
        speed = random.randint(ENEMY_MEDIUM_SPEED_MIN, ENEMY_MEDIUM_SPEED_MAX)
        super().__init__(ENEMY_MEDIUM_IMAGE_PATH_IDLE[0], speed)
        self.image_group = {
            "idle": [self.image],
            "explode": [pygame.image.load(path) for path in ENEMY_MEDIUM_IMAGE_PATH_EXPLODE]
        }
        for i in range(1, len(ENEMY_MEDIUM_IMAGE_PATH_IDLE)):
            self.image_group["idle"].append(pygame.image.load(ENEMY_MEDIUM_IMAGE_PATH_IDLE[i]))
        self.rect.x = random.randint(0, BACKGROUND_SIZE_X-ENEMY_MEDIUM_SIZE_X)
        self.rect.y = -ENEMY_MEDIUM_SIZE_Y
        self.missile_group = pygame.sprite.Group()
        self.fire_cool_down = ENEMY_MEDIUM_FIRE_COOL_DOWN
        self.cool_down_timer = 0
        self.explode_timer = ENEMY_EXPLODE_TIMER
        self.hp = ENEMY_MEDIUM_HP

    def update(self, *args):
        super().update()
        if self.hp <= 0:
            self.explode()
        else:
            self.image = self.image_group["idle"][len(ENEMY_MEDIUM_IMAGE_PATH_IDLE)-1-int((self.hp-.5)/(ENEMY_MEDIUM_HP//len(ENEMY_MEDIUM_IMAGE_PATH_IDLE)))]

    def fire(self):
        trigger = random.randint(1, 100)
        if trigger <= ENEMY_MEDIUM_FIRE_CHANCE and self.cool_down_timer <= 0:
            missile = Missile()
            missile.speed = MISSILE_SPEED
            missile.rect.centerx = self.rect.centerx
            missile.rect.y = self.rect.bottom + ENEMY_MEDIUM_SIZE_Y//2
            self.missile_group.add(missile)
            self.cool_down_timer = self.fire_cool_down
            return missile
        return None

    def explode(self):
        n = len(self.image_group["explode"])
        self.image = self.image_group["explode"][n - self.explode_timer // (PLAYER_EXPLODE_TIMER // n) - 1]
        self.explode_timer -= 1
        if self.explode_timer == 0:
            self.kill()
