from .color import Color
from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_length: float, color: Color):
        super().__init__(side_length, side_length, color)

    def __repr__(self):
        return f"Square(side_length: {self._width}, color: '{self._color}')"
