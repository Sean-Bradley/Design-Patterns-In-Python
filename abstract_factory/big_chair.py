"A Class of Chair"
from interface_chair import IChair


class BigChair(IChair):  # pylint: disable=too-few-public-methods
    "The Big Chair Concrete Class that implements the IChair interface"

    def __init__(self):
        self._height = 80
        self._width = 80
        self._depth = 80

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }
