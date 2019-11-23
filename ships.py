import pygame
from controls import Controls

class Ships(object):
    def __init__(self, screen, screen_ships_speed_factor):
        self.screen = screen
        self.screen_ships_speed_factor = screen_ships_speed_factor
        """load image and get rectangle"""
        self.ship_image = pygame.image.load("images/playerShip1_orange.png")
        self.rect = self.ship_image.get_rect()
        self.ships_control = Controls(self.screen_ships_speed_factor, self.screen)
        # Ship settings.

    def ships_show(self,ai_settings, screen, ship,bullets):
        self.rect.centerx = self.ships_control.ships_ctrl(ai_settings, screen, ship,bullets)[0]
        self.rect.bottom = self.ships_control.ships_ctrl(ai_settings, screen, ship,bullets)[1]

        self.screen.blit(self.ship_image, self.rect)


