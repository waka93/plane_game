import random

import pygame

from enemy import Enemy
from missile import Missile
from setting import *


class EnemySmall(Enemy):

    def __init__(self):
        speed = random.randint(ENEMY_SMALL_SPEED_MIN, ENEMY_SMALL_SPEED_MAX)
        super().__init__(ENEMY_SMALL_IMAGE_PATH_IDLE, speed)
        self.image_group = {
            "idle": self.image,
            "explode": [pygame.image.load(path) for path in ENEMY_SMALL_IMAGE_PATH_EXPLODE]
        }
        self.rect.x = random.randint(0, BACKGROUND_SIZE_X-ENEMY_SMALL_SIZE_X)
        self.rect.y = -ENEMY_SMALL_SIZE_Y
        self.missile_group = pygame.sprite.Group()
        self.fire_cool_down = ENEMY_SMALL_FIRE_COOL_DOWN
        self.cool_down_timer = 0
        self.explode_timer = ENEMY_EXPLODE_TIMER
        self.hp = ENEMY_SMALL_HP

    def update(self, *args):
        super().update()
        if self.hp <= 0:
            self.explode()

    def fire(self):
        trigger = random.randint(1, 100)
        if trigger <= ENEMY_SMALL_FIRE_CHANCE and self.cool_down_timer <= 0:
            missile = Missile()
            missile.speed = MISSILE_SPEED
            missile.rect.centerx = self.rect.centerx
            missile.rect.y = self.rect.bottom + ENEMY_SMALL_SIZE_Y//2
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