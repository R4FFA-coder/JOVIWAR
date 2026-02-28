import os.path

import pygame
from src.Const import *
from src.Level import Level
from src.Menu import Menu
from sys import exit

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(LARGURA, ALTURA))
    def run(self):
        relogio = pygame.time.Clock()
        while True:
            relogio.tick(30)
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return in [MENU_OPTION[0]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return in [MENU_OPTION[1]]:
                pass
            elif menu_return in [MENU_OPTION[2]]:
                pygame.quit()
                exit()