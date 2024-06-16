from decorator_pattern.base.base_pizza import BasePizza

class Margherita(BasePizza):

    def get_description(self):
        return "Margherita pizza"

    def get_cost(self):
        return 100

class Farmhouse(BasePizza):

    def get_description(self):
        return "Farmhouse pizza"

    def get_cost(self):
        return 300

class VegDelight(BasePizza):

    def get_description(self):
        return "Veg-Delight pizza"

    def get_cost(self):
        return 200