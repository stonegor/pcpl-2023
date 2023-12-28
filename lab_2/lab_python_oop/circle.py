import math

from .color import Color
from .shape import Shape


class Circle(Shape):
    def __init__(self, radius: float, color: Color):
        self._radius = radius
        self._color = color

    def get_area(self) -> float:
        return self._radius * math.pi

    def __repr__(self):
        return f"Circle(radius: {self._radius}, color: '{self._color}')"
