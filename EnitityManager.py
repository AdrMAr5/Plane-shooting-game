from Bullet import Bullet
from Enemy import Enemy
from EnemyBullet import EnemyBullet
from Player import Player
from Enums import *


class EntityManager(object):
    def __init__(self, game):
        self.game = game
        self._entities = {}
        for entity in EntityType:
            self._entities[entity] = []

        self.initial_index_of_layer = {}
        for layer in Layer:
            self.initial_index_of_layer[layer] = 0

    @property
    def entities(self):
        return self._entities

    def add_entity(self, entity):
        self._entities[entity.type].append(entity)
        self.game.add_widget(entity, self.initial_index_of_layer[entity.layer])
        for layer in range(entity.layer.value + 1, len(Layer)):
            self.initial_index_of_layer[Layer(layer)] += 1

    def remove_entity(self, entity):
        self._entities[entity.type].remove(entity)
        self.game.remove_widget(entity)
        for layer in range(entity.layer.value + 1, len(Layer)):
            self.initial_index_of_layer[Layer(layer)] -= 1
