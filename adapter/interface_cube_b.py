# pylint: disable=too-few-public-methods
"An interface to implement"
from abc import ABCMeta, abstractmethod


class ICubeB(metaclass=ABCMeta):
    "An interface for an object"
    @staticmethod
    @abstractmethod
    def create(top_left_front, bottom_right_back):
        "Manufactures a Cube with coords offset [0, 0, 0]"
