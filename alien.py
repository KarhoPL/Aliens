import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class presenting simple alien """
    def __init__(self, ai_settings, screen):
        """Initialization of alien and defining it's position"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # uploading alien image and defining its attribute rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # placeing new alien in upper left edge 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storing exact aliens position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = self.x