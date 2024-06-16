from factory_pattern.shape import Shape


class Circle(Shape):

    def draw(self):
        print("Circle")