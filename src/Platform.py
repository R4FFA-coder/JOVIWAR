import pygame

from src.Const import WHITE, LARGURA, ALTURA


class Platform:
    def __init__(self, pos_X: int):
        self.surf = pygame.image.load('./assets/Plataforma1.png')
        self.rect = self.surf.get_rect()
        self.rect.y = ALTURA - 80
        self.rect.x = pos_X * 128

    def move(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -= 10

