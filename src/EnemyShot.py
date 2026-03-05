import pygame

from src.Const import ENTITY_SPEED
from src.Entity import Entity


class EnemyShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, (48* 0.4, 48 * 0.4))

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]