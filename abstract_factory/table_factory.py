"""A Factory Pattern Example
The Factory Pattern Defines in Interface for creating an object
and defers instantation until runtime.
Used when you don't know how many or what type of objects will be needed until during runtime
"""

from abc import ABCMeta, abstractstaticmethod


class ITable(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """The Table Interface"""

    @abstractstaticmethod
    def dimensions():
        """Get the table dimensions"""


class BigTable(ITable):  # pylint: disable=too-few-public-methods
    """The Big Table Concrete Class which implements the ITable interface"""

    def __init__(self):
        self._height = 60
        self._width = 120
        self._depth = 80

    def dimensions(self):
        return {"width": self._width, "depth": self._depth, "height": self._height}


class MediumTable(ITable):  # pylint: disable=too-few-public-methods
    """The Medium Table Concrete Class which implements the ITable interface"""

    def __init__(self):
        self._height = 60
        self._width = 110
        self._depth = 70

    def dimensions(self):
        return {"width": self._width, "depth": self._depth, "height": self._height}


class SmallTable(ITable):  # pylint: disable=too-few-public-methods
    """The Small Table Concrete Class which implements the ITable interface"""

    def __init__(self):
        self._height = 60
        self._width = 100
        self._depth = 60

    def dimensions(self):
        return {"width": self._width, "depth": self._depth, "height": self._height}


class TableFactory:  # pylint: disable=too-few-public-methods
    """Tha Factory Class"""

    @staticmethod
    def get_table(table):
        """A static method to get a table"""
        try:
            if table == "BigTable":
                return BigTable()
            if table == "MediumTable":
                return MediumTable()
            if table == "SmallTable":
                return SmallTable()
            raise AssertionError("Table Not Found")
        except AssertionError as _e:
            print(_e)
        return None


if __name__ == "__main__":
    TABLE = TableFactory().get_table("SmalTable")
    print(TABLE)
