"A Class of Chair"
from interface_chair import IChair


class MediumChair(IChair):  # pylint: disable=too-few-public-methods
    """The Medium Chair Concrete Class implements the IChair interface"""

    def __init__(self):
        self._height = 60
        self._width = 60
        self._depth = 60

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }
