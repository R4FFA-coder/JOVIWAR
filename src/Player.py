import pygame
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, ):
        pygame.sprite.Sprite.__init__(self)
        self.images_player = []
        self.diretorio_principal = os.path.dirname(__file__)
        self.diretorio_assets = os.path.join(self.diretorio_principal, 'assets')
        self.diretorio_charPlayer = os.path.join(self.diretorio_principal, '../chars/player1')

        sprite_sheet = pygame.image.load(os.path.join(self.diretorio_charPlayer, 'Run2.png')).convert_alpha()

        for c in range(6):
            img = sprite_sheet.subsurface((48 * c, 0), (48, 48))
            img = pygame.transform.scale(img, (48 * 1.5 , 48 * 1.5))
            self.images_player.append(img)


        self.current = 0
        self.image = self.images_player[self.current]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 500)
        self.frames = 0
        self.max_frames = 1

    def update(self):
        if self.frames > self.max_frames:
            self.frames = 0
            self.current += 1
        if self.current > len(self.images_player) - 1:
            self.current = 0
        self.frames += 1
        self.image = self.images_player[self.current]
