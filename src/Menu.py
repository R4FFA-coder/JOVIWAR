import pygame
from sys import *
from pygame.locals import *
from src.Const import *

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(BGD).convert_alpha()
        self.rect = self.surf.get_rect()

    def run(self):
        menu_option = 0
        pygame.display.set_caption('JOVIWAR 0.1')
        pygame.mixer_music.load(BGM)  # Metodo para carregar musica
        pygame.mixer_music.play(-1, fade_ms=1000)  # metodo que coloca a musica em loop
        self.window.blit(self.surf, self.rect)
        self.menu_texto(80, 'JOVI', WHITE, (LARGURA // 2 - 30, 127))
        self.menu_texto(55, 'WAR', BLUE, (LARGURA // 2 + 60, 179))
        self.instrucoes(20, (LARGURA - 200, 450))

        while True:
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_texto(30, MENU_OPTION[i], BLUE, (255 - i * 19, 300 + 40 * i))
                else:
                    self.menu_texto(30, MENU_OPTION[i], BLACK, (255 - i * 19, 300 + 40 * i))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.key == K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == K_RETURN:
                        return MENU_OPTION[menu_option]



    def menu_texto(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Metodo que cria texto para o menu
            A Logica é a mesma de criar uma imagem de fundo, um texto sera como uma imagem projetada em um retangulo que criaremos
        """
        text_font = pygame.font.Font(FONT_PATH, size=text_size)  # padroniza uma fonte e o tamanho
        text_surf = text_font.render(text, True, text_color).convert_alpha()  # Renderiza o texto
        text_rect = text_surf.get_rect(center=text_center_pos)  # Desenha um retangulo que será a área em que o texto ocupará
        self.window.blit(source=text_surf, dest=text_rect)  # carrega o texto e imprime na area do retangulo

    def instrucoes(self, text_size: int, text_center_pos: tuple):
        text_font = pygame.font.Font(FONT_PATH_ITALLIC, size=text_size)
        text_surf = text_font.render('(SPACE) - pular', True, YELLOW).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

        text_center_pos = (LARGURA - 203, 470)
        text_surf2 = text_font.render('(CTRL) - Atirar', True, YELLOW).convert_alpha()
        text_rect2 = text_surf2.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf2, dest=text_rect2)
