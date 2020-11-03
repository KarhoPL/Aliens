import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Chasing the rain")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    drops = Group()
    gf.create_drop(ai_settings, screen, drops, ship)
    while True:
        if gf.check_if_add_new_drop(drops): gf.create_drop(ai_settings, screen, drops, ship)
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_drops(ai_settings, drops, ship)
        gf.update_screen(ai_settings,screen,ship, drops, bullets)

run_game()
