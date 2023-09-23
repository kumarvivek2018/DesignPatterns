from creational.abstract_factory.enums.engine_type import EngineType
from creational.abstract_factory.enums.fuel_type import FuelType
from creational.abstract_factory.factories.abstract_car_factory import AbstractCarFactory
from creational.abstract_factory.models.engine import Engine


class SportsCarFactory(AbstractCarFactory):
    def create_engine(self) -> Engine:
        return Engine(fuel_type=FuelType.PETROL, engine_type=EngineType.CYLINDER12)

    def create_seats(self) -> int:
        return 2
