# pylint: disable=too-few-public-methods
"The Interface that Value should implement"
from abc import ABCMeta, abstractmethod


class IValue(metaclass=ABCMeta):
    "Methods the component must implement"
    @staticmethod
    @abstractmethod
    def __str__():
        "Override the object to return the value attribute by default"
