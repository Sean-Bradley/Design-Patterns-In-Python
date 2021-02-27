# pylint: disable=too-few-public-methods
"The Chair Interface"
from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):
    "The Chair Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"
