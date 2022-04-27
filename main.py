from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
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

        self.game = GameWidget()
        self.add_widget(self.game)

    def on_leave(self, *args):
        pass

    def change(self, *args):
        # self.clear_widgets()

        print(self.children)
        self.game.destroy()
        self.game = None
        print(self.children)
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
