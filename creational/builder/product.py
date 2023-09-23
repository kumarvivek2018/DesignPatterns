from __future__ import annotations

from functools import reduce
from typing import List

from creational.builder.exceptions import PriceCannotBeNegativeError, WeightCannotBeNegativeError, \
    CaloriesCannotBeNegativeError, ItemNotPresentError
from creational.builder.item import Item

"""
I have Product
-> product will have items
-> item will have weight, and calories
-> product will have a base price
-> additional items' price will be added to product base price.

Item:
- price: int in cents
- calories: int
- weight: int in gm

Product:
- name
- base price
- items_map {total_price, total_weight, total_calories, items_list}
- additional_items_map {total_price, total_weight, total_calories, items_list}
+ Product(items, price)
+ cost(): float
+ weight(): float
+ calories(): int
+ add_item(item)
+ remove_item(item)

"""


class Product:
    def __init__(self, name: str, items: List[Item], price: int) -> None:
        self._name: str = name
        self._items: List[Item] = items
        self._price: int = price
        self._weight: int = reduce(lambda accumulator, item: accumulator + item.weight, self._items, 0)
        self._calories: int = reduce(lambda accumulator, item: accumulator + item.calories, self._items, 0)
        self._additional_items: List[Item] = list()

    def _add_price(self, price) -> None:
        self._price += price

    def _reduce_price(self, price) -> None:
        if self._price + price < 0:
            raise PriceCannotBeNegativeError()
        self._price += price

    def _add_weight(self, weight) -> None:
        self._weight += weight

    def _reduce_weight(self, weight) -> None:
        if self._weight + weight < 0:
            raise WeightCannotBeNegativeError()
        self._weight += weight

    def _add_calories(self, calories) -> None:
        self._calories += calories

    def _reduce_calories(self, calories) -> None:
        if self._calories + calories < 0:
            raise CaloriesCannotBeNegativeError()
        self._calories += calories

    @property
    def price(self) -> int:
        return self._price

    @property
    def weight(self) -> int:
        return self._weight

    @property
    def calories(self) -> int:
        return self._calories

    def add_item(self, item: Item) -> None:
        self._additional_items.append(item)
        self._add_price(item.price)
        self._add_weight(item.weight)
        self._add_calories(item.calories)

    def remove_item(self, item: Item):
        if item in self._items:
            self._items.remove(item)
        elif item in self._additional_items:
            self._additional_items.remove(item)
        else:
            raise ItemNotPresentError()

        self._add_price(-item.price)
        self._add_weight(-item.weight)
        self._add_calories(-item.calories)

    def __str__(self):
        return f'name: {self._name}\n'\
               f'price: {self._price}\n'\
               f'weight: {self._weight}\n'\
               f'calories: {self._calories}\n'\
               f'Items: {self._items}'




