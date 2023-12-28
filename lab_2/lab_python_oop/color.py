class Color:
    def __init__(self, value: str):
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __repr__(self):
        return f"Color({self.value})"

    def __str__(self):
        return self.value
