from abc import ABC, abstractmethod

from creational.abstract_factory.models.car import Car
from creational.abstract_factory.models.engine import Engine


class AbstractCarFactory(ABC):
    @abstractmethod
    def create_engine(self) -> Engine:
        pass

    @abstractmethod
    def create_seats(self) -> int:
        pass

    def create_car(self) -> Car:
        return Car(engine=self.create_engine(), seats=self.create_seats())
