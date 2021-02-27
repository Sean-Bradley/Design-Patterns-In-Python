# pylint: disable=too-few-public-methods
"An interface to implement"
from abc import ABCMeta, abstractmethod


class ICubeA(metaclass=ABCMeta):
    "An interface for an object"
    @staticmethod
    @abstractmethod
    def manufacture(width, height, depth):
        "manufactures a cube"
