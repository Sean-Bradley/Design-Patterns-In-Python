"A Class of Table"
from interface_table import ITable


class BigTable(ITable):  # pylint: disable=too-few-public-methods
    "The Big Chair Concrete Class implements the ITable interface"

    def __init__(self):
        self._height = 60
        self._width = 120
        self._depth = 80

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }
