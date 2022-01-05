
from Enemy import Enemy


class EnemyBullet(Enemy):
    def __init__(self, game, pos, speed=300, size=(16, 16), **kwargs):
        super(EnemyBullet, self).__init__(game, pos, speed, **kwargs)
        self.entity_size = size
        self.entity_pos = pos
        self.source = "assets/enemy bullet.png"
        self.playerPos = self.game.player.entity_pos
        self.direction = self.get_direction(self.playerPos)
        self.angularSpeedIncrement = self.get_angular_increment(self.playerPos)

    def on_frame(self, sender, dt):
        self.moving(dt)
        if self.is_outside_world():
            self.destroy()

    def moving(self, dt):
        self.entity_pos = self.x + (self.direction[0] * self._speed * dt),\
                          self.y + (self.direction[1] * self._speed * dt)


