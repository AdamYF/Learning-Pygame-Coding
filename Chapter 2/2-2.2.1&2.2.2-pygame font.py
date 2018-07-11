# 引入pygame库并引入所有的常量
import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 500))

# 创建一个字体对象用于在窗口中输出文本
myfont = pygame.font.Font(None, 60)

white = 255, 255, 255
blue = 0, 0, 255
textImage = myfont.render("Hello Pygame", True, white)

# # 第一版：只是简单显示一下窗口就关闭了
# screen.fill(blue)
# screen.blit(textImage, (100, 100))
# pygame.display.update()

# 第二版：加上循环和用户输入用来退出
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill(blue)
    screen.blit(textImage, (100, 100))

    pygame.display.update()