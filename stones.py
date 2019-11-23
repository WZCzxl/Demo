import pygame
from pygame.sprite import Sprite
import random
class Stones(Sprite):
    def __init__(self, screen):
        super(Stones,self).__init__()
        self.screen = screen
        """load image and get rectangle"""
        self.stones_image = pygame.image.load("images/meteorBrown_small1.png")
        self.rect = self.stones_image.get_rect()
        self.rect.centerx = random.randrange(0, 2*self.screen.get_rect().centerx)
        self.rect.bottom = 0

    def stones_update(self):
        self.rect.bottom += 1

        self.screen.blit(self.stones_image, self.rect)



