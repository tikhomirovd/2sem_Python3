import math
import random

import pygame
from pygame import font
from pygame.locals import *

pygame.init()
(windows_width, windows_height, windows_title) = (800, 600, "Simple Figure")
screen = pygame.display.set_mode((windows_width, windows_height), 0, 32)
pygame.display.set_caption(windows_title)
windows_bgcolor = (0, 77, 255)
mainLoop = True

def_font = font.Font('freesansbold.ttf', 30)

body_x = 350
head_x = 361
hand_1_x = 350
hand_2_x = 400
leg_x = 380

red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
bodile = (222, 184, 135)
brown = (165, 42, 42)
white = (255, 255, 255)
roof_color = (128, 0, 0)
black = (0, 0, 0)
BIRD = (0, 0, 0)

sun = (30, 50)
grass = Rect(0, 400, 800, 500)
house = Rect(10, 300, 100, 100)
window = Rect(35, 330, 50, 50)
body_1 = Rect((200, 275), (50, 100))
roof = [(10, 300), (110, 300), (55, 200)]

st_angle = 31
birds_count = 1
birds = {'here': False, 'x': 0, 'y': 0, 'size': 20, 'speed': 0,
         'fly': st_angle, 'direction': 1, 'k': 1}
spawn_range = spawn_r_s, spawn_r_f = 50, 250
size_range = size_r_s, size_r_f = 20, 35

sun = {'x': 100}


def bird(x, y, size, angle):
    x1 = x + size * math.cos(math.radians(180 - angle))
    x2 = x - size * math.cos(math.radians(180 - angle))
    y1 = y - size * math.sin(math.radians(angle))
    pygame.draw.lines(screen, BIRD, 0, ((x1, y1), (x, y), (x2, y1)), 4)
    pygame.draw.lines(screen, BIRD, 0, ((x1, y1), (x, y - 4), (x2, y1)), 4)
    pygame.draw.circle(screen, BIRD, (x, y - 7), 3)


def bird_fly(x, y):
    return abs(round(random.randint(1, 3) * math.sin(x / 40) + y + 0.25))


def f(x): return round(((x * x) / 500) - 2 * x) + 500


def spawn():
    birds['here'] = True
    birds['direction'] = 1 if random.randint(0, 1) else -1
    birds['x'] = -40 if (birds['direction'] == 1) else windows_width + 40
    birds['y'] = random.randint(spawn_r_s, spawn_r_f)
    birds['size'] = random.randint(size_r_s, size_r_f)
    birds['speed'] = 1
    birds['fly'] = st_angle
    birds['k'] = 1


spawn()

while mainLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False
    screen.fill(windows_bgcolor)
    speed_man = 0.01

    body_2 = Rect((body_x, 275), (50, 100))
    head_2 = Rect((head_x, 245), (30, 30))

    pygame.draw.rect(screen, green, grass)
    pygame.draw.rect(screen, brown, house)
    pygame.draw.rect(screen, white, window)
    pygame.draw.polygon(screen, roof_color, roof)

    pygame.draw.ellipse(screen, bodile, body_1, 0)
    pygame.draw.ellipse(screen, bodile, body_2, 0)

    pygame.draw.circle(screen, bodile, (225, 260), 15, 0)
    pygame.draw.ellipse(screen, bodile, head_2, 0)

    pygame.draw.line(screen, bodile, (200, 305), (170, 340), 3)
    pygame.draw.line(screen, bodile, (250, 305), (280, 340), 3)
    pygame.draw.line(screen, bodile, (230, 340), (200, 400), 3)
    pygame.draw.line(screen, bodile, (230, 340), (260, 400), 3)

    pygame.draw.line(screen, bodile, (hand_1_x, 305), (hand_1_x - 30, 340), 3)
    pygame.draw.line(screen, bodile, (hand_2_x, 305), (hand_2_x + 30, 340), 3)
    pygame.draw.line(screen, bodile, (leg_x, 340), (leg_x - 30, 400), 3)
    pygame.draw.line(screen, bodile, (leg_x, 340), (leg_x + 30, 400), 3)

    # pygame.draw.line(screen, black, ())

    # pygame.draw.line()

    head_x += speed_man
    body_x += speed_man
    hand_1_x += speed_man
    hand_2_x += speed_man
    leg_x += speed_man
    if sun['x'] > windows_width:
        sun['x'] = 100

    pygame.draw.circle(screen, yellow, (sun['x'], f(sun['x'])), 50)
    sun['x'] += 1

    # pygame.draw()

    birds['y'] = bird_fly(birds['x'], birds['y'])

    if birds['y'] > 150:
        if (birds['fly'] >= 80) or (birds['fly'] <= 30):
            birds['k'] *= -1
        birds['fly'] += 5 * birds['k']

        if -40 <= birds['x'] <= windows_width + 40:
            birds['x'] += birds['speed'] * birds['direction']
        else:
            birds['x'] = -40 if birds['direction'] == 1 else windows_width + 40
        bird(birds['x'], birds['y'], birds['size'], birds['fly'])


    pygame.display.update()

pygame.quit()
# destroy data here
