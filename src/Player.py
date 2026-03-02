import pygame
import os

from src.Const import ALTURA


class Player(pygame.sprite.Sprite):
    def __init__(self, opcao: int):
        pygame.sprite.Sprite.__init__(self)
        self.nome_sprite = None
        self.opcao = opcao
        self.images_player = []
        self.diretorio_principal = os.path.dirname(__file__)
        self.diretorio_assets = os.path.join(self.diretorio_principal, 'assets')
        self.diretorio_charPlayer = os.path.join(self.diretorio_principal, '../chars/player1')

        match opcao:
            case 1:
                self.nome_sprite = 'Run2'

            case 2:
                self.nome_sprite = 'Player2'

        self.sprite_sheet = pygame.image.load(
            os.path.join(self.diretorio_charPlayer, self.nome_sprite + '.png')).convert_alpha()
        if opcao == 1:
            for c in range(6):
                img = self.sprite_sheet.subsurface((48 * c, 0), (48, 48))
                img = pygame.transform.scale(img, (48 * 1.5, 48 * 1.5))
                self.images_player.append(img)
        elif opcao == 2:
            for c in range(2, 9):
                img = self.sprite_sheet.subsurface((72 * c, 0), (72, 72))
                img = pygame.transform.scale(img, (72 * 1.3, 72 * 1.3))
                self.images_player.append(img)

        self.current = 0
        self.image = self.images_player[self.current]
        self.rect = self.image.get_rect()
        self.rect.center = (100, ALTURA - 69)
        self.frames = 0
        self.max_frames = 2

    def update(self):
        if self.frames > self.max_frames:
            self.frames = 0
            self.current += 1
        if self.current > len(self.images_player) - 1:
            self.current = 0
        self.frames += 1
        self.image = self.images_player[self.current]

    # def pular(self):
    #
