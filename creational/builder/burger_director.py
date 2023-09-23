from creational.builder.burger import Burger
from creational.builder.burger_builder import BurgerBuilder
from creational.builder.item import Item


class BurgerDirector:
    def __init__(self, builder: BurgerBuilder) -> None:
        self._builder = builder

    def build_chicken_maharaja(self) -> Burger:
        top_bun: Item = Item(name='Top Bun', price=20, weight=20, calories=100)
        bottom_bun: Item = Item(name='Bottom Bun', price=15, weight=20, calories=100)
        cheese_slice: Item = Item(name='Cheese Slice', price=10, weight=10, calories=200)
        chicken_patty: Item = Item(name='Chicken Patty', price=50, weight=30, calories=300)

        return self._builder\
            .add_item(top_bun)\
            .add_item(bottom_bun)\
            .add_item(cheese_slice)\
            .add_item(chicken_patty)\
            .with_price(200)\
            .build()