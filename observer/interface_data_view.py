"The Data View interface"
from abc import ABCMeta, abstractmethod


class IDataView(metaclass=ABCMeta):
    "A method for the Observer to implement"

    @staticmethod
    @abstractmethod
    def notify(data):
        "Receive notifications"

    @staticmethod
    @abstractmethod
    def draw(data):
        "Draw the view"

    @staticmethod
    @abstractmethod
    def delete():
        "a delete method to remove observer specific resources"
