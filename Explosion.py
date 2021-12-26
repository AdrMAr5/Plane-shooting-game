from kivy.clock import Clock
from kivy.core.audio import SoundLoader

from Entity import Entity


class Explosion(Entity):
    def __init__(self, game, pos):
        super().__init__()
        self.game = game
        self.entity_pos = pos
        #sound = SoundLoader.load("assets/explosion.wav")
        self.source = "assets/explosion.png"
        #sound.play()
        Clock.schedule_once(self._remove_me, 0.1)

    def _remove_me(self, dt):
        self.game.entityManager.remove_entity(self)
