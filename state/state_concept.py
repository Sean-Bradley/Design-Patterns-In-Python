# pylint: disable=too-few-public-methods
"The State Pattern Concept"
from abc import ABCMeta, abstractmethod
import random

class Context():
    "This is the object whose behavior will change"

    def __init__(self):
        self.state_handles = [ConcreteStateA(),
                              ConcreteStateB(),
                              ConcreteStateC()]
        self.handle = None

    def request(self):
        """A method of the state that dynamically changes which
        class it uses depending on the value of self.handle"""
        self.handle = self.state_handles[random.randint(0, 2)]
        return self.handle

class IState(metaclass=ABCMeta):
    "A State Interface"

    @staticmethod
    @abstractmethod
    def __str__():
        "Set the default method"

class ConcreteStateA(IState):
    "A ConcreteState Subclass"

    def __str__(self):
        return "I am ConcreteStateA"

class ConcreteStateB(IState):
    "A ConcreteState Subclass"

    def __str__(self):
        return "I am ConcreteStateB"

class ConcreteStateC(IState):
    "A ConcreteState Subclass"

    def __str__(self):
        return "I am ConcreteStateC"

# The Client
CONTEXT = Context()
print(CONTEXT.request())
print(CONTEXT.request())
print(CONTEXT.request())
print(CONTEXT.request())
print(CONTEXT.request())
