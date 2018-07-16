import sys, pygame
import time
pygame.init()

def smoke():
    i = 0
    x = 170
    y = 380
    while i < 10:
        pygame.draw.ellipse(screen, grey, [x-i, y-3*i, 15, 20])
        pygame.draw.ellipse(screen, grey, [x+i, y-3*i, 15, 20])
        x, y = x-i, y-3*i
        time.sleep(0.25)
        pygame.draw.ellipse(screen, grey, [x+10, y-8, 15, 20])
        y -= 8
        pygame.display.update()
        i +=0.2
    pygame.display.flip()



##def UFO():
##    x01 = 650
##    y01 = 120
##    x02 = 665
##    y02 = 100
##    
##    while i < 30:
##        x_1 = 3(x - x01)+x01
##        y_1 = 3(y - y01)+y01
##        x_2 = 3(x - x02)+x02
##        x_2 = 3(y - y01)+y02
##        pygame.draw.ellipse(screen, light_green, [x_1, y_1, 60, 30])
##        pygame.draw.ellipse(screen, light_green, [x_2, y_2, 30, 40])
##        
        
    
size = 800, 680
red = 200, 26, 65
white = 255, 255, 255
roof = 255,0,0
light_green = 200, 255, 200
grey = 83, 80, 89
sky = 204, 204, 255
green = 0, 128, 0
house = 215, 110, 0
yellow = 247, 242, 42

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
milli = seconds = 0.0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        screen.fill(sky)
        pygame.draw.polygon(screen, green, [(0, 680),(0, 580),(800, 580), (800, 680)])    
        pygame.draw.polygon(screen, house, [(150, 580),(150, 450),(350, 450),(350, 580)])
        pygame.draw.polygon(screen, roof, [(150, 450),(350, 450),(250, 400)])
        pygame.draw.polygon(screen, sky, [(170, 500),(170, 470),(200, 470),(200, 500)])
        pygame.draw.polygon(screen, yellow, [(220, 580),(220, 510),(250, 510),(250, 580)])
        pygame.draw.polygon(screen, sky, [(270, 500),(270, 470),(300, 470),(300, 500)])
        pygame.draw.polygon(screen, roof, [(170, 450),(170, 400),(200, 400),(200, 450)])
        
        time.sleep(1)

        smoke()

        pygame.display.update()
    pygame.display.flip()
