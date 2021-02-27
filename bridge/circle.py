# pylint: disable=too-few-public-methods
"A Circle Abstraction"
from interface_shape import IShape


class Circle(IShape):
    "The Circle is a Refined Abstraction"

    def __init__(self, implementer):
        self.implementer = implementer()

    def draw(self):
        self.implementer.draw_implementation()
