# Parametros padrao
import pygame
# ENTITY_CONFIG
EVENT_ENEMY = pygame.USEREVENT = 1

ENTITY_DAMAGE = {'Level1_1': 0,
                 'Level1_2': 0,
                 'Level1_3': 0,
                 'Level1_4': 0,
                 'Level1_5': 0,
                 'Drone': 1,
                 'Player1': 1,
                 'PlayerShot': 1,
                 'EnemyShot': 1}

ENTITY_HEALTH = {'Level1_1': 999,
                 'Level1_2': 999,
                 'Level1_3': 999,
                 'Level1_4': 999,
                 'Level1_5': 999,
                 'Player1': 6,
                 'Drone': 10,
                 'PlayerShot': 1,
                 'EnemyShot': 1}

ENTITY_SCORE = {'Level1_1': 0,
                 'Level1_2': 0,
                 'Level1_3': 0,
                 'Level1_4': 0,
                 'Level1_5': 0,
                 'Drone': 5,
                 'Player1': 0,
                 'PlayerShot': 0,
                 'EnemyShot': 0}

ENTITY_SPEED = {'Level1_1': 0,
                'Level1_2': 1,
                'Level1_3': 2,
                'Level1_4': 3,
                'Level1_5': 4,
                'Drone': 3,
                'Player1': 0,
                'PlayerShot': 20,
                'EnemyShot': 11}
# COLOR
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
SILVER = (192,192,192)
ORANGE = (255,148,0)

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
