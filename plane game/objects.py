import pygame as pg
import random
from settings import *
vec = pg.math.Vector2


# objects
class Plane(pg.sprite.Sprite):
    def __init__(self, all_objects, frames, pos):
        all_objects.append(self)
        pg.sprite.Sprite.__init__(self)
        self.frames = frames
        self.frame = 0
        self.frame_start = pg.time.get_ticks()
        self.image = self.frames[self.frame]
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        self.vel = vec(PLANE_VX, 0)
        self.acc = vec(0, 0)
        self.angle = 0
        self.wobble = random.randint(-PLANE_WOBBLE, PLANE_WOBBLE)
        self.crash = False
        self.volume = CRUISE_VOL
        self.mask = pg.mask.from_surface(self.image)
        self.explosion_effect = False

    def get_events(self, vy):
        self.acc = vec(0, vy)
        keys = pg.key.get_pressed()
        self.volume_acc = VOL_ACC
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.acc = vec(0, -vy)
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.acc = vec(0, vy * 2)
        else:
            self.volume_acc = -VOL_ACC

    def update(self, dt, vy):
        if not self.crash:
            self.update_frame()
            self.angle = self.vel.angle_to(vec(PLANE_VX, 0))
            self.image = pg.transform.rotate(self.frames[self.frame],
                                             self.angle + self.wobble)
            self.rect = self.image.get_rect()
            self.mask = pg.mask.from_surface(self.image)
            self.get_events(vy)
            self.acc.y -= self.vel.y
            self.vel.y += self.acc.y * dt
            self.pos.y += self.vel.y * dt
            if self.pos.y < 0:  # self.rect.width // 2:
                self.pos.y = 0  # self.rect.width // 2
            elif self.pos.y > WIDTH:  # - self.rect.width // 2:
                self.pos.y = WIDTH  # - self.rect.width // 2
            self.rect.center = self.pos
            self.volume = max(min(self.volume + self.volume_acc, ACCELERATE_VOL), CRUISE_VOL)

    def update_frame(self):
        now = pg.time.get_ticks()
        if now - self.frame_start > PLANE_FRAME_TIME / (self.volume / ACCELERATE_VOL):
            self.frame_start = now
            self.frame = (self.frame + 1) % len(self.frames)
            self.wobble = random.randint(-PLANE_WOBBLE, PLANE_WOBBLE)

    def explode(self, all_objects, exp_images):
        self.crash = True
        exp_image = exp_images[random.choice(EXPLOSION_TYPES)]
        self.explosion_effect = True
        Animation(all_objects, exp_image, self.pos)

    def draw(self, screen):
        if not self.crash:
            screen.blit(self.image, self.rect)


class Ground(pg.sprite.Sprite):
    def __init__(self, all_objects, grounds, pos, index):
        all_objects.append(self)
        pg.sprite.Sprite.__init__(self)
        self.grounds = grounds
        self.ground_index = index
        self.image = self.grounds[self.ground_index]
        self.rect = self.image.get_rect()
        self.rect.y = HEIGHT - self.rect.height
        self.rect.x = pos
        self.x = pos
        self.start_pos = pos
        self.vx = PLANE_VX
        self.mask = pg.mask.from_surface(self.image)

    def update(self, dt):
        # old_pos = self.x
        self.x = -(-(self.x - self.vx * dt) % self.rect.width - self.start_pos)
        # print(abs(self.x - old_pos), self.vx * dt)
        # if abs(self.x - old_pos) > self.vx * dt + 10:
        #     self.ground_index = (self.ground_index + 1) % len(self.grounds)
        #     self.image = self.grounds[self.ground_index]
        #     self.rect = self.image.get_rect()
        #     self.rect.y = HEIGHT - self.rect.height

        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Animation:
    def __init__(self, all_objects, frames, pos):
        self.all_objects = all_objects
        self.all_objects.append(self)
        self.frame = 0
        self.frame_start = pg.time.get_ticks()
        self.frames = frames
        self.image = self.frames[self.frame]
        self.size = self.image.get_size()
        new_size = (self.size[0] - (len(self.frames) - self.frame) * 50,
                    self.size[1] - (len(self.frames) - self.frame) * 50)
        self.image = pg.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos

    def update(self, dt):
        now = pg.time.get_ticks()
        if now - self.frame_start > ANIMATION_FRAME_TIME:
            self.frame_start = pg.time.get_ticks()
            self.frame += 1
            if self.frame > len(self.frames) - 1:
                self.all_objects.remove(self)
            else:
                self.image = self.frames[self.frame]
                new_size = (self.size[0] - (len(self.frames) - self.frame) * 50,
                            self.size[1] - (len(self.frames) - self.frame) * 50)
                self.image = pg.transform.scale(self.image, new_size)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)


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


# button object for menus
class Button:
    def __init__(self, active_color, inactive_color, rect, text):
        # color and text settings
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.text = text
        self.color = self.inactive_color
        # position and rect settings
        self.rect = rect
        self.x = self.rect.x
        self.width = self.rect.width
        self.last_click = pg.time.get_ticks()

    def update(self):
        # update button state and return if it got pressed or not
        mouse_pos = pg.mouse.get_pos()
        self.color = self.inactive_color
        self.rect.width = self.width
        self.rect.x = self.x
        # check if the mouse is hovering above the button
        if self.rect.x < mouse_pos[0] < self.rect.right:
            if self.rect.y < mouse_pos[1] < self.rect.bottom:
                mouse_press = pg.mouse.get_pressed()
                self.color = self.active_color
                self.rect.x -= self.rect.width // 6
                self.rect.width = self.rect.width * 4 // 3
                # check if the button got pressed (mouse pressed on the button)
                if mouse_press[0] and pg.time.get_ticks() - self.last_click > 350:
                    self.last_click = pg.time.get_ticks()
                    return True
        return False

    def draw(self, screen):
        # draw button rect and text
        pg.draw.rect(screen, self.color, self.rect)
        pg.draw.rect(screen, BLACK, self.rect, 3)
        self.font_size = self.rect.width // len(self.text) * 5 // 4
        draw_text(screen, self.text, 'comicsansms',
                  self.font_size, BLACK, self.rect.centerx, self.rect.centery, align='center')


class Obstacle(pg.sprite.Sprite):
    def __init__(self, all_objects, obstacles, image, pos, vx, side):
        all_objects.append(self)
        obstacles.append(self)
        pg.sprite.Sprite.__init__(self)
        self.all_objects = all_objects
        self.obstacles = obstacles
        image_size = image.get_size()
        if len(obstacles) > 1:
            new_height = (HEIGHT - obstacles[-2].rect.height) * 5 // 6
            new_height = random.choice([(new_height + random.randint(OBSTACLE_SIZE[0], OBSTACLE_SIZE[1])) // 2,
                                        OBSTACLE_SIZE[0],
                                        OBSTACLE_SIZE[1],
                                        random.randint(OBSTACLE_SIZE[0], OBSTACLE_SIZE[1])
                                        ])
        else:
            new_height = random.randint(OBSTACLE_SIZE[0], OBSTACLE_SIZE[1])
        # * new_height // image_size[1]
        image = pg.transform.scale(image, (image_size[0] * 4 // 5, new_height))
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = pos
        if not side:
            self.rect.y = self.pos.y
        else:
            self.rect.bottom = self.pos.y
        self.side = side
        self.vx = vx
        self.rect.centerx = self.pos.x
        self.mask = pg.mask.from_surface(self.image)

    def update(self, dt):
        if dt > 1:
            print('noooo')
        else:
            self.pos.x -= self.vx * dt
            self.rect.centerx = self.pos.x
            # print('pos: ', self.pos.x, 'rect: ', self.rect.x)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Coin:
    def __init__(self, all_objects, items, image, pos, score, vx):
        all_objects.append(self)
        items.append(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        self.score = score
        self.vx = vx

    def update(self, dt):
        self.pos.x -= self.vx * dt
        self.rect.centerx = self.pos.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)
