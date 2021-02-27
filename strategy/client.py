# pylint: disable=too-few-public-methods
"The Strategy Pattern Example Use Case"
from abc import ABCMeta, abstractmethod


class GameCharacter():
    "This is the context whose strategy will change"

    @staticmethod
    def move(movement_style):
        "The movement algorithm has been decided by the client"
        movement_style()


class IMove(metaclass=ABCMeta):
    "A Concrete Strategy Interface"

    @staticmethod
    @abstractmethod
    def __call__():
        "Implementors must select the default method"


class Walking(IMove):
    "A Concrete Strategy Subclass"

    @staticmethod
    def walk():
        "A walk algorithm"
        print("I am Walking")

    __call__ = walk


class Running(IMove):
    "A Concrete Strategy Subclass"

    @staticmethod
    def run():
        "A run algorithm"
        print("I am Running")

    __call__ = run


class Crawling(IMove):
    "A Concrete Strategy Subclass"

    @staticmethod
    def crawl():
        "A crawl algorithm"
        print("I am Crawling")

    __call__ = crawl


# The Client
GAME_CHARACTER = GameCharacter()
GAME_CHARACTER.move(Walking())
# Character sees the enemy
GAME_CHARACTER.move(Running())
# Character finds a small cave to hide in
GAME_CHARACTER.move(Crawling())
