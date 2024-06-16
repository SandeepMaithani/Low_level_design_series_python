from factory_pattern.shape import Shape


class Square(Shape):

    def draw(self):
        print("Square")