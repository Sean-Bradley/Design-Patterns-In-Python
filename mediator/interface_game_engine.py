"The Game Client Mediator Interface"
from abc import ABCMeta, abstractmethod


class IGameEngine(metaclass=ABCMeta):
    "The Game Client Interface"
    @staticmethod
    @abstractmethod
    def new_game():
        "A method to implement"

    @staticmethod
    @abstractmethod
    def add_player(player):
        "A method to implement"

    @staticmethod
    @abstractmethod
    def list_winners():
        "A method to implement"

    @staticmethod
    @abstractmethod
    def calculate_winners():
        "A method to implement"

    @staticmethod
    @abstractmethod
    def notify_winners():
        "A method to implement"

    @staticmethod
    @abstractmethod
    def game_result():
        "A method to implement"
