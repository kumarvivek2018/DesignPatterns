from creational.abstract_factory.car_service import CarService
from creational.abstract_factory.factories.sports_car_factory import SportsCarFactory
from creational.abstract_factory.factories.suv_car_factory import SUVCarFactory

if __name__ == '__main__':
    car_service: CarService = CarService(SportsCarFactory())

    print(car_service.create_car())

    car_service.car_factory = SUVCarFactory()
    print(car_service.create_car())
