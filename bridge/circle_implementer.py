# pylint: disable=too-few-public-methods
"A Circle Implementer"
from interface_shape_implementer import IShapeImplementer


class CircleImplementer(IShapeImplementer):
    "A Circle Implementer"

    def draw_implementation(self):
        print("    ******")
        print("  **      **")
        print(" *          *")
        print("*            *")
        print("*            *")
        print(" *          *")
        print("  **      **")
        print("    ******")
