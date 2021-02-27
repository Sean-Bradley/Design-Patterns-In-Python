"The switch interface, which all commands will implement"
from abc import ABCMeta, abstractmethod


class ISwitch(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    "The switch interface, which all commands will implement"

    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method which all command objects will use"
