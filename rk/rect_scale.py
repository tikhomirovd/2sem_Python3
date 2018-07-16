import sys
from pygame import *

# домик с трубой, из которой идет дым
# и летающая тарелка приземляется
# масштабируется при этом
# она состоит из окружности и овала

clock = time.Clock()
size = width, height = 500, 500
screen = display.set_mode(size)
display.set_caption('Catch Birds')

BLACK = 0, 0, 0
WHITE = 255, 255, 255
BLUE = 14, 33, 137
GREEN = 44, 144, 44
RED = 144, 44, 44
YELLOW = 204, 204, 44

'''Поворот вокруг центра:
x = (x - xc) * cos(angle) + (y - yc) * sin(angle) + xc
y = (y - yc) * cos(angle) + (x - xc) * sin(angle) + yc

Вращение по кругу:
X = x * cos(a) - y * sin(a); Y = y * cos(a) + x * sin(a);

Масштабирование:
x = k * (x - xc) + xc
y = k * (y - yc) + yc
'''
x1 = 100; y1 = 100; x2 = 400; y2 = 100
x3 = 100; y3 = 380; x4 = 400; y4 = 380; k = 1.02; xc =250; yc = 390
while 1:
    clock.tick(5)
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    screen.fill(WHITE)
    if (x1 < 400):
        draw.polygon(screen, BLACK, ((x1, y1), (x2, y2), (x4, y4), (x3, y3)), 5)
        x1 = k * (x1 - xc) + xc
        y1 = k * (y1 - yc) + yc
        x2 = k * (x2 - xc) + xc
        y2 = k * (y2 - yc) + yc
        x3 = k * (x3 - xc) + xc
        y3 = k * (y3 - yc) + yc
        x4 = k * (x4 - xc) + xc
        y4 = k * (y4 - yc) + yc
        display.flip()

    display.flip()