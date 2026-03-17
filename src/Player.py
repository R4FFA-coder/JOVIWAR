import pygame
from src.Const import ALTURA
from src.Entity import Entity
from src.PlayerShot import PlayerShot

class Player(Entity):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'Player'
        self.images_player_run = []
        self.images_player_jump = []
        self.pulo = False
        self.pos_y_inicial = ALTURA - 70 - 90 // 2
        self.sprite_sheet = pygame.image.load('./chars/player1/Player2.png').convert_alpha()

        for c in range(2, 9):
            img = self.sprite_sheet.subsurface((72 * c, 0), (72, 72))
            img = pygame.transform.scale(img, (72 * 1.3, 72 * 1.3))
            self.images_player_run.append(img)
        for c in range(28, 36):
            img = self.sprite_sheet.subsurface((72 * c, 0), (72, 72))
            img = pygame.transform.scale(img, (72 * 1.3, 72 * 1.3))
            self.images_player_jump.append(img)

        self.current = 0
        self.image = self.images_player_run[self.current]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (100, self.pos_y_inicial + (self.image.get_height() // 2))
        self.frames = 0
        self.max_frames = 1
        self.surf = self.image
        self.health = 5
        self.damage = 1
        self.score = 0

    def update(self):
        if self.pulo:
            self.rect.y -= 21
            if self.rect.y <= 320:
                self.pulo = False
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 13
            else:
                self.rect.y = self.pos_y_inicial
        if self.rect.y < self.pos_y_inicial:
            atual_list = self.images_player_jump
        else:
            atual_list = self.images_player_run
        self.frames += 1
        if self.frames > self.max_frames:
            self.frames = 0
            self.current += 1
        if self.current > len(atual_list) - 1:
            self.current = 0
        self.surf = self.image

        pos_antiga = self.rect.midbottom
        self.image = atual_list[self.current]
        self.rect = self.image.get_rect(midbottom=pos_antiga)

    def pular(self):
        self.pulo = True
        self.current = 0

    def atirar(self):
        return PlayerShot('PlayerShot', (self.rect.right - 15, self.rect.y + 35))

    def move(self):
        pass
