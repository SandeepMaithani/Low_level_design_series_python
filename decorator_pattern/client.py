

from decorator_pattern.add_on.topping_options import ExtraCheese, Mushroom
from decorator_pattern.base.pizza_options import Margherita


if __name__ == "__main__":

    # base pizza
    pizza = Margherita()
    print(pizza.get_description())
    print(pizza.get_cost())

    # Create different decorators(topping)
    with_extra_cheese = ExtraCheese(pizza)
    with_mushroom = Mushroom(pizza)

    # Apply decorators individually
    print(with_extra_cheese.get_description())
    print(with_extra_cheese.get_cost())

    print(with_mushroom.get_description())
    print(with_mushroom.get_cost())


    # Combine decorators
    with_mushroom_and_extra_cheese = ExtraCheese(Mushroom(pizza))
    print(with_mushroom_and_extra_cheese.get_description())
    print(with_mushroom_and_extra_cheese.get_cost())