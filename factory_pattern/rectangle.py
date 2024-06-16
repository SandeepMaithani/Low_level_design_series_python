from factory_pattern.shape import Shape


class Rectangle(Shape):

    def draw(self):
        print("Rectangle")