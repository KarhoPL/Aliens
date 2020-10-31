import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_UP:
        ship.moving_top = True
    if event.key == pygame.K_DOWN:
        ship.moving_bottom = True   
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ship):
    if event.key == pygame.K_UP:
        ship.moving_top = False
    if event.key == pygame.K_DOWN:
        ship.moving_bottom = False

def fire_bullet(ai_settings, screen, ship, bullets):
    '''wystrzelenie pocisku jeżeli nie przekroczono ustalonego limitu'''
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen, ship, bullets):
    #odświeżenie ekranu po każdej iteracji pętli
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullets()
    ship.blitme()
    pygame.display.flip()

def update_bullets(bullets,ai_settings):
    bullets.update()
    # deleting bullets that are out of screen
    for bullet in bullets.copy():
        if bullet.rect.left > ai_settings.screen_width :
            bullets.remove(bullet)
