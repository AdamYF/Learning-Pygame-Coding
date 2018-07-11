# 弧线形状也比较复杂，因为它需要额外的参数
# 需要提供一个矩形来表示弧形的边界，包括左上角的位置，宽度和高度
# 然后还要提供开始角度和结束角度，通常倾向以度为单位来考量，并通过math.radians()函数来将弧度转换为角度

# 由于需要使用弧度转换函数，还要引入math库
import math
import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Arcs")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 0))

    # draw the arc
    color = 255, 0, 255
    position = 200, 150, 200, 200
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    width = 8
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

    pygame.display.update()