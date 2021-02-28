# pylint: disable=too-few-public-methods
"The Add Decorator"
from interface_value import IValue


class Add(IValue):
    "A Decorator that Adds a number to a number"

    def __init__(self, val1, val2):
        # val1 and val2 can be int or the custom Value
        # object that contains the `value` attribute
        val1 = getattr(val1, 'value', val1)
        val2 = getattr(val2, 'value', val2)
        self.value = val1 + val2

    def __str__(self):
        return str(self.value)
