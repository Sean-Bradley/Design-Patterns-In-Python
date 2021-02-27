"A Data Model Interface"
from abc import ABCMeta, abstractmethod


class IDataModel(metaclass=ABCMeta):
    "A Subject Interface"

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        "The subscribe method"

    @staticmethod
    @abstractmethod
    def unsubscribe(observer_id):
        "The unsubscribe method"

    @staticmethod
    @abstractmethod
    def notify(data):
        "The notify method"
