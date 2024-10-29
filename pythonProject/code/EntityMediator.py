from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.const import  WIN_WIDTH
from code.enemy import Enemy
from code.entity import Entity


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <0:
                ent.health = 0

        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
        for j in range(len(entity_list)):
            entity2 = entity_list[j]

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)