from src.Const import LARGURA
from src.Enemy import Enemy
from src.EnemyShot import EnemyShot
from src.Entity import Entity
from src.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left > LARGURA:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            temp_entity = entity_list[i]
            EntityMediator.__verify_collision_window(temp_entity)
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)