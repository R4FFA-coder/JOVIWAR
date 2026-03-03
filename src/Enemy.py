from random import randint

from src.Const import *
from src.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <=0:
            self.rect.left = LARGURA + randint(10,LARGURA)