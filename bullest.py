
from pygame.sprite import Sprite
import pygame

class Bullets(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullets, self).__init__()
        self.screen = screen
        # self.bullets = bullets

        # 创建子弹矩形初始位置（0,0,3,15）分别对应lef，top，宽，高
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx  # 设置中心点x轴坐标跟飞船一致
        self.rect.top = ship.rect.top  # 设置y轴坐标顶部跟飞船一致

        # 设置成小数进行计算
        self.top = float(self.rect.top)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.top -= self.speed_factor
        self.rect.top = self.top

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

def fire_bullet( ai_settings, screen, ship, bullets):
    pass