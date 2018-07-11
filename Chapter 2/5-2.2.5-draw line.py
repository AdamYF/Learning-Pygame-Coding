# 线条形状更加复杂，因为需要提供起点和终点

import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Lines")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 0))

    # draw the line
    color = 100, 255, 200
    width = 8
    pygame.draw.line(screen, color, (100, 100), (500, 400), width)
    # pygame.draw.line(screen, color, (400, 100), (100, 450), width)

    pygame.display.update()