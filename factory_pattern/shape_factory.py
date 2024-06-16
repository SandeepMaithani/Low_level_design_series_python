from factory_pattern.circle import Circle
from factory_pattern.rectangle import Rectangle
from factory_pattern.square import Square


class ShapeFactory():

    def get_shape_instance(self, shape_name):

        if shape_name == 'Circle':
            return Circle()
        elif shape_name == 'Rectangle':
            return Rectangle()
        elif shape_name == 'Square':
            return Square()
        else:
            return None
