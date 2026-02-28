import pygame
from pygame.locals import *
from src.Const import BGML2
from src.Entity import Entity
from src.EntityFactory import EntityFactory
from src.Player import Player
from sys import exit


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1'))

    def run(self, ):
        pygame.mixer_music.load(BGML2)
        pygame.mixer_music.play(-1, fade_ms=1500)
        pygame.mixer_music.set_volume(0.45)
        clock = pygame.time.Clock()
        todas_as_sprites = pygame.sprite.Group()
        player = Player()
        todas_as_sprites.add(player)

        while True:
            clock.tick(30)
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()

            todas_as_sprites.draw(self.window)
            todas_as_sprites.update()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()