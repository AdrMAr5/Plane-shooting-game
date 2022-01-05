from kivy.clock import Clock

from Enemy import Enemy
from EnemyBullet import EnemyBullet


# Podstawowy myśliwiec Japońskiej Marynarki Wojennej - Mitsubishi A6M Reisen znany jako Zero
class Zero(Enemy):
    def __init__(self, game, pos, speed=300, **kwargs):
        super().__init__(game, pos, speed, **kwargs)
        self.game = game
        self._speed = speed
        self.entity_pos = pos
        self.source = "assets/enemy.png"
        self._collisionEvent = Clock.schedule_interval(self.collision, game.collisionCheckTime)

        self.playerPos = self.get_player_pos()
        self.angularSpeedIncrement = self.get_angular_increment(self.playerPos)
        self.escapePos = (self.playerPos[0] - (self.x - self.playerPos[0]), self.y)
        self.pkt = 500

        self.commandStep = 0

    def get_player_pos(self):
        pos = self.game.player.entity_pos
        pos = (pos[0], pos[1] + 200)
        return pos

    def on_frame(self, sender, dt):
        self.moving(dt)

    def moving(self, dt):
        if self.commandStep == 0:  # Podlatywanie pod pozycję gracza
            self.entity_pos = self.move_towards(self.playerPos, self._speed * dt)
            if self.entity_pos == self.playerPos:
                self.commandStep += 1
        elif self.commandStep == 1:  # Stzał do gracza
            #self.game.entityManager.add_entity(EnemyBullet(self.game, self.entity_pos))
            self.commandStep += 1
            self.angularSpeedIncrement = self.get_angular_increment(self.escapePos)
        elif self.commandStep == 2:  # Odlatywanie od gracza
            self.entity_pos = self.move_towards(self.escapePos, self._speed * dt)
            if self.entity_pos == self.escapePos:
                self.commandStep += 1
        else:
            self.destroy()

    def stop_callbacks(self):
        super(Zero, self).stop_callbacks()
        self._collisionEvent.cancel()
