from src.Const import *
from src.Level import Level
from src.Menu import Menu
from sys import exit
from src.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(LARGURA, ALTURA))
    def run(self):
        relogio = pygame.time.Clock()
        while True:
            score = Score(self.window)
            relogio.tick(30)
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return in [MENU_OPTION[0]]:
                level = Level(self.window, 'Level1')
                level_return = level.run()
            if menu_return in [MENU_OPTION[1]]:
                level_infinito = Level(self.window, 'Level_infinite')
                level_infinito.run()
            elif menu_return in [MENU_OPTION[2]]:
                # score = Score(self.window)
                # score.show_score()
                pass
            elif menu_return in [MENU_OPTION[3]]:
                pygame.quit()
                exit()