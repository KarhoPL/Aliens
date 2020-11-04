import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #inicjacja gry
    pygame.init()
    ai_settings = Settings()
    #utworzenie obiektu ekranu
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Attack of Aliens")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # utworzenie floty obcych
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # rozpoczęcie głównej pętli gry
    while True:
        #ta pętla będzie działać po każdym "wydarzeniu" czyli kliknięciu klawisza lub myszy
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings,screen,ship, aliens, bullets)

run_game()
