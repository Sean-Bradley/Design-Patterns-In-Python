# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
"Bridge Pattern Concept Sample Code"
from abc import ABCMeta, abstractmethod

class IAbstraction(metaclass=ABCMeta):
    "The Abstraction Interface"

    @staticmethod
    @abstractmethod
    def method(*args):
        "The method handle"

class RefinedAbstractionA(IAbstraction):
    "A Refined Abstraction"

    def __init__(self, implementer):
        self.implementer = implementer()

    def method(self, *args):
        self.implementer.method(*args)

class RefinedAbstractionB(IAbstraction):
    "A Refined Abstraction"

    def __init__(self, implementer):
        self.implementer = implementer()

    def method(self, *args):
        self.implementer.method(*args)

class IImplementer(metaclass=ABCMeta):
    "The Implementer Interface"

    @staticmethod
    @abstractmethod
    def method(*args: tuple) -> None:
        "The method implementation"

class ConcreteImplementerA(IImplementer):
    "A Concrete Implementer"

    @staticmethod
    def method(*args: tuple) -> None:
        print(args)

class ConcreteImplementerB(IImplementer):
    "A Concrete Implementer"

    @staticmethod
    def method(*args: tuple) -> None:
        for arg in args:
            print(arg)

# The Client
REFINED_ABSTRACTION_A = RefinedAbstractionA(ConcreteImplementerA)
REFINED_ABSTRACTION_A.method('a', 'b', 'c')

REFINED_ABSTRACTION_B = RefinedAbstractionB(ConcreteImplementerB)
REFINED_ABSTRACTION_B.method('a', 'b', 'c')
