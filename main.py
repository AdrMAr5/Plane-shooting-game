from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.label import CoreLabel
import random

from Enemy import Enemy
from EnitityManager import EntityManager
from Entity import Entity
from Player import Player
from Zero import Zero


def scoreFormat(score):
    str_score = str(score)
    length = len(str_score)
    return (6 - length) * '0' + str_score


class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.collisionCheckTime = 0.1

        self._score_label = CoreLabel(text="000000", font_size=26)
        self._score_label.refresh()
        self._score = 0

        self.register_event_type("on_frame")

        with self.canvas:
            Rectangle(source="assets/background.png", pos=(0, 0),
                      size=(Window.width, Window.height))
            self._score_instruction = Rectangle(texture=self._score_label.texture, pos=(
                0, Window.height - 50), size=self._score_label.texture.size)

        self.player = Player(self)
        self.player.entity_pos = (Window.width - Window.width / 3, 0)
        self.entityManager = EntityManager(self)
        self.entityManager.add_entity(self.player)


        Clock.schedule_interval(lambda dt: print(f"[\033[92mINFO\033[0m   ] [FPS         ] {str(Clock.get_fps())}"), 1)

        Clock.schedule_interval(self._on_frame, 0)

        # self.sound = SoundLoader.load("assets/music.wav")
        # self.sound.play()

        Clock.schedule_interval(self.spawn_enemies, 1)
        #self.spawn_enemies(1)

    def spawn_enemies(self, dt):
        for i in range(1):
            random_x = random.randint(0, Window.width)
            y = Window.height
            self.entityManager.add_entity(Zero(self, (random_x, y)))

    def _on_frame(self, dt):
        self.dispatch("on_frame", dt)

    def on_frame(self, dt):
        pass

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
        self._score_label.text = scoreFormat(value)
        self._score_label.refresh()
        self._score_instruction.texture = self._score_label.texture
        self._score_instruction.size = self._score_label.texture.size


game = GameWidget()


class MyApp(App):
    def build(self):
        return game


if __name__ == "__main__":
    app = MyApp()
    app.run()
