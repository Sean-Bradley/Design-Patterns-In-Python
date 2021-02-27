# pylint: disable=too-few-public-methods
"A Square Implementer"
from interface_shape_implementer import IShapeImplementer


class SquareImplementer(IShapeImplementer):
    "A Square Implementer"

    def draw_implementation(self):
        print("**************")
        print("*            *")
        print("*            *")
        print("*            *")
        print("*            *")
        print("*            *")
        print("*            *")
        print("**************")
