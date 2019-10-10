from abc import ABCMeta, abstractmethod

class IGraphic(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def print():
        """print information"""

class Ellipse(IGraphic):
    def print(self):
        print("Ellipse")

class Circle(IGraphic):
    def print(self):
        print("Circle")

class CompositeGraphic(IGraphic):
    def __init__(self):
        self.child_graphics = []

    def add(self, graphic):
        self.child_graphics.append(graphic)
    
    def print(self):
        for g in self.child_graphics:
            g.print()


ELLIPSE1 = Ellipse()
CIRCLE1 = Circle()

COMPOSITE1 = CompositeGraphic()
COMPOSITE1.add(ELLIPSE1)

COMPOSITE2 = CompositeGraphic()
COMPOSITE2.add(CIRCLE1)
COMPOSITE2.add(COMPOSITE1)

COMPOSITE2.print()



# ELLIPSE1.print()
# CIRCLE1.print()



