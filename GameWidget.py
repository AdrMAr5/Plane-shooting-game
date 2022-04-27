from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import CoreLabel, Label
from kivy.uix.stencilview import StencilView
import random

from EnitityManager import EntityManager
from Player import Player
from Zero import Zero
from ship import Ship
from Enums import EntityType


def scoreFormat(score):
    str_score = str(score)
    length = len(str_score)
    return (6 - length) * '0' + str_score


class GameWidget(StencilView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game_over = False

        self.collisionCheckTime = 0.1

        self._score_label = CoreLabel(text="000000", font_size=26)
        self._score_label.refresh()
        self._score = 0

        self.register_event_type("on_frame")
        self.register_event_type("on_game_over")

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

        self.on_frame_event = Clock.schedule_interval(self._on_frame, 0)

        # self.sound = SoundLoader.load("assets/music.wav")
        # self.sound.play()

        self.on_spawn_enemies = Clock.schedule_interval(self.spawn_enemies, 0.5)
        self.on_spawn_ships = Clock.schedule_interval(self.spawn_ships, 3)
        # self.spawn_enemies(1)

    def spawn_enemies(self, dt):
        for i in range(1):
            random_x = random.randint(0, Window.width)
            y = Window.height
            self.entityManager.add_entity(Zero(self, (random_x, y)))

    def spawn_ships(self, dt):
        for i in range(1):
            pos = (random.randint(0, Window.width), Window.height)
            self.entityManager.add_entity(Ship(self, pos))

    def _on_frame(self, dt):
        self.dispatch("on_frame", dt)

    def on_frame(self, dt):
        pass

    def on_game_over(self):

        self.parent.change()

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

    def destroy(self):
        #self.unregister_event_types('on_frame')

        self.on_frame_event.cancel()
        # self.unregister.event.types(self.on_frame_event)

        #self.entityManager = None
        #self.player = None

        #self.unregister_event_types('on_game_over')
        self.clear_widgets()
        self.parent.remove_widget(self)



