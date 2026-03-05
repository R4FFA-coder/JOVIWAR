from random import randint
from src.Background import Background
from src.Const import LARGURA, ALTURA
from src.Enemy import Enemy
from src.Platform import Platform


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1':
                list_bg = []
                for i in range(1,6):
                    list_bg.append(Background(f'Level1_{i}', (0, 0)))
                    list_bg.append(Background(f'Level1_{i}', (LARGURA, 0)))
                return list_bg
            case 'Enemy':
                return Enemy('Drone', (LARGURA + randint(20, LARGURA), ALTURA - 85))