from __future__ import annotations

from typing import List

from creational.builder.burger import Burger
from creational.builder.exceptions import PriceCannotBeNegativeError
from creational.builder.item import Item


class BurgerBuilder:
    def __init__(self) -> None:
        self._items: List[Item] = list()
        self._price: int = 0

    def add_item(self, item: Item) -> BurgerBuilder:
        self._items.append(item)
        return self

    def with_price(self, price: int) -> BurgerBuilder:
        if price < 0:
            raise PriceCannotBeNegativeError()

        self._price = price
        return self

    def reset(self) -> BurgerBuilder:
        self.__init__()
        return self

    def build(self) -> Burger:
        return Burger(self._items, self._price)
