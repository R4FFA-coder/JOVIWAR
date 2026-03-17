import pygame
from src.Const import BGML1


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Scorebg.jpg').convert_alpha()
        self.rect = self.surf.get_rect()

    def salvar(self):
        pass

    def show_score(self):
        pygame.mixer_music.load(BGML1)
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.4)
        while True:
            pass
