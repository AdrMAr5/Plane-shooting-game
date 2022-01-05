from kivy.clock import Clock

from Enemy import Enemy
from EnemyBullet import EnemyBullet



class Ship(Enemy):
    def __init__(self, game, pos, **kwargs):
        super().__init__(game, pos, **kwargs)
        self.game = game
        self.parameters = {'speed': 1, 'bullets': 1, 'points': 100}
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
        #print(self.pos)

    def moving(self, dt):
        self.entity_pos = self.entity_pos[0], self.entity_pos[1] - self.parameters['speed']
        if (self.entity_pos[0] - self.player_pos[0])**2 + (self.entity_pos[1] - self.player_pos[1])**2 < 100000\
                and self.shoots < self.parameters['bullets']:
            self.shoots += 1
            self.game.entityManager.add_entity(EnemyBullet(self.game, self.entity_pos))


    def stop_callbacks(self):
        super(Ship, self).stop_callbacks()
        # self._collisionEvent.cancel()
