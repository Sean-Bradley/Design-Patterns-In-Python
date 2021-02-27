# pylint: disable=too-few-public-methods
"The Custom Value class"
from interface_value import IValue


class Value(IValue):
    "A component that can be decorated or not"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
