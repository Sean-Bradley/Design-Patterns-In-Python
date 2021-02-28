# pylint: disable=too-few-public-methods
"The Visitor Pattern Concept"
from abc import ABCMeta, abstractmethod

class IVisitor(metaclass=ABCMeta):
    "An interface that custom Visitors should implement"
    @staticmethod
    @abstractmethod
    def visit(element):
        "Visitors visit Elements/Objects within the application"

class IVisitable(metaclass=ABCMeta):
    """
    An interface the concrete objects should implement that allows
    the visitor to traverse a hierarchical structure of objects
    """
    @staticmethod
    @abstractmethod
    def accept(visitor):
        """
        The Visitor traverses and accesses each object through this
        method
        """

class Element(IVisitable):
    "An Object that can be part of any hierarchy"

    def __init__(self, name, value, parent=None):
        self.name = name
        self.value = value
        self.elements = set()
        if parent:
            parent.elements.add(self)

    def accept(self, visitor):
        "required by the Visitor that will traverse"
        for element in self.elements:
            element.accept(visitor)
        visitor.visit(self)

# The Client
# Creating an example object hierarchy.
Element_A = Element("A", 101)
Element_B = Element("B", 305, Element_A)
Element_C = Element("C", 185, Element_A)
Element_D = Element("D", -30, Element_B)

# Now Rather than changing the Element class to support custom
# operations, we can utilise the accept method that was
# implemented in the Element class because of the addition of
# the IVisitable interface

class PrintElementNamesVisitor(IVisitor):
    "Create a visitor that prints the Element names"
    @staticmethod
    def visit(element):
        print(element.name)

# Using the PrintElementNamesVisitor to traverse the object hierarchy
Element_A.accept(PrintElementNamesVisitor)

class CalculateElementTotalsVisitor(IVisitor):
    "Create a visitor that totals the Element values"
    total_value = 0

    @classmethod
    def visit(cls, element):
        cls.total_value += element.value
        return cls.total_value

# Using the CalculateElementTotalsVisitor to traverse the
# object hierarchy
TOTAL = CalculateElementTotalsVisitor()
Element_A.accept(CalculateElementTotalsVisitor)
print(TOTAL.total_value)
