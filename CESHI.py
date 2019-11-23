# # import pygame
# # from pygame import Rect
# # screen_rect_width = 1200
# # screen_rect_height = 800
# # screen_set_mode = pygame.display.set_mode((screen_rect_width, screen_rect_height))
# #
# # while True:
# #     screen_set_mode.fill((230, 230, 230))
# #
# #     pygame.draw.rect(screen_set_mode, (50, 150, 50, 180), \
# #                  Rect(screen_rect_width / 2, screen_rect_height - 100, 20, 25))
# #     pygame.display.flip()
# # b = 1
# # a = (b = 2)
# # print()
# import os
# import sys
# getcwd =  os.getcwd() #获取当前工作目录路径
# # path_getcwd = os.path.getcwd('.') #获取当前工作目录路径
# # print os.path.abspath('test.txt') #获取当前目录文件下的工作目录路径
# # print os.path.abspath('..') #获取当前工作的父目录 ！注意是父目录路径
# abspath = os.path.abspath(os.curdir) #获取当前工作目录路径
# print('getcwd:{}'.format(getcwd),'abspath:{}'.format(abspath))
# i = len(sys.argv)
# print('i = :{}'.format(i))
# if i == 2:
#     file_dir = sys.argv[1]
# elif i == 1:
#     file_dir = getcwd
# for roots, dirs, files in os.walk(file_dir):
#     # print('roots:{}'.format(roots))
#     # print('dirs:{}'.format(dirs))
#     print('files:{}'.format(files).split('.pyc'))
import itchat

import time

@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print("收到一条信息：",msg.text)

if __name__ == '__main__':
    itchat.auto_login()
    time.sleep(5)
    itchat.send("文件助手你好哦", toUserName="filehelper")
    itchat.run()

