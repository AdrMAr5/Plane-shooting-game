from kivy.clock import Clock
from kivy.core.window import Window

from Bullet import Bullet
from Entity import Entity
from Explosion import Explosion
from ship import Ship

class Player(Entity):
    def __init__(self, game, **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self.source = "assets/plane.png"
        self.entity_pos = (400, 0)
        self.entity_size = (50, 50)
        self.speed = 400

        self.timeToShoot = 0.1
        self.canShoot = True

        self._shoot_event = Clock.schedule_interval(self.shootDelay, self.timeToShoot)
        self._collisionEvent = Clock.schedule_interval(self.collision, game.collisionCheckTime)

        game.bind(on_frame=self.on_frame)

        self._keyboard = Window.request_keyboard(
            self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        self.keysToMove = {"w": 0, "a": 0, "s": 0, "d": 0}
        self.keysToShoot = {"spacebar": 0}
        self.isFlyingByTouch = False

        self.posToFollow = self.entity_pos

    def on_frame(self, sender, dt):
        self.flying(dt)
        self.shooting()

    def on_touch_down(self, touch):
        self.isFlyingByTouch = True
        self.posToFollow = touch.pos

    def on_touch_move(self, touch):
        self.posToFollow = touch.pos

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if self.keysToMove.__contains__(keycode[1]):
            self.keysToMove[keycode[1]] = 1
            self.isFlyingByTouch = False
        if self.keysToShoot.__contains__(keycode[1]):
            self.keysToShoot[keycode[1]] = 1

    def _on_key_up(self, keyboard, keycode):
        if self.keysToMove.__contains__(keycode[1]):
            self.keysToMove[keycode[1]] = 0
        if self.keysToShoot.__contains__(keycode[1]):
            self.keysToShoot[keycode[1]] = 0

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def shooting(self):
        if self.canShoot and self.keysToShoot["spacebar"] == 1:
            self.canShoot = False
            self.timeToShoot += 0.5
            x = self.entity_pos[0] + 12
            y = self.entity_pos[1] + 50
            self.game.entityManager.add_entity(Bullet(self.game, (x, y)))

    def shootDelay(self, dt):
        self.canShoot = True

    def flying(self, dt):
        if self.isFlyingByTouch:
            self.entity_pos = self.move_towards(self.posToFollow, self.speed * 2 * dt)
        else:
            newX = self.entity_pos[0] + ((self.keysToMove["d"] - self.keysToMove["a"]) * self.speed * dt)
            newY = self.entity_pos[1] + ((self.keysToMove["w"] - self.keysToMove["s"]) * self.speed * dt)
            self.entity_pos = (newX, newY)

    def collision(self, dt):
        for e in self.game.entityManager.enemies:
            if e.collide_widget(self) and type(e) != Ship:
                self.game.entityManager.add_entity(Explosion(self.game, self.entity_pos))
                self.destroy()
                e.destroy()
                return

    def stop_call_backs(self):
        self.clear_widgets()
        self.game.unbind(on_frame=self.on_frame)
        self._shoot_event.cancel()
        self._collisionEvent.cancel()

    def destroy(self):
        self.stop_call_backs()
        self.game.entityManager.remove_entity(self)
        self.game.dispatch("on_game_over")


