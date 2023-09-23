from creational.abstract_factory.enums.engine_type import EngineType
from creational.abstract_factory.enums.fuel_type import FuelType


class Engine:
    def __init__(self, fuel_type: FuelType, engine_type: EngineType) -> None:
        self._fuel_type: FuelType = fuel_type
        self._engine_type: EngineType = engine_type

    def __str__(self):
        return f'Engine of fuel type: {self._fuel_type.value}, and engine type: {self._engine_type.value}'
