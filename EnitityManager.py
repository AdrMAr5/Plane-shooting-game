from Bullet import Bullet
from Enemy import Enemy
from EnemyBullet import EnemyBullet
from Player import Player


class EntityManager(object):
    def __init__(self, game):
        self._entities = set()
        self._bullets = set()
        self._enemies = set()
        self._enemy_bullets = set()
        self.game = game

    @property
    def entities(self):
        return self._entities

    @property
    def bullets(self):
        return self._bullets

    @property
    def enemies(self):
        return self._enemies

    @property
    def enemy_bullets(self):
        return self._enemy_bullets

    def add_entity(self, entity):
        if type(entity) == Bullet:
            self._bullets.add(entity)
        elif isinstance(entity, Enemy):
            if type(entity) == EnemyBullet:
                self._enemy_bullets.add(entity)
            else:
                self._enemies.add(entity)
        self._entities.add(entity)
        self.game.add_widget(entity)

    def remove_entity(self, entity):
        if entity in self._entities:
            if type(entity) == Bullet:
                self._bullets.remove(entity)
            elif isinstance(entity, Enemy):
                if type(entity) == EnemyBullet:
                    self._enemy_bullets.remove(entity)
                else:
                    self._enemies.remove(entity)
            self._entities.remove(entity)
            self.game.remove_widget(entity)
