# pylint: disable=too-few-public-methods
"The Table Interface"
from abc import ABCMeta, abstractmethod


class ITable(metaclass=ABCMeta):
    "The Table Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"
