from Bullet import Bullet
from Enemy import Enemy
from Player import Player


class EntityManager(object):
    def __init__(self, game):
        self._entities = set()
        self._bullets = set()
        self._enemies = set()
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

    def add_entity(self, entity):
        if type(entity) == Bullet:
            self._bullets.add(entity)
        elif isinstance(entity, Enemy):
            self._enemies.add(entity)
        self._entities.add(entity)
        self.game.add_widget(entity)

    def remove_entity(self, entity):
        if entity in self._entities:
            if type(entity) == Bullet:
                self._bullets.remove(entity)
            elif isinstance(entity, Enemy):
                self._enemies.remove(entity)
            self._entities.remove(entity)
            self.game.remove_widget(entity)
