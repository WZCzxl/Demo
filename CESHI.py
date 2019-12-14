import pygame
import sys
import random
import math

pygame.init()

SIZE = WIDTH, HEIGHT = 200, 400
BACKGROUND_COLOR = (230, 255, 230)

screen = pygame.display.set_mode(SIZE)
leaves = []


class Leaf(object):
    def __init__(self, pos=[10, 10], speed=[1, 1]):
        self.imageSrc = pygame.image.load("images/bolt_gold.png")
        self.rect = self.imageSrc.get_rect()
        self.image = self.imageSrc
        self.speed = speed
        self.angle = 0
        self.pos = pos
        self.rect = self.rect.move(pos[0], pos[1])

    def move(self):
        self.rect = self.rect.move(self.speed[0], self.speed[1])
        new_rect = self.image.get_rect()
        new_rect.left, new_rect.top = self.rect.left, self.rect.top
        if new_rect.left < 0 or new_rect.right > WIDTH:
            self.speed[0] = -self.speed[0]
            if new_rect.right > WIDTH:
                self.rect.left = WIDTH - new_rect.width
            if new_rect.left < 0:
                self.rect.left = 0
        if new_rect.top > HEIGHT:
            self.rect.bottom = 0

    def draw(self):
        screen.blit(self.image, self.rect)

    def rotate(self):
        self.image = pygame.transform.rotate(self.imageSrc, self.angle)
        self.angle += random.randint(1, 5)
        if math.fabs(self.angle) == 360:
            self.angle = 0


def init():
    for i in range(0, 5):
        leaf = Leaf([random.randint(50, WIDTH - 50), random.randint(30, HEIGHT)],
                    [random.randint(1, 2), random.randint(1, 2)])
        leaf.move()
        leaves.append(leaf)


clock = pygame.time.Clock()
init()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    # 将旋转后的图象，渲染到新矩形里
    for item in leaves:
        item.rotate()
        item.move()
        item.draw()

    # 正式渲染
    pygame.display.update()
    # 控制帧数<=100
    clock.tick(100)