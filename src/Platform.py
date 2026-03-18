import pygame
from src.Const import LARGURA, ALTURA

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos_x: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/Plataforma2.png')
        self.image = pygame.transform.scale(self.image, (48 * 2 + 4, 48 * 2 + 4))
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA - 70
        self.rect.x = pos_x * 100

    def update(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.rect.left = LARGURA