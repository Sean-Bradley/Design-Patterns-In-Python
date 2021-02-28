"A Column that is used in a Row"
from flyweight_factory import FlyweightFactory

class Column():  # pylint: disable=too-few-public-methods
    """
    The columns are the contexts.
    They will share the Flyweights via the FlyweightsFactory.
    `data`, `width` and `justify` are extrinsic values. They are outside
    of the flyweights.
    """

    def __init__(self, data="", width=11, justify=0) -> None:
        self.data = data
        self.width = width
        self.justify = justify  # 0:center, 1:left, 2:right

    def get_data(self):
        "Get the flyweight value from the factory, and apply the extrinsic values"
        ret = ""
        for data in self.data:
            ret = ret + FlyweightFactory.get_flyweight(data).code
        ret = f"{ret.center(self.width)}" if self.justify == 0 else ret
        ret = f"{ret.ljust(self.width)}" if self.justify == 1 else ret
        ret = f"{ret.rjust(self.width)}" if self.justify == 2 else ret
        return ret
