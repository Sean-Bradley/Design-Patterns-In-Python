# pylint: disable=too-few-public-methods
"The Subtract Decorator"
from interface_value import IValue


class Sub(IValue):
    "A Decorator that subtracts a number from a number"

    def __init__(self, val1, val2):
        # val1 and val2 can be int or the custom Value
        # object that contains the `value` attribute
        val1 = getattr(val1, 'value', val1)
        val2 = getattr(val2, 'value', val2)
        self.value = val1 - val2

    def __str__(self):
        return str(self.value)
