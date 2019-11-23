
import sys
import os
import pygame
from pygame import Rect
from setting import Setting
import ships
from time import sleep
from ships import Ships
from pygame.sprite import Group
from bullest import Bullets
from stones import Stones
import tkinter
import tkinter.messagebox
import sound

screen_rect_width = 1200
screen_rect_height = 800

def run_game():

    """初始化游戏并创建一个display obj"""
    pygame.init()
    attacker = None
    cllisions = False
    root = tkinter.Tk()
    root.withdraw()  # 隐藏
    # pygame.mouse.set_visible(False)

    screen_set_mode = pygame.display.set_mode((screen_rect_width,screen_rect_height))
    pygame.display.set_caption(("小丽--1号").title())
    screen_setting = Setting()
    screen_ships_speed_factor = screen_setting.ships_speed_factor
    screen_ships = ships.Ships(screen_set_mode, screen_ships_speed_factor)
    """创建子弹编组"""
    bullets_group = Group()
    stones_group = Group()
    cycle_time = 0
    blood_full = 200
    blood = blood_full
    # rect = Rect（0，0，width，height）
    sounds = sound.Sound()
    sound_to_stop_num = 20

    while True:
        """实时刷新绘图"""
        screen_set_mode.fill((230, 230, 230))
        screen_ships.ships_show(screen_setting, screen_set_mode, screen_ships,bullets_group)
        """更新子弹位置"""
        for bullet in bullets_group.sprites():
            bullet.update()  # 子弹组每个成员执行self.update()操作
            if bullet.rect.bottom <= 0:  # 子弹出界 删除
                bullets_group.remove(bullet)
            bullet.draw_bullet()  # 绘制子弹

        if cycle_time % 100 == 0:
            if len(stones_group) <= 50:
                new_stone = Stones(screen_set_mode)
                stones_group.add(new_stone)
        for stone in stones_group.sprites():
            stone.stones_update()
            if stone.rect.bottom >= (screen_rect_height - 200):
                stones_group.remove(stone)
        cycle_time += 1
        #首先用pygame.sprite.spritecollideany来判断ship是否与
        # 任意的stone产生了碰撞，如果产生碰撞，
        # 则再使用pygame.sprite.collide_circle_ratio缩小检测范围做一次检测，
        attacker = pygame.sprite.spritecollideany(screen_ships, stones_group)
        if attacker != None:
            if pygame.sprite.collide_circle_ratio(0.65)(screen_ships, attacker):
                blood -= 1
                stones_group.remove(attacker)

        if blood < 0:
            #os.system("pause")
            tkinter.messagebox.showinfo("提示", "你输了~~")
            blood = blood_full
        # 检测是否STONE与子弹有碰撞，有就删除他们
        cllisions = pygame.sprite.groupcollide(bullets_group, stones_group, True, True)
        #每次击中都把声音播放时间延长到30次循环，保证能听到声音
        if cllisions:
            sounds.sound_play()
            sound_to_stop_num = 38
        else:
            sound_to_stop_num -= 1
            if sound_to_stop_num == 0:
                sounds.sound_stop()
        # 每次击中都把声音播放时间延长到30次循环，保证能听到声音
        print(type(cllisions))
        print("cllisions:{}".format(cllisions))
        # 绘制玩家血量条
        pygame.draw.rect(screen_set_mode, (50, 150, 50, 180), \
                         Rect(screen_rect_width/2, screen_rect_height - 100, blood, 25))
        pygame.draw.rect(screen_set_mode, (100, 200, 100, 180), \
                         Rect(screen_rect_width/2, screen_rect_height - 100, blood_full, 25), 2)
        pygame.display.flip()

run_game()