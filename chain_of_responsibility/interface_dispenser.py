"The ATM Notes Dispenser Interface"
from abc import ABCMeta, abstractmethod


class IDispenser(metaclass=ABCMeta):
    "Methods to implement"
    @staticmethod
    @abstractmethod
    def next_successor(successor):
        """Set the next handler in the chain"""

    @staticmethod
    @abstractmethod
    def handle(amount):
        """Handle the event"""
