"A Data Controller Interface"
from abc import ABCMeta, abstractmethod


class IDataController(metaclass=ABCMeta):
    "A Subject Interface"
    @staticmethod
    @abstractmethod
    def subscribe(observer):
        "The subscribe method"

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        "The unsubscribe method"

    @staticmethod
    @abstractmethod
    def notify(observer):
        "The notify method"
