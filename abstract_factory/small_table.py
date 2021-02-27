"A Class of Table"
from interface_table import ITable


class SmallTable(ITable):  # pylint: disable=too-few-public-methods
    "The Small Table Concrete Class implements the ITable interface"

    def __init__(self):
        self._height = 60
        self._width = 100
        self._depth = 60

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }
