import sys
import pygame
# from PIL import Im
import sound
from bullest import Bullets
# import

class Controls(object):
    def __init__(self, screen_ships_speed_factor, screen):
        self.is_k_down = False
        self.is_k_up = False
        self.is_k_left = False
        self.is_k_right = False
        self.is_k_space = False
        self.ship_control_speed_factor = screen_ships_speed_factor
        self.screen = screen
        self.screen_static = screen
        self.ships_x = self.screen.get_rect().centerx
        self.ships_y = self.screen.get_rect().bottom
        # self.sound = sound.Sound()

    def ships_ctrl(self,ai_settings, screen, ship,bullets):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.is_k_down = True
                if event.key == pygame.K_UP:
                    self.is_k_up = True
                if event.key == pygame.K_LEFT:
                    self.is_k_left = True
                if event.key == pygame.K_RIGHT:
                    self.is_k_right = True
                if event.key == pygame.K_SPACE:
                    self.is_k_space = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.is_k_down = False
                if event.key == pygame.K_UP:
                    self.is_k_up = False
                if event.key == pygame.K_LEFT:
                    self.is_k_left = False
                if event.key == pygame.K_RIGHT:
                    self.is_k_right = False
                if event.key == pygame.K_SPACE:
                    self.is_k_space = False

        if self.is_k_space == True:
            new_bullet = Bullets(ai_settings, screen, ship)
            bullets.add(new_bullet)
            ship.ship_image.trans
            # self.sound.sound_play()
        else:
            # self.sound.sound_stop
            pass
        if self.is_k_right == True:
            self.ships_x += self.ship_control_speed_factor
        if self.is_k_left == True:
            self.ships_x -= self.ship_control_speed_factor
        if self.is_k_up == True:
            self.ships_y -= self.ship_control_speed_factor
        if self.is_k_down == True:
            self.ships_y += self.ship_control_speed_factor

        if self.ships_x < 0:
            self.ships_x =                      \
            (2*self.screen.get_rect().centerx - abs(self.ships_x) % (2*self.screen.get_rect().centerx))
        if self.ships_x >= 0:
            self.ships_x = self.ships_x % (2*self.screen.get_rect().centerx)
        if self.ships_y < 0:
            self.ships_y =                      \
            (self.screen.get_rect().bottom - abs(self.ships_y) % self.screen.get_rect().bottom)
        if self.ships_y >= 0:
            self.ships_y = self.ships_y % self.screen.get_rect().bottom
        return (self.ships_x, self.ships_y)