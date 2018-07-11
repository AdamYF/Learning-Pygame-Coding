import random
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
    count = 0

    while count < 10:
        pygame.draw.line(screen, color, (random.randint(0, 600), random.randint(0, 500)), (random.randint(0, 600), random.randint(0, 500)), width)
        count += 1

    pygame.display.update()