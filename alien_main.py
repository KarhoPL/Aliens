import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf

def run_game():
    #inicjacja gry
    pygame.init()
    ai_settings = Settings()
    #utworzenie obiektu ekranu
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Attack of Aliens")
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # utworzenie floty obcych
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # rozpoczęcie głównej pętli gry
    while True:
        gf.check_events(ai_settings, screen, stats, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings,screen,ship, aliens, bullets)

run_game()
