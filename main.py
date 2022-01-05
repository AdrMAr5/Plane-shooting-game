from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from GameWidget import GameWidget


class MainWindow(Screen):

    def play_game(self):
        sm.current = "Game"


class GameWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = GameWidget()
        self.game.bind(on_game_over=self.on_game_over)
        self.add_widget(self.game)

    def on_pre_enter(self, *args):
        self.game = GameWidget()
        self.add_widget(self.game)

    def on_enter(self, *args):
        print("Wchodzę do giery")
        # self.game = GameWidget()
        # self.add_widget(self.game)

    def on_leave(self, *args):
        print("Wychodzę z giery")
        self.remove_widget(self.game)

    def on_game_over(self, dt):
        print("Koniec Gry")
        sm.current = "Menu"


kv = Builder.load_file("menu.kv")
sm = ScreenManager()


class MyMainApp(App):

    def build(self):
        sm.add_widget(GameWindow(name="Game"))
        sm.add_widget(MainWindow(name="Menu"))
        return sm


if __name__ == "__main__":
    MyMainApp().run()
