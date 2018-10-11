import pygame


# Basic settings
GAME_NAME = "TEST"
FPS = 60
ENEMY_OCCUR_INTERVAL = 1000
CREATE_ENEMY_EVENT = pygame.USEREVENT
GAME_OVER_EVENT = pygame.USEREVENT + 1
ENEMY_SMALL_EXPLODE_EVENT = pygame.USEREVENT + 2
ENEMY_MEDIUM_EXPLODE_EVENT = pygame.USEREVENT + 3
ENEMY_LARGE_EXPLODE_EVENT = pygame.USEREVENT + 4
PLAYER_EXPLODE_EVENT = pygame.USEREVENT + 5
ENEMY_SHOOT_EVENT = pygame.USEREVENT + 6
PLAYER_SHOOT_EVENT = pygame.USEREVENT + 7
BGM_END_EVENT = pygame.USEREVENT + 8

# Increase level based on time playing
LEVEL_UP = 20000

# Background info
BACKGROUND_POSITION_X = 0
BACKGROUND_POSITION_Y = 0

BACKGROUND_SIZE_X = 640
BACKGROUND_SIZE_Y = 960

BACKGROUND_IMAGE_PATH = "./images/background.png"

BACKGROUND_SPEED = 1


# Player info
PLAYER_START_POSITION_X = 256
PLAYER_START_POSITION_Y = 800

PLAYER_SIZE_X = 128
PLAYER_SIZE_Y = 128
PLAYER_IMAGE_EDGE = 10

PLAYER_IMAGE_PATH_STAY = "./images/aircraft_1.png"
PLAYER_IMAGE_PATH_MOVE = "./images/aircraft_2.png"
PLAYER_IMAGE_PATH_EXPLODE = [
    "./images/aircraft_explode_1.png",
    "./images/aircraft_explode_2.png",
    "./images/aircraft_explode_3.png",
    "./images/aircraft_explode_4.png",
]

PLAYER_SPEED = 5

PLAYER_FIRE_COOL_DOWN = 20

PLAYER_EXPLODE_TIMER = 20

PLAYER_HP = 4

# Enemy info

ENEMY_EXPLODE_TIMER = 20
ENEMY_SMALL_SPAWN = 10
ENEMY_MEDIUM_SPAWN = 2

# Small enemy
ENEMY_SMALL_SIZE_X = 64
ENEMY_SMALL_SIZE_Y = 64

ENEMY_SMALL_IMAGE_PATH_IDLE = "./images/aircraft_small_idle.png"
ENEMY_SMALL_IMAGE_PATH_EXPLODE = [
    "./images/aircraft_small_explode_1.png",
    "./images/aircraft_small_explode_2.png",
    "./images/aircraft_small_explode_3.png",
    "./images/aircraft_small_explode_4.png",
]


ENEMY_SMALL_SPEED_MIN = 1
ENEMY_SMALL_SPEED_MAX = 5

ENEMY_SMALL_FIRE_COOL_DOWN = 240
ENEMY_SMALL_FIRE_CHANCE = 10

ENEMY_SMALL_HP = 1

# Medium enemy
ENEMY_MEDIUM_SIZE_X = 128
ENEMY_MEDIUM_SIZE_Y = 128

ENEMY_MEDIUM_IMAGE_PATH_IDLE = [
    "./images/aircraft_medium_idle_1.png",
    "./images/aircraft_medium_idle_2.png",
]

ENEMY_MEDIUM_IMAGE_PATH_EXPLODE = [
    "./images/aircraft_medium_explode_1.png",
    "./images/aircraft_medium_explode_2.png",
    "./images/aircraft_medium_explode_3.png",
    "./images/aircraft_medium_explode_4.png",
]

ENEMY_MEDIUM_SPEED_MIN = 1
ENEMY_MEDIUM_SPEED_MAX = 3

ENEMY_MEDIUM_HP = 4

ENEMY_MEDIUM_FIRE_COOL_DOWN = 120
ENEMY_MEDIUM_FIRE_CHANCE = 20

# Large enemy
ENEMY_LARGE_SIZE_X = 245
ENEMY_LARGE_SIZE_Y = 279

ENEMY_LARGE_IMAGE_PATH_IDLE = [
    "./images/aircraft_large_idle_1.png",
    "./images/aircraft_large_idle_2.png",
    "./images/aircraft_large_idle_3.png",
]

ENEMY_LARGE_IMAGE_PATH_EXPLODE = [
    "./images/aircraft_large_explode_1.png",
    "./images/aircraft_large_explode_2.png",
    "./images/aircraft_large_explode_3.png",
    "./images/aircraft_large_explode_4.png",
    "./images/aircraft_large_explode_5.png",
    "./images/aircraft_large_explode_6.png",
]

ENEMY_LARGE_SPEED_MIN = 1
ENEMY_LARGE_SPEED_MAX = 2

ENEMY_LARGE_HP = 6

ENEMY_LARGE_FIRE_COOL_DOWN = 240
ENEMY_LARGE_FIRE_CHANCE = 60


# Missile
MISSILE_SIZE_X = 9
MISSILE_SIZE_Y = 21

MISSILE_IMAGE_PATH = "./images/missile_1.png"

MISSILE_SPEED = 10

BASIC_ATTACK = 1


# Supplies

# Bomb
BOMB_MAX_NUM = 9

BOMB_SIZE_X = 62
BOMB_SIZE_Y = 56

BOMB_POSITION_X = BACKGROUND_SIZE_X - BOMB_SIZE_X - 80
BOMB_POSITION_Y = BACKGROUND_SIZE_Y - BOMB_SIZE_Y - 20

BOMB_IMAGE_PATH = [
    "./images/ui_remain_bomb_1.png",
    "./images/ui_remain_bomb_2.png",
]

BOMB_SUPPLY_SIZE_X = 61
BOMB_SUPPLY_SIZE_Y = 103

BOMB_IMAGE_PATH_SUPPLY = "./images/supply_bomb.png"

# Missile

MISSILE_SUPPLY_SIZE_X = 58
MISSILE_SUPPLY_SIZE_Y = 87

MISSILE_IMAGE_PATH_SUPPLY = "./images/supply_double_missile.png"

# Sound

# BGM

BGM_1 = "./sounds/bgm_1.wav"
BGM_VOLUME = .2

# SE

PLAYER_SHOOT_SE_VOLUME = .2
ENEMY_SHOOT_SE_VOLUME = .2

SE = {
    "ENEMY_SMALL_EXPLODE_SOUND": "./sounds/se_enemy_small_explode.wav",
    "ENEMY_MEDIUM_EXPLODE_SOUND": "./sounds/se_enemy_medium_explode.wav",
    "ENEMY_LARGE_EXPLODE_SOUND": "./sounds/se_enemy_large_explode.wav",
    "PLAYER_EXPLODE_SOUND": "./sounds/se_enemy_medium_explode.wav",
    "PLAYER_SHOOT_SOUND": "./sounds/se_player_shoot.wav",
    "ENEMY_SHOOT_SOUND": "./sounds/se_enemy_shoot.wav",
    "GET_SUPPLY_SOUND": "./sounds/se_get_supply.wav",
}


# Font

BOMB_FONT = "./fonts/Good_Morning.ttf"
BOMB_FONT_SIZE = 25
