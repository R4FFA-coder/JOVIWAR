from random import randint
from src.Const import *
from src.EnemyShot import EnemyShot
from src.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = 75

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        # if self.rect.right < 0:
        #     self.rect.left = LARGURA + randint(40,LARGURA - 40)

    def atirar(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            self.shot_delay = randint(75,300)
            return EnemyShot('EnemyShot', (self.rect.centerx, self.rect.centery - 5))