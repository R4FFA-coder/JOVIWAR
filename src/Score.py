from datetime import datetime
from sys import exit
import pygame.display
from pygame.locals import *
from src.Const import *
from src.DBProxy import DBProxy

class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Scorebg.jpg').convert_alpha()
        self.rect = self.surf.get_rect()

    def salvar(self, score):
        name = ''
        if score > 0:
            name_text = 'DIGITE SEU NOME (minimo 3 caracteres)'
            pygame.mixer_music.load(BGML1)
            pygame.mixer_music.play(-1)
            pygame.mixer_music.set_volume(0.4)
            self.window.blit(self.surf, self.rect)
            db_proxy = DBProxy('DBScore')
            while True:
                self.score_text('FIM DE JOGO!', 55, (LARGURA // 2, 100), YELLOW, FONT_PATH_BOLD)
                self.score_text(name_text, 25, (LARGURA // 2, ALTURA // 2 - 70), WHITE, FONT_PATH)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == KEYDOWN:
                        if event.key == K_RETURN and len(name) > 2:
                            db_proxy.save({'name': name, 'score': score, 'data': get_formatted_date()})
                            self.show()
                        elif event.key == K_BACKSPACE:
                            name = name[:-1]
                        else:
                            if len(name) < 8:
                                if event.key == K_RETURN:
                                    continue
                                name += event.unicode
                self.score_text(name, 20, (LARGURA // 2, ALTURA // 2), WHITE, FONT_PATH_ITALLIC)

                pygame.display.flip()

    def show(self):
        pygame.mixer_music.load(BGML1)
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.4)
        self.window.blit(self.surf, self.rect)
        self.score_text('TOP 10 RANK', 75, (LARGURA //2, 70), GREEN, FONT_PATH)
        self.score_text('NOME   PONTOS      DATA       ', 30, (LARGURA //2, 150), YELLOW, FONT_PATH_ITALLIC)
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for i in list_score:
            id_, nome, pontos, data = i
            self.score_text(f'{nome}    {pontos :05d}    {data}', 25, (SCORE_POS[list_score.index(i)]), GREEN, FONT_PATH, (12,12,12))
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()

            pygame.display.flip()

    def score_text(self, text: str, size: int, text_center_pos: tuple, color, font, background=None):
        text_font = pygame.font.Font(font, size=size)
        text_surf = text_font.render(text, True, color, background).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H:%M')
    current_date = current_datetime.strftime('%d/%m/%y')
    return f'{current_time} - {current_date}'
