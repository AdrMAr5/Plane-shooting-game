from kivy.clock import Clock

from Entity import Entity
from Enums import EntityType
from Explosion import Explosion


class Enemy(Entity):
    def __init__(self, game, pos, speed=100, **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self._speed = speed
        self.entity_pos = pos
        self.source = "assets/enemy.png"
        self.entity_size = (50, 50)
        self.pkt = 100
        self._angularSpeedIncrement = 1
        game.bind(on_frame=self.on_frame)

        self._collision_objects = [EntityType.Bullet, EntityType.EnemyBullet]

    @property
    def angularSpeedIncrement(self):
        return self._angularSpeedIncrement

    @angularSpeedIncrement.setter
    def angularSpeedIncrement(self, value):
        self._angularSpeedIncrement = value
        self._speed *= value

    def on_frame(self, sender, dt):
        self.moving(dt)
        if self.entity_pos[1] < 0:
            self.destroy()
            self.game.score -= 1
            return

    def collision(self, dt):
        for collision_object in self._collision_objects:
            for e in self.game.entityManager.entities[collision_object]:
                if e.collide_widget(self):
                    if isinstance(e, Enemy) and e.owner == self:
                        continue
                    if e.type == EntityType.Bullet:
                        self.game.score += self.pkt

                    self.game.entityManager.add_entity(Explosion(self.game, self.entity_pos))
                    self.destroy()
                    e.destroy()
                    return

    def moving(self, dt):
        step_size = self._speed * dt
        new_x = self.entity_pos[0]
        new_y = self.entity_pos[1] - step_size
        self.entity_pos = (new_x, new_y)

    def stop_callbacks(self):
        self.game.unbind(on_frame=self.on_frame)

    def destroy(self):
        self.stop_callbacks()
        self.game.entityManager.remove_entity(self)
