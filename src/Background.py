from src.Const import LARGURA, BACKGROUND_SPEED
from src.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= BACKGROUND_SPEED[self.name]
        if self.rect.right <=0:
            self.rect.left = LARGURA
