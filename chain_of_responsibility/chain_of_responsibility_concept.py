# pylint: disable=too-few-public-methods
"The Chain Of Responsibility Pattern Concept"
import random
from abc import ABCMeta, abstractmethod


class IHandler(metaclass=ABCMeta):
    "The Handler Interface that the Successors should implement"
    @staticmethod
    @abstractmethod
    def handle(payload):
        "A method to implement"


class Successor1(IHandler):
    "A Concrete Handler"
    @staticmethod
    def handle(payload):
        print(f"Successor1 payload = {payload}")
        test = random.randint(1, 2)
        if test == 1:
            payload = payload + 1
            payload = Successor1().handle(payload)
        if test == 2:
            payload = payload - 1
            payload = Successor2().handle(payload)
        return payload


class Successor2(IHandler):
    "A Concrete Handler"
    @staticmethod
    def handle(payload):
        print(f"Successor2 payload = {payload}")
        test = random.randint(1, 3)
        if test == 1:
            payload = payload * 2
            payload = Successor1().handle(payload)
        if test == 2:
            payload = payload / 2
            payload = Successor2().handle(payload)
        return payload


class Chain():
    "A chain with a default first successor"
    @staticmethod
    def start(payload):
        "Setting the first successor that will modify the payload"
        return Successor1().handle(payload)


# The Client
CHAIN = Chain()
PAYLOAD = 1
OUT = CHAIN.start(PAYLOAD)
print(f"Finished result = {OUT}")
