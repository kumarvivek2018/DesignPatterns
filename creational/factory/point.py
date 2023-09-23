class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def __str__(self):
        return f'x: {self._x}, y: {self._y}'
