# pylint: disable=too-few-public-methods

"A Game Interface"

from abc import ABCMeta, abstractmethod


class IGame(metaclass=ABCMeta):
    "A Game Interface"
    @staticmethod
    @abstractmethod
    def add_winner(position, name):
        "Must implement add_winner"
