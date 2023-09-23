from creational.abstract_factory.models.engine import Engine


class Car:
    def __init__(self, engine: Engine, seats: int) -> None:
        self._engine: Engine = engine
        self._seats: int = seats

    def __str__(self):
        return f'Car with {self._engine} having {self._seats} seats.'
