from abc import ABCMeta, abstractmethod


class IGraphic(metaclass=ABCMeta):
    """Component"""

    @staticmethod
    @abstractmethod
    def print():
        """print information"""


class CompositeGraphic(IGraphic):
    """Composite"""

    def __init__(self):
        self.child_graphics = []

    def add(self, graphic):
        self.child_graphics.append(graphic)

    def print(self):
        for g in self.child_graphics:
            g.print()


class Ellipse(IGraphic):
    """leaf"""

    def print(self):
        print("Ellipse")


class Circle(IGraphic):
    def print(self):
        print("Circle")


"""client"""
ELLIPSE1 = Ellipse()
ELLIPSE2 = Ellipse()
ELLIPSE3 = Ellipse()
ELLIPSE4 = Ellipse()
CIRCLE1 = Circle()

COMPOSITE4 = CompositeGraphic()
COMPOSITE4.add(ELLIPSE1)
COMPOSITE4.add(ELLIPSE2)
COMPOSITE4.add(ELLIPSE3)

COMPOSITE2 = CompositeGraphic()
COMPOSITE2.add(ELLIPSE4)
COMPOSITE2.add(CIRCLE1)

COMPOSITE3 = CompositeGraphic()
COMPOSITE3.add(COMPOSITE4)
COMPOSITE3.add(COMPOSITE2)

COMPOSITE1 = CompositeGraphic()
COMPOSITE1.add(ELLIPSE1)
COMPOSITE1.add(COMPOSITE3)
# COMPOSITE3.print()

COMPOSITE1.print()
