from kivy.clock import Clock

from Enemy import Enemy
from EnemyBullet import EnemyBullet
from Enums import *


class Ship(Enemy):
    def __init__(self, game, pos, **kwargs):
        super().__init__(game, pos, **kwargs)
        self.type = EntityType.Ship
        self.layer = Layer.Ground
        self.game = game
        self.parameters = {'speed': 1, 'bullets': 1, 'points': 100}
        self.bullet_parameters = {'damage': 50, 'speed': 150, 'size': (18, 18),
                                  'source': "assets/enemy bullet.png", 'owner': self}
        self.shoots = 0
        self.entity_pos = pos
        self.player_pos = self.get_player_pos()
        self.source = "assets/ship.png"

        self.pkt = 500


    def get_player_pos(self):
        pos = self.game.player.entity_pos
        return pos

    def on_frame(self, sender, dt):
        self.moving(dt)
        self.player_pos = self.get_player_pos()


    def moving(self, dt):
        self.entity_pos = self.entity_pos[0], self.entity_pos[1] - self.parameters['speed']
        if self.distance_between(self.player_pos) < 150 and self.shoots < self.parameters['bullets']:
            self.shoots += 1
            self.game.entityManager.add_entity(EnemyBullet(self.game, self.entity_pos, self.bullet_parameters))


    def stop_callbacks(self):
        super(Ship, self).stop_callbacks()
        # self._collisionEvent.cancel()
