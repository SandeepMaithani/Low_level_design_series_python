from decorator_pattern.add_on.topping_decorator import ToppingDecorator


class ExtraCheese(ToppingDecorator):

    def get_description(self):
        return self._base_pizza.get_description() + " with Extra Cheese"

    def get_cost(self):
        return self._base_pizza.get_cost() + 25

class Mushroom(ToppingDecorator):

    def get_description(self):
        return self._base_pizza.get_description() + " with Mushroom"
    
    def get_cost(self):
        return self._base_pizza.get_cost() + 30