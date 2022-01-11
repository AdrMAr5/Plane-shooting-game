import math
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget


class Entity(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._entity_pos = (0, 0)
        self._entity_size = (50, 50)
        self._source = "bullshit.png"
        self._instruction = Rectangle(
            pos=self.entity_pos, size=self.entity_size, source=self._source)
        self.canvas.add(self._instruction)

    @property
    def entity_pos(self):
        return self._entity_pos

    @entity_pos.setter
    def entity_pos(self, value):
        self.pos = value
        self._entity_pos = value
        self._instruction.pos = self._entity_pos

    @property
    def entity_size(self):
        return self._entity_size

    @entity_size.setter
    def entity_size(self, value):
        self.size = value
        self._entity_size = value
        self._instruction.size = self._entity_size

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
        self._instruction.source = self._source

    def move_towards(self, targetPos, maxDistanceDelta, direction=(0, 0)):
        if direction == (0, 0):
            direction = self.get_direction(targetPos)
        if self.get_distance(targetPos) < maxDistanceDelta:
            return targetPos
        return self.x + (direction[0] * maxDistanceDelta), self.y + (direction[1] * maxDistanceDelta)

    def get_direction(self, targetPos):
        if self.entity_pos == targetPos:
            return 0, 0
        diff_x = targetPos[0] - self.x
        diff_y = targetPos[1] - self.y
        m = abs(diff_x) + abs(diff_y)
        return diff_x / m, diff_y / m

    def get_angular_increment(self, target_pos, direction=(0, 0)):
        if direction == (0, 0):
            direction = self.get_direction(target_pos)
        if direction[0] == 0:
            return 1
        distance = self.get_distance(target_pos)
        diff_x = abs(target_pos[0] - self.x) or 1
        return (1 / distance) / ((abs(direction[0])) / diff_x)

    def get_distance(self, pos):
        return math.sqrt(pow(self.x - pos[0], 2) + pow(self.y - pos[1], 2))

    def is_outside_world(self):
        if self.x < 0 or self.x > Window.width:
            return True
        if self.y < 0 or self.y > Window.height:
            return True
        return False

    def distance_between(self, position):
        return pow((self.entity_pos[0] - position[0])**2 + (self.entity_pos[1] - position[1])**2, 0.5)
