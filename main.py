from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget

from GameWidget import GameWidget


class MenuWindow(Screen):
    def __init__(self, **kwargs):
        super(MenuWindow, self).__init__(**kwargs)

        self.start_button = Button(text='PLAY', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.add_widget(self.start_button)
        self.start_button.bind(on_release=self.start_game)

        self.exit_button = Button(text='EXIT GAME', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.add_widget(self.exit_button)
        self.exit_button.bind(on_release=self.exit_game)

    def start_game(self, *args):
        self.manager.current = 'game'

    def exit_game(self, *args):
        self.get_root_window().close()


class GameWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = None

    def on_pre_enter(self, *args):
        pass

    def on_enter(self, *args):
        print("Wchodzę do giery")
        self.game = GameWidget()
        self.add_widget(self.game)

    def on_leave(self, *args):
        print("Wychodzę z giery")

    def change(self, *args):
        # self.clear_widgets()
        print('dzieci screena:')
        print(self.children)
        # self.clear_widgets([self.game])
        self.game.destroy()
        # self.parent.remove_widget(self.game)
        # self.remove_widget(self.game)
        self.game = None
        print('dzieci screena:')
        print(self.children)
        self.manager.current = 'menu'



# class Game(Widget):
#     def __init__(self, screen):
#         super(Game, self).__init__()
#         self.game = None
#
#     def create_game(self):
#         game = GameWidget(self)
#         self.add_widget(game)
#         print(self.children)
#
#     def change(self):
#         self.clear_widgets()
#         print(self.children)
#         self.parent.manager.current = 'menu'


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
