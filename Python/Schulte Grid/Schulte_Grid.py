import pygame
import sys
import random
import time
import game_functions as gf
from button import Button
from settings import Setting


pygame.init()
clock = pygame.time.Clock()
setting = Setting()
pygame.display.set_caption(setting.game_name)
gf.form_choose_interface(setting)

try:
    while True:
        clock.tick(60)
        
        gf.check_events(setting)
        gf.update_screen(setting)
        gf.update_time(setting)
        gf.draw_game(setting)
        
        pygame.display.flip()

except BaseException as err:
    gf.except_action_1(err)
