from abc import ABC, abstractmethod

from decorator_pattern.base.base_pizza import BasePizza

class ToppingDecorator(BasePizza, ABC):
    
    def __init__(self, base_pizza) -> None:
        self._base_pizza = base_pizza
    
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass