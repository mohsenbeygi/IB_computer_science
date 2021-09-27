# With the name of god
# Art from kenney "Kenney.nl" or "www.kenney.nl"
# Plane game

import sys
import time
import pygame as pg
import random
from settings import *
from objects import *
vec = pg.math.Vector2


# functions
def load_images(image_dir, plane_colors, ground_types, exp_types, obstacles, coin_images):
    images = {}

    # planes
    images['planes'] = {}
    for plane_color in plane_colors:
        images['planes'][plane_color] = []
        for index in range(1, 4):
            plane_name = 'plane{0}{1}.png'.format(plane_color, index)
            img = pg.image.load(path.join(image_dir, plane_name)).convert_alpha()
            images['planes'][plane_color].append(img)

    images['grounds'] = []
    for ground_type in ground_types:
        plane_name = 'ground{0}.png'.format(ground_type)
        img = pg.image.load(path.join(image_dir, plane_name)).convert_alpha()
        images['grounds'].append(img)

    images['exp'] = {}
    for exp_type in exp_types:
        images['exp'][exp_type] = []
        for index in range(9):
            exp_name = '{0}0{1}.png'.format(exp_type, index)
            img = pg.image.load(path.join(image_dir, exp_name)).convert_alpha()
            images['exp'][exp_type].append(img)

    images['obstacles'] = {}
    for obstacle in obstacles:
        img = pg.image.load(path.join(image_dir, obstacle + '.png')).convert_alpha()
        name = '{}Down.png'.format(obstacle)
        images['obstacles'][obstacle] = [img]
        img = pg.image.load(path.join(image_dir, name)).convert_alpha()
        images['obstacles'][obstacle].append(img)

    images['coins'] = []
    for coin_image in coin_images:
        images['coins'].append(pg.image.load(
            path.join(image_dir, 'medal{}.png'.format(coin_image))).convert_alpha())

    return images


def dry_sky(screen, start_color, end_color, screen_height, screen_width):
    vr = (end_color[0] - start_color[0]) / screen_height
    vg = (end_color[1] - start_color[1]) / screen_height
    vb = (end_color[2] - start_color[2]) / screen_height
    color = [start_color[0], start_color[1], start_color[2]]
    for y in range(0, screen_height):
        pg.draw.rect(screen, (color[0] // 1, color[1] // 1, color[2] // 1), [0, y, screen_width, 2])
        color[0] += vr
        color[1] += vg
        color[2] += vb


def draw_text(screen, text, font_name, size, color, x, y, align="nw"):
    font = pg.font.SysFont(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if align == "nw":
        text_rect.topleft = (x, y)
    elif align == "ne":
        text_rect.topright = (x, y)
    elif align == "sw":
        text_rect.bottomleft = (x, y)
    elif align == "se":
        text_rect.bottomright = (x, y)
    elif align == "n":
        text_rect.midtop = (x, y)
    elif align == "s":
        text_rect.midbottom = (x, y)
    elif align == "e":
        text_rect.midright = (x, y)
    elif align == "w":
        text_rect.midleft = (x, y)
    elif align == "center":
        text_rect.center = (x, y)

    screen.blit(text_surface, text_rect)


def program_quit():
    pg.quit()
    sys.exit()


def menu(screen, background, record):
    menu = True
    start_button = Button(LIGHT_GREEN, GREEN, START_BUTTON.copy(), "Start")
    quit_button = Button(LIGHT_GRAY, GRAY, QUIT_BUTTON.copy(), "Quit")
    color_index = 0
    color_button = Button(BUTTON_COLORS[color_index][1],
                          BUTTON_COLORS[color_index][0], COLOR_BUTTON.copy(), "Color")
    while menu:
        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                # record
                with open(path.join(DIR, 'record.txt'), 'w') as record_file:
                    record_file.write(str(record))
                program_quit()

        click = start_button.update()
        if click:
            menu = False

        click = quit_button.update()
        if click:
            # record
            with open(path.join(DIR, 'record.txt'), 'w') as record_file:
                record_file.write(str(record))
            program_quit()
        click = color_button.update()
        if click:
            color_index = (color_index + 1) % len(PLANE_COLORS)
            del color_button
            color_button = Button(BUTTON_COLORS[color_index][1], BUTTON_COLORS[color_index][0],
                                  COLOR_BUTTON.copy(), "Color")

        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        start_button.draw(screen)

        quit_button.draw(screen)

        color_button.draw(screen)

        draw_text(screen, MENU_TITLE, 'comicsansms', TITLE_FONT, BLACK, WIDTH // 2, 50, align="n")

        draw_text(screen, 'Highest score: ' + str(record), 'comicsansms',
                  TITLE_FONT // 3, BLACK, 10, 0, align="nw")

        pg.display.update()

    return color_index


# initialize pygame and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
icon = pg.image.load(path.join(IMAGE_DIR, ICON)).convert_alpha()
pg.display.set_icon(icon)
clock = pg.time.Clock()

# load files
images = load_images(IMAGE_DIR, PLANE_COLORS, GROUND_TYPES, EXPLOSION_TYPES, OBSTACLES, COIN_IMAGES)
plane_sound = pg.mixer.music.load(path.join(SOUND_DIR, PLANE_SOUND))
menu_background = pg.transform.scale(pg.image.load(
    path.join(IMAGE_DIR, MENU_BACKGROUND)), (WIDTH, HEIGHT))

# record
with open(path.join(DIR, 'record.txt'), 'r') as record_file:
    record = int(record_file.readline())

# game loop
running = True
score = 0
while running:
    all_objects = []
    obstacles = []
    items = []

    ground_len = images['grounds'][0].get_size()[0]
    ground_count = round(WIDTH / ground_len) * 2
    grounds = []
    for index in range(ground_count):
        grounds.append(Ground(all_objects, images['grounds'], index * ground_len, 0))

    record = max(score, record)
    playing = True
    score = 0
    dis_score = 0

    obstacle_dis = OBSTACLE_DIS
    side = random.randint(0, 1)
    image = random.choice(list(images['obstacles'].values()))[1 - side]
    Obstacle(all_objects, obstacles, image, vec(WIDTH // 2, HEIGHT * side), PLANE_VX, side)
    for index in range(1, OBSTACLE_NUM + 1):
        x = index * obstacle_dis + WIDTH // 2
        side = 1
        if obstacles[-1].side:
            side = 0
        image = random.choice(list(images['obstacles'].values()))[1 - side]
        Obstacle(all_objects, obstacles, image, vec(x, HEIGHT * side), PLANE_VX, side)

    # start_menu
    color_index = menu(screen, menu_background, record)

    plane_pos = vec(PLANE_POS.x, PLANE_POS.y)
    plane = Plane(all_objects, images['planes'][PLANE_COLORS[color_index]], plane_pos)

    pg.mixer.music.set_volume(CRUISE_VOL)
    pg.mixer.music.play(-1)

    while playing or running and plane.explosion_effect:
        # keep loop running at the right speed ( FPS )
        dt = clock.tick(FPS) / 1000.0

        # events section
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                playing = False
                running = False

        # Update section

        # update all objects
        old_vol = plane.volume
        obst_index = 0
        for index, object in enumerate(all_objects):
            if isinstance(object, Plane):
                object.update(dt, PLANE_VY + score * 4)

            elif isinstance(object, Obstacle):
                object.update(dt)
                if object.pos.x < -object.rect.width * 2:
                    del all_objects[index]
                    del obstacles[obst_index]
                    del object
                    deleted = True
                obst_index += 1

            else:
                object.update(dt)

        if old_vol != plane.volume:
            pg.mixer.music.set_volume(plane.volume)

        # check if a plane hit the ground ( grounds )
        for ground in grounds:
            if plane.pos.y + plane.rect.height // 2 > HEIGHT - ground.rect.height:
                if not plane.crash:
                    hit = pg.sprite.collide_mask(plane, ground)
                    if hit or plane.pos.y + plane.rect.height // 2 > HEIGHT:
                        # print(hit)
                        pg.mixer.music.stop()
                        for ground in grounds:
                            ground.vx = 0
                        for obstacle in obstacles:
                            obstacle.vx = 0
                        for item in items:
                            item.vx = 0
                        plane.explode(all_objects, images['exp'])
                        playing = False
                        break

        # check if plane hit an obstacle
        for obstacle in obstacles:
            if obstacle.rect.x < plane.rect.right < obstacle.rect.right:
                if plane.rect.bottom > obstacle.rect.top:
                    if not plane.crash:
                        hit = pg.sprite.collide_mask(plane, obstacle)
                        if hit:
                            pg.mixer.music.stop()
                            for ground in grounds:
                                ground.vx = 0
                            for obstacle in obstacles:
                                obstacle.vx = 0
                            for item in items:
                                item.vx = 0
                            plane.explode(all_objects, images['exp'])
                            playing = False
                            break

        # check to create a new obstacle
        if len(obstacles) < OBSTACLE_NUM:
            score += 1
            # print('new obstacle', time.time())
            x = obstacles[-1].rect.right + obstacle_dis
            side = 1
            if obstacles[-1].side:
                side = 0
            sides = [side] * 9 + [not side]
            side = random.choice(sides)
            image = random.choice(list(images['obstacles'].values()))[1 - side]
            Obstacle(all_objects, obstacles, image, vec(x, HEIGHT * side), PLANE_VX, side)

        if plane.explosion_effect:
            flag = False
            for object in all_objects:
                if isinstance(object, Animation):
                    flag = True
                    break
            if not flag:
                plane.explosion_effect = False

        if score > dis_score + 3:
            coin_index = random.randint(0, len(images['coins']) - 1)
            coin_image = images['coins'][coin_index]
            pos = vec(random.randint(WIDTH, WIDTH * 2),
                      random.randint(grounds[0].rect.height + 100,
                                     HEIGHT - 100 - grounds[0].rect.height))
            Coin(all_objects, items, coin_image, pos, (coin_index + 1) * 5, PLANE_VX)
            dis_score = score
            obstacle_dis = max(MIN_OBSTACLE_DIS, obstacle_dis - 5)

        for index, item in enumerate(items):
            if isinstance(item, Coin):
                if item.rect.x < plane.rect.x < item.rect.right or item.rect.x < plane.rect.right < item.rect.right:
                    if item.rect.y < plane.rect.y < item.rect.bottom or item.rect.y < plane.rect.bottom < item.rect.bottom:
                        score += item.score
                        del items[index]
                        all_objects.remove(item)
                        del item

        # Draw / render
        pg.display.set_caption('{:.2f}'.format(clock.get_fps()))
        dry_sky(screen, SKY_START_COLOR, SKY_END_COLOR, HEIGHT, WIDTH)
        for object in all_objects:
            object.draw(screen)
        plane.draw(screen)
        draw_text(screen, str(score), 'comicsansms', 50, BLACK, WIDTH // 2, 0, align="n")

        pg.display.update()

# record
with open(path.join(DIR, 'record.txt'), 'w') as record_file:
    record_file.write(str(record))

program_quit()
