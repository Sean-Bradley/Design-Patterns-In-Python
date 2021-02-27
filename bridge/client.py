"Bridge Pattern Concept Sample Code"

from circle_implementer import CircleImplementer
from square_implementer import SquareImplementer
from circle import Circle
from square import Square

CIRCLE = Circle(CircleImplementer)
CIRCLE.draw()

SQUARE = Square(SquareImplementer)
SQUARE.draw()
