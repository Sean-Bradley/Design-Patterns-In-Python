# pylint: disable=too-few-public-methods
"The Strategy Pattern Example Use Case"
from abc import ABCMeta, abstractmethod


class GameCharacter():
    "This is the context whose strategy will change"

    position = [0, 0]

    @classmethod
    def move(cls, movement_style):
        "The movement algorithm has been decided by the client"
        movement_style(cls.position)


class IMove(metaclass=ABCMeta):
    "A Concrete Strategy Interface"

    @staticmethod
    @abstractmethod
    def __call__():
        "Implementors must select the default method"


class Walking(IMove):
    "A Concrete Strategy Subclass"

    @staticmethod
    def walk(position):
        "A walk algorithm"
        position[0] += 1
        print(f"I am Walking. New position = {position}")

    __call__ = walk


class Running(IMove):
    "A Concrete Strategy Subclass"

    @staticmethod
    def run(position):
        "A run algorithm"
        position[0] += 2
        print(f"I am Running. New position = {position}")

    __call__ = run


class Crawling(IMove):
    "A Concrete Strategy Subclass"

    @staticmethod
    def crawl(position):
        "A crawl algorithm"
        position[0] += 0.5
        print(f"I am Crawling. New position = {position}")

    __call__ = crawl


# The Client
GAME_CHARACTER = GameCharacter()
GAME_CHARACTER.move(Walking())
# Character sees the enemy
GAME_CHARACTER.move(Running())
# Character finds a small cave to hide in
GAME_CHARACTER.move(Crawling())
