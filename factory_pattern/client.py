
from factory_pattern.shape_factory import ShapeFactory


if __name__ == "__main__":

    factory_instance = ShapeFactory()
    share_input = "Rectangle"

    shape_instance = factory_instance.get_shape_instance(shape_name=share_input)

    if shape_instance:
        shape_instance.draw()
    else:
        print("Failed to load shape instance")