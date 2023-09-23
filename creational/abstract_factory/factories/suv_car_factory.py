from creational.abstract_factory.enums.engine_type import EngineType
from creational.abstract_factory.enums.fuel_type import FuelType
from creational.abstract_factory.factories.abstract_car_factory import AbstractCarFactory
from creational.abstract_factory.models.engine import Engine


class SUVCarFactory(AbstractCarFactory):
    def create_engine(self) -> Engine:
        return Engine(fuel_type=FuelType.DIESEL, engine_type=EngineType.CYLINDER4)

    def create_seats(self) -> int:
        return 7
