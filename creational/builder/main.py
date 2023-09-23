from creational.builder.burger import Burger
from creational.builder.burger_builder import BurgerBuilder
from creational.builder.burger_director import BurgerDirector
from creational.builder.item import Item
from creational.builder.product import Product

if __name__=='__main__':
    burger_builder: BurgerBuilder = BurgerBuilder()
    burger_director: BurgerDirector = BurgerDirector(burger_builder)

    burger: Product = burger_director.build_chicken_maharaja()
    print(burger)

    burger.add_item(Item(name='Cheese', price=20, weight=20, calories=200))
    print(burger)
