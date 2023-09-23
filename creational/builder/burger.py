from typing import List

from creational.builder.item import Item
from creational.builder.product import Product


class Burger(Product):
    def __init__(self, items: List[Item], price: int) -> None:
        super().__init__("Burger", items, price)