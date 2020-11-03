import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    """ Class presenting simple drop """
    def __init__(self, ai_settings, screen):
        """Initialization of drop and defining it's position"""
        super(Drop,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # uploading drop image and defining its attribute rect
        self.image = pygame.image.load('images/drop.png')
        self.rect = self.image.get_rect()

        # placeing new drop in upper left edge 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storing exact drops position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self, ship):
        ship_rect = ship.rect
        if self.rect.bottom >= ship_rect.top:
            return True

    def update(self):
        self.y += self.ai_settings.fleet_drop_speed
        self.rect.y = self.y