import pygame

class Ship():
    def __init__(self,screen):
        self.screen = screen    

        #utworzenie statku kosmicznego i jego prostokąta
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #każdy nowy statek kosmiczny pojawia się na dole ekranu.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
                
    def blitme(self):
        #wyświetlanie statku kosmicznego w jego aktualnym położeniu
        self.screen.blit(self.image, self.rect)
