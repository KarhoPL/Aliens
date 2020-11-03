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
        self.image = pygame.image.load('images/drop.png')
        self.rect = self.image.get_rect()

        # placeing new alien in upper left edge 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storing exact aliens position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self, ship):
        #screen_rect = self.screen.get_rect()
        ship_rect = ship.rect
        if self.rect.bottom >= ship_rect.top:
            return True

    def update(self):
        self.y += self.ai_settings.fleet_drop_speed
        self.rect.y = self.y