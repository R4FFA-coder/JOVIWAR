from random import randint
import pygame
from src.Const import WHITE, LARGURA, ALTURA

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos_x: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/Plataforma2-1.png')
        self.image = pygame.transform.scale(self.image, (48 * 2 + 4, 48 * 2 + 4))
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA - 70
        self.rect.x = pos_x * 100

    def update(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.rect.left = LARGURA

            # MEUS PLANOS ORIGINAL ERA TER UM SISTEMA DE PLATAFORMA COM ALTURA VARIADA PARA DAR UMA DIFICULDADE
            # POREM AINDA ESTOU APRENDENDO A LÓGICA PARA FAZER O SISTEMA DE COLISÃO, NÃO DESISTI, FUTURAMENTE
            # FAREI DO JEITO QUE EU SEMPRE PRETENDI

            # if Platform.count_platform % 10 == 0:
            #     if Platform.count_platform > 5:
            #         Platform.current_y = randint(350, ALTURA - 50)
            #     else:
            #         Platform.current_y = ALTURA - 70

            # self.rect.y = Platform.current_y