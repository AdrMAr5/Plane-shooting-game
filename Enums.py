from enum import Enum


class EntityType(Enum):
    Entity = 0
    Player = 1
    Bullet = 2
    EnemyBullet = 3
    Zero = 4
    Ship = 5


class Layer(Enum):
    Sky = 0
    Ground = 1
    BackGround = 2
