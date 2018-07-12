import sys, random, math, pygame
from pygame.locals import *
################################################
# # 要使用pygame.gfxdraw的函数的话必须单独import
# from pygame.gfxdraw import *
################################################

class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # X property
    def getx(self):
        return self.__x
    def setx(self, x):
        self.__x = x
    x = property(getx, setx)

    # Y property
    def gety(self):
        return self.__y
    def sety(self, y):
        self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
            ",Y:" + "{:.0f}".format(self.__y) + "}"

def print_text(font, x, y, text, color = (255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

def wrap_angle(angle):
    return angle % 360

# main program begins
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Orbit Demo")
font = pygame.font.Font(None, 18)

# load bitmaps
# 原本找不太到合适的背景，所以用gfxdraw.pixel()直接画了
# 后来发现有背景刷新的问题，于是又找了个图凑合了
# space = pygame.image.load("space.png").convert()
space = pygame.image.load("Chapter 6\\space.jpeg").convert()
space = pygame.transform.smoothscale(space, (800, 600))
# 下面的都是自己随便找了个png代替的
planet = pygame.image.load("Chapter 6\\planet2.png").convert_alpha()
ship = pygame.image.load("Chapter 6\\freelance.png").convert_alpha()
width, height = ship.get_size()
ship = pygame.transform.smoothscale(ship, (width * 2 // 3, height * 2 // 3))

radius = 250
angle = 0.0
pos = Point(0, 0)
old_pos = Point(0, 0)
angular_speed = 0.1
################################################
# back_x = random.randint(0, 800)
# back_y = random.randint(0, 600)
# back_count = 0
# white = 255, 255, 255
################################################

# repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_EQUALS:
                angular_speed += 0.01
            elif event.key == pygame.K_MINUS:
                angular_speed -= 0.01

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    # draw background
    screen.blit(space, (0, 0))
################################################
    # # 由于不加载位图来作为背景的话，会留下之前飞船的痕迹
    # # 同时由于刷新速度非常快，会导致星空背景像雪花电视
    # # 所以这段代码还是屏蔽了
    # screen.fill((0, 0, 0))
    # while back_count < 500:
    #     back_x = random.randint(0, 800)
    #     back_y = random.randint(0, 600)
    #     pygame.gfxdraw.pixel(screen, back_x, back_y, white)
    #     back_count += 1
################################################

    width, height = planet.get_size()
    screen.blit(planet, (400 - width / 2, 300 - height / 2))

    # move the ship
    angle = wrap_angle(angle - angular_speed)
    pos.x = math.sin(math.radians(angle)) * radius
    pos.y = math.cos(math.radians(angle)) * radius
    # rotate the ship
    delta_x = pos.x - old_pos.x
    delta_y = pos.y - old_pos.y
    rangle = math.atan2(delta_y, delta_x)
    rangled = wrap_angle(-math.degrees(rangle))
    scratch_ship = pygame.transform.rotate(ship, rangled)

    # draw the scratched ship
    width, height = scratch_ship.get_size()
    x = 400 + pos.x - width // 2
    y = 300 + pos.y - height // 2
    screen.blit(scratch_ship, (x, y))

    print_text(font, 0, 0, "Orbit: " + "{:.0f}".format(angle))
    print_text(font, 0, 20, "Rotation: " + "{:.2f}".format(rangle))
    print_text(font, 0, 40, "Position: " + str(pos))
    print_text(font, 0, 60, "Old Pos: " + str(old_pos))
    print_text(font, 0, 80, "Angular Speed : " + "{:.2f}".format(angular_speed))

    pygame.display.update()

    # remember the old position
    old_pos.x = pos.x
    old_pos.y = pos.y
    # back_count = 0