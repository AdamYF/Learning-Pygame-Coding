import pygame

# pygame中有一个类叫做Surface，我们之前建立的窗口其实都属于Surface类
# 在Pygame中，一个位图也叫做Surface

# 加载位图使用pygame.image.load()函数
# 对于太空背景图，可以加载位图，也可以使用pygame.gfxdraw.pixel()函数来做到
space = pygame.image.load("space.png").convert()
# 最后的convert()函数将位图转换为程序窗口的本地颜色深度，如果加载时没有转换，绘制时也必须
# 该函数还有另一种形式convert_alpha()，在加载必须使用透明度方式绘制的前景对象时，需要使用这种形式