from random import randint, random

import pygame

size = (1200, 600)

a, b = 70, 30
k = 0.1

house_color = (222, 184, 135)
roof_color = (165, 42, 42)
smoke_color = (160, 160, 160)
ufo_color = (130, 0, 150)
WHITE = (255, 255, 255)
GREEN = (124, 252, 0)

x_ufo, y_ufo = 400, -100
x_house, y_house = 800, 260
x_window = x_house + 50
y_window = y_house + 40
smoke = []

window = pygame.display.set_mode(size)
screen = pygame.Surface(size)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            break

    if y_ufo < 400:
        y_ufo += 0.3
        k += 0.001

    screen.fill((0, 0, 0))
    # UFO
    pygame.draw.ellipse(screen, ufo_color, (x_ufo - a * k, y_ufo, 2 * a * k, 2 * b * k))
    pygame.draw.circle(screen, ufo_color, (x_ufo, int(y_ufo)), int(k * b))

    # Дом
    pygame.draw.rect(screen, GREEN, (0, 500, 1200, 900))
    pygame.draw.rect(screen, house_color, (x_house, y_house + 80, 200, 200))
    pygame.draw.rect(screen, WHITE, (x_window, y_window + 75, 100, 100))
    pygame.draw.polygon(screen, roof_color,
                        ((x_house, y_house + 80), (x_house + 200, y_house + 80), (x_house + 100, y_house)))
    pygame.draw.rect(screen, roof_color, (x_house + 20, y_house, 40, 80))

    # Дым
    if len(smoke) < 500:
        smoke.append([x_house + 20, y_house, randint(5, 10)])
    for pos in range(len(smoke)):
        if smoke[pos][1] < y_house - 260:
            smoke[pos][1] = y_house
        else:
            smoke[pos][1] -= random()
            smoke[pos][0] += random() * 2 - 1
            if smoke[pos][0] < x_house + 10 or smoke[pos][0] > x_house + 20 + 50:
                smoke[pos][0] = x_house + 20 + 20
            pygame.draw.circle(screen, smoke_color, (int(smoke[pos][0]), int(smoke[pos][1])), smoke[pos][2])

    window.blit(screen, (0, 0))
    pygame.display.flip()
