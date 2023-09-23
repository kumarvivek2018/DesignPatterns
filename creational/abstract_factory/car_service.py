from creational.abstract_factory.factories.abstract_car_factory import AbstractCarFactory
from creational.abstract_factory.models.car import Car


class CarService:
    def __init__(self, car_factory: AbstractCarFactory) -> None:
        self._car_factory: AbstractCarFactory = car_factory

    @property
    def car_factory(self) -> AbstractCarFactory:
        return self._car_factory

    @car_factory.setter
    def car_factory(self, car_factory: AbstractCarFactory) -> None:
        self._car_factory = car_factory

    def create_car(self) -> Car:
        return self._car_factory.create_car()
