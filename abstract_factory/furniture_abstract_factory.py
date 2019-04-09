"""An Abstract Factory Pattern Example
The Abstract Factory Pattern adds an abstract layer over multiple factory method implementations.
The Abstract Factory contains or composites one or more than one factory method
"""

from abc import ABCMeta, abstractstaticmethod
from chair_factory import ChairFactory
from table_factory import TableFactory


class IFurnitureFactory(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """Furniture Factory Interface"""

    @abstractstaticmethod
    def get_furniture(furniture):
        """The static funiture factory inteface method"""


class FurnitureFactory(IFurnitureFactory):  # pylint: disable=too-few-public-methods
    """The Furniture Factory Concrete Class"""

    @staticmethod
    def get_furniture(furniture):
        """Static get_furniture method"""
        try:
            if furniture in ["SmallChair", "MediumChair", "BigChair"]:
                return ChairFactory().get_chair(furniture)
            if furniture in ["SmallTable", "MediumTable", "BigTable"]:
                return TableFactory().get_table(furniture)
            raise AssertionError("No Furniture Factory Found")
        except AssertionError as _e:
            print(_e)
        return None


FURNITURE = FurnitureFactory.get_furniture("SmallChair")
print(f"{FURNITURE.__class__} : {FURNITURE.dimensions()}")

FURNITURE = FurnitureFactory.get_furniture("MediumTable")
print(f"{FURNITURE.__class__} : {FURNITURE.dimensions()}")
