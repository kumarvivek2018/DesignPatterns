from dataclasses import dataclass

from creational.builder.exceptions import PriceCannotBeNegativeError, WeightCannotBeNegativeError, \
    CaloriesCannotBeNegativeError


@dataclass(frozen=True)
class Item:
    name: str
    price: int
    weight: int
    calories: int

    def __post_init__(self):
        if self.price < 0:
            raise PriceCannotBeNegativeError()

        if self.weight < 0:
            raise WeightCannotBeNegativeError()

        if self.calories < 0:
            raise CaloriesCannotBeNegativeError()
