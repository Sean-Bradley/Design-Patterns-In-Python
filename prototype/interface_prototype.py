# pylint: disable=too-few-public-methods
"Prototype Concept Sample Code"
from abc import ABCMeta, abstractmethod


class IProtoType(metaclass=ABCMeta):
    "interface with clone method"
    @staticmethod
    @abstractmethod
    def clone(mode):
        """The clone, deep or shallow.
        It is up to you how you  want to implement
        the details in your concrete class"""
