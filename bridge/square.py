# pylint: disable=too-few-public-methods
"A Square Abstraction"
from interface_shape import IShape


class Square(IShape):
    "The Square is a Refined Abstraction"

    def __init__(self, implementer):
        self.implementer = implementer()

    def draw(self):
        self.implementer.draw_implementation()
