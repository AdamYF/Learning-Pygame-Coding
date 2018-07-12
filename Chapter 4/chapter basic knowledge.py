import pygame

# 默认情况下，Pygame不会重复的响应一个持续被按下的键
# 只会在第一次按下的时候发送一个事件
# 为了能够重复响应，需要添加pygame.key.set_repeat(n)函数
# 其中的n是以毫秒为单位的重复值，参数不可遗漏
pygame.key.set_repeat(10)

# Pygame支持的鼠标事件包括：MOUSEMOTION、MOUSEBUTTONUP和MOUSEBUTTONDOWN
# MOUSEMOTION事件包括event.pos、event.rel和event.buttons属性
for event in pygame.event.get():
    if event.type == MOUSEMOTION:
        mouse_x, mouse_y = event.pos
        move_x, move_y = event.rel
# MOUSEBUTTONUP和MOUSEBUTTONDOWN事件包括event.pos和event.buttons属性
for event in pygame.event.get():
    if event.type == MOUSEBUTTONUP:
        move_up = event.button
        mouse_up_x, mouse_up_y = event.pos
    if event.type == MOUSEBUTTONDOWN:
        move_down = event.button
        mouse_down_x, mouse_down_y = event.pos

# Pygame中使用pygame.key.get_pressed()来轮询键盘接口
# 该方法返回布尔值的一个列表，使用每个键的ASCII编码来作为索引
# 一次轮询所有的键的好处是，不必遍历事件系统就可以检测多个键的按下
# 因此可以使用如下代码来代替旧的时间处理程序代码，以检测Escape键
keys = pygame.key.get_pressed()
if keys[K_ESCAPE]:
    sys.exit()