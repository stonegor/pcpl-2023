from lab_python_oop.color import Color
from .shape import Shape


class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: Color):
        self._width = width
        self._height = height
        self._color = color

    def get_area(self) -> float:
        return self._height * self._width

    def __repr__(self):
        return f"Rectangle(width: {self._width}, height: {self._height}, color: '{self._color}')"
