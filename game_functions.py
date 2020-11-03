import sys
import pygame
from drop import Drop
from bullet import Bullet
from random import randint
from datetime import datetime

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True   
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def fire_bullet(ai_settings, screen, ship, bullets):
    '''wystrzelenie pocisku jeżeli nie przekroczono ustalonego limitu'''
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen, ship, drops, bullets):
    #odświeżenie ekranu po każdej iteracji pętli
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullets()
    ship.blitme()
    drops.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    # deleting bullets that are out of screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <0 :
            bullets.remove(bullet)


def create_drop(ai_settings, screen, drops, ship):
    drop = Drop(ai_settings, screen)
    drop.x = randint(ship.rect.width,ai_settings.screen_width-ship.rect.width) 
    drop.rect.x = drop.x
    drop.rect.y= 0
    drops.add(drop)

def check_fleet_edges(ai_settings, drops, ship):
    for drop in drops.sprites():
        if drop.check_edges(ship):
            drops.remove(drop)
            break

def update_drops(ai_settings, drops,ship):
    check_fleet_edges(ai_settings, drops,ship)
    drops.update()

def check_if_add_new_drop(drops):
    positions = []
    for drop in drops:
        if drop.rect.y < drop.rect.height*1.5:
            positions.append(drop.rect.y)
    if positions:
        return False
    return True