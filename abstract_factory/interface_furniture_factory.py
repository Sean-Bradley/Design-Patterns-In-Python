# pylint: disable=too-few-public-methods
"The Abstract Factory Interface"
from abc import ABCMeta, abstractmethod


class IFurnitureFactory(metaclass=ABCMeta):
    "Abstract Furniture Factory Interface"

    @staticmethod
    @abstractmethod
    def get_furniture(furniture):
        "The static Abstract factory interface method"
