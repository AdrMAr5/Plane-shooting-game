from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button

from GameWidget import GameWidget


class MenuWindow(Screen):
    def __init__(self, **kwargs):
        super(MenuWindow, self).__init__(**kwargs)
        self.start_button = Button(text='play')
        self.add_widget(self.start_button)
        self.start_button.bind(on_release=self.start_game)

    def start_game(self, *args):
        self.manager.current = 'game'


class GameWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = None

    def on_pre_enter(self, *args):
        self.game = GameWidget(self.manager)
        self.add_widget(self.game)

    def on_enter(self, *args):
        print("Wchodzę do giery")

    def on_leave(self, *args):
        print("Wychodzę z giery")
        self.clear_widgets()

    def change(self, *args):
        self.manager.current = 'menu'





class MyMainApp(App):

    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sc1 = MenuWindow(name='menu')
        sc2 = GameWindow(name='game')
        sm.add_widget(sc1)
        sm.add_widget(sc2)
        return sm


if __name__ == "__main__":
    MyMainApp().run()
