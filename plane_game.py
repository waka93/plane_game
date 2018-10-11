import random

import pygame
from pygame.locals import *

from setting import *
from background import Background
from player import Player
from enemy_small import EnemySmall
from enemy_medium import EnemyMedium
from enemy_large import EnemyLarge
from bomb import Bomb


class PlaneGame:
    # Basic frames
    __screen = None
    __clock = None

    # Units
    __player = None
    __player_group = None
    __background_group = None
    __enemy_group = None
    __enemy_count = [0, 0, 0]
    __enemy_missile_group = None

    # Supplies
    __bomb = None

    def __init__(self):
        self.__screen = pygame.display.set_mode((BACKGROUND_SIZE_X, BACKGROUND_SIZE_Y))
        self.__clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, ENEMY_OCCUR_INTERVAL)

    def __create_sprites(self):
        # Create background sprite group
        bg1 = Background(BACKGROUND_IMAGE_PATH)
        bg2 = Background(BACKGROUND_IMAGE_PATH, True)
        self.__background_group = pygame.sprite.Group(bg1, bg2)

        # Create player sprite group
        self.__player = Player(PLAYER_IMAGE_PATH_STAY, speed=PLAYER_SPEED)
        self.__player_group = pygame.sprite.Group(self.__player)

        # Create enemy sprite group
        self.__enemy_group = pygame.sprite.Group()
        self.__enemy_missile_group = pygame.sprite.Group()

        # Create bomb sprite
        self.__bomb = Bomb()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit()

            # Create enemies
            elif event.type == CREATE_ENEMY_EVENT:
                for i in range(random.randint(0, 1+int(pygame.time.get_ticks()//LEVEL_UP))):
                    enemy = EnemySmall()
                    self.__enemy_group.add(enemy)
                    self.__enemy_count[0] += 1

                    # Spawn medium size enemy
                    if self.__enemy_count[0] >= ENEMY_SMALL_SPAWN:
                        enemy_medium = EnemyMedium()
                        self.__enemy_group.add(enemy_medium)
                        self.__enemy_count[0] = 0
                        self.__enemy_count[1] += 1

                    # Spawn large size enemy
                    if self.__enemy_count[1] >= ENEMY_MEDIUM_SPAWN:
                        enemy_large = EnemyLarge()
                        self.__enemy_group.add(enemy_large)
                        self.__enemy_count[1] = 0
                        self.__enemy_count[2] += 1

            elif event.type == KEYDOWN and event.key == K_b:
                self.__enemy_missile_group.empty()
                for sprite in self.__enemy_group.sprites():
                    sprite.hp = 0

            elif event.type == GAME_OVER_EVENT:
                self.__create_sprites()
                self.start_game()

        key_pressed = pygame.key.get_pressed()

        # Player move
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_LEFT]:
            if key_pressed[pygame.K_RIGHT]:
                if self.__player.direction[0] <= 0:
                    self.__player.direction[0] += 1
            if key_pressed[pygame.K_LEFT]:
                if self.__player.direction[0] >= 0:
                    self.__player.direction[0] -= 1
        else:
            self.__player.direction[0] = 0
        if key_pressed[pygame.K_UP] or key_pressed[pygame.K_DOWN]:
            if key_pressed[pygame.K_UP]:
                if self.__player.direction[1] <= 0:
                    self.__player.direction[1] += 1
            if key_pressed[pygame.K_DOWN]:
                if self.__player.direction[1] >= 0:
                    self.__player.direction[1] -= 1
        else:
            self.__player.direction[1] = 0

        # Player fire
        if key_pressed[pygame.K_SPACE]:
            self.__player.fire()

    def __collision_detection(self):
        # Create mask for player
        player_mask = pygame.mask.from_surface(self.__player.image)

        for sprite in self.__enemy_group.sprites():
            # Create mask for enemy
            enemy_mask = pygame.mask.from_surface(sprite.image)

            # Check if an enemy collide with the player
            if self.__player.explode_timer == PLAYER_EXPLODE_TIMER and sprite.hp > 0 and \
                    player_mask.overlap(enemy_mask, (sprite.rect.x-self.__player.rect.x, sprite.rect.y-self.__player.rect.y)) is not None:
                self.__player.explode_timer -= 1
                sprite.explode_timer -= 1

            # Check if a player missile hit an enemy
            for missile in self.__player.missile_group.sprites():
                missile_mask = pygame.mask.from_surface(missile.image)
                if sprite.hp > 0 and missile_mask.overlap(enemy_mask, (sprite.rect.x-missile.rect.x, sprite.rect.y-missile.rect.y)):
                    sprite.hp -= missile.attack
                    missile.kill()

        # Check if an enemy missile hit the player
        for missile in self.__enemy_missile_group.sprites():
            missile_mask = pygame.mask.from_surface(missile.image)
            if self.__player.explode_timer == PLAYER_EXPLODE_TIMER and \
                    missile_mask.overlap(player_mask, (self.__player.rect.x-missile.rect.x, self.__player.rect.y-missile.rect.y)) is not None:
                self.__player.explode_timer -= 1
                missile.kill()

    def __update_sprites(self):
        # Update background
        self.__background_group.update()
        self.__background_group.draw(self.__screen)

        # Update enemy missiles
        for sprite in self.__enemy_group.sprites():
            missile = sprite.fire()
            if missile is not None:
                self.__enemy_missile_group.add(missile)
        self.__enemy_missile_group.update()
        self.__enemy_missile_group.draw(self.__screen)

        # Update enemy aircraft
        self.__enemy_group.update()
        self.__enemy_group.draw(self.__screen)

        # Update player missiles
        self.__player.missile_group.update()
        self.__player.missile_group.draw(self.__screen)

        # Update player aircraft
        self.__player_group.update()
        self.__player_group.draw(self.__screen)

        # Fire cooling down
        if self.__player.cool_down_timer > 0:
            self.__player.cool_down_timer -= 1
        for sprite in self.__enemy_group.sprites():
            if sprite.cool_down_timer > 0:
                sprite.cool_down_timer -= 1

    def start_game(self):
        pygame.init()

        while True:
            # Set fps
            self.__clock.tick(FPS)
            # Event handler
            self.__event_handler()
            # Collision detection
            self.__collision_detection()
            # Redraw
            self.__update_sprites()
            # Update display
            pygame.display.update()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
