import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen    
        self.ai_settings = ai_settings

        #utworzenie statku kosmicznego i jego prostokąta
        self.image = pygame.image.load('images/ship_side.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #każdy nowy statek kosmiczny pojawia się na dole ekranu.
        self.rect.centery = self.screen_rect.centery
        #self.rect.left = self.screen_rect.left

        self.center = float(self.rect.centery)

        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        if self.moving_top and self.rect.top >self.screen_rect.top:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
        self.rect.centery = self.center
                
    def blitme(self):
        #wyświetlanie statku kosmicznego w jego aktualnym położeniu
        self.screen.blit(self.image, self.rect)
