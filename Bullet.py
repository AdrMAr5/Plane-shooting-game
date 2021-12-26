from kivy.core.audio import SoundLoader
from kivy.core.window import Window

from Entity import Entity


class Bullet(Entity):
    def __init__(self, game, pos, speed=200, **kwargs):
        super().__init__(**kwargs)
        #sound = SoundLoader.load("assets/bullet.wav")
        #sound.play()
        self.game = game
        self._speed = speed
        self.entity_pos = pos
        self.entity_size = (25, 25)
        self.source = "assets/bullet.png"
        game.bind(on_frame=self.on_frame)

    def on_frame(self, sender, dt):
        self.moving(dt)
        #Czy bullet jest poza grą
        if self.entity_pos[1] > Window.height:
            self.destroy()

    def moving(self, dt):
        step_size = self._speed * dt
        new_x = self.entity_pos[0]
        new_y = self.entity_pos[1] + step_size
        self.entity_pos = (new_x, new_y)

    def stop_callbacks(self):
        self.game.unbind(on_frame=self.on_frame)

    def destroy(self):
        self.stop_callbacks()
        self.game.entityManager.remove_entity(self)