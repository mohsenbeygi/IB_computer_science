from os import path
import pygame as pg
vec = pg.math.Vector2

# game options / settings
WIDTH = 800
HEIGHT = 700
FPS = 60
DIR = path.dirname(__file__)
IMAGE_DIR = path.join(DIR, 'images')
SOUND_DIR = path.join(DIR, 'sounds')
TITLE = 'Plane'
ICON = 'planeYellow1.png'

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GREEN = (125, 255, 50)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_GRAY = (200, 200, 200)
GRAY = (150, 150, 150)
LIGHT_BLUE = (0, 200, 255)
SKY_START_COLOR = LIGHT_BLUE
SKY_END_COLOR = WHITE
YELLOW = (255, 255, 0)

# images
PLANE_COLORS = ['Red', 'Blue', 'Green', 'Yellow']

# plane settings
PLANE_POS = vec(WIDTH // 6, HEIGHT // 3)
PLANE_VY = 350
PLANE_VX = 300
PLANE_FRAME_TIME = 50
PLANE_WOBBLE = 3
PLANE_SOUND = 'plane.ogg'
VOL_ACC = 0.005
ACCELERATE_VOL = 0.5
CRUISE_VOL = 0.1

# ground
GROUND_TYPES = ['Dirt', 'Grass', 'Ice', 'Snow', 'Rock']

# explosions
EXPLOSION_TYPES = ['flash', 'fart', 'explosion']

# animations
ANIMATION_FRAME_TIME = 70

# menu setings
MENU_TITLE = 'Plane'
TITLE_FONT = 100
START_BUTTON = pg.Rect(WIDTH // 5, HEIGHT * 2 // 3, WIDTH // 5, HEIGHT // 6)
QUIT_BUTTON = pg.Rect(WIDTH * 3 // 5, HEIGHT * 2 // 3, WIDTH // 5, HEIGHT // 6)
MENU_BACKGROUND = 'background.png'
COLOR_BUTTON = pg.Rect(WIDTH * 2 // 7, HEIGHT * 5 // 12, WIDTH * 3 // 7, HEIGHT // 6)
BUTTON_COLORS = [[RED, (255, 100, 100)], [BLUE, (0, 200, 255)],
                 [YELLOW, (255, 231, 74)], [GREEN, LIGHT_GREEN]]

# obstacles
OBSTACLES = ['rock', 'rockIce', 'rockGrass', 'rockSnow']
OBSTACLE_NUM = 6
OBSTACLE_SIZE = [HEIGHT // 5, HEIGHT * 5 // 11]
OBSTACLE_DIS = WIDTH // 3
MIN_OBSTACLE_DIS = int(WIDTH / 5)
PLANE_COLORS = ['Red', 'Blue', 'Yellow', 'Green']

# items
COIN_IMAGES = ['Bronze', 'Silver', 'Gold']
