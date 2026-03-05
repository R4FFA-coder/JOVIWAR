# Parametros padrao
import pygame

# ENTITY_CONFIG
EVENT_ENEMY = pygame.USEREVENT = 1

ENTITY_HEALTH = {'Level1_1': 999,
                 'Level1_2': 999,
                 'Level1_3': 999,
                 'Level1_4': 999,
                 'Level1_5': 999,
                 'Drone': 40,
                 'Player': 200}

ENTITY_SPEED = {'Level1_1': 0,
                'Level1_2': 1,
                'Level1_3': 2,
                'Level1_4': 3,
                'Level1_5': 4,
                'Drone': 6}
# COLOR
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# FONT
FONT_PATH = './font/FutureMillennium.ttf'
FONT_PATH_ITALLIC = './font/FutureMillennium Italic.ttf'
FONT_PATH_BOLD = './font/FutureMillennium Black.ttf'

# MENU OPTION
MENU_OPTION = ('NOVO JOGO',
               'RANKING',
               'SAIR')

# PATHS
BGD = './assets/MenuBG.jpg'
BGM = './assets/RuasdeSP.wav'
BGML1 = './assets/Samba.wav'
BGML2 = './assets/Labirinto.wav'
SCORE = './assets/Score.wav'
SHOOT = './assets/Shoot.wav'

# SPAWN TIMER
SPAWN_TIMER = 2000

# WINDOW
LARGURA = 800
ALTURA = 600
