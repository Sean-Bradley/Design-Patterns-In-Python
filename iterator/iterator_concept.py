# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
"The Iterator Pattern Concept"
from abc import ABCMeta, abstractmethod


class IIterator(metaclass=ABCMeta):
    "An Iterator Interface"
    @staticmethod
    @abstractmethod
    def has_next():
        "Returns Boolean whether at end of collection or not"

    @staticmethod
    @abstractmethod
    def next():
        "Return the object in collection"


class Iterable(IIterator):
    "The concrete iterator (iterable)"

    def __init__(self, aggregates):
        self.index = 0
        self.aggregates = aggregates

    def next(self):
        if self.index < len(self.aggregates):
            aggregate = self.aggregates[self.index]
            self.index += 1
            return aggregate
        raise Exception("AtEndOfIteratorException", "At End of Iterator")

    def has_next(self):
        return self.index < len(self.aggregates)


class IAggregate(metaclass=ABCMeta):
    "An interface that the aggregates should implement"
    @staticmethod
    @abstractmethod
    def method():
        "a method to implement"


class Aggregate(IAggregate):
    "A concrete object"
    @staticmethod
    def method():
        print("This method has been invoked")


# The Client
AGGREGATES = [Aggregate(), Aggregate(), Aggregate(), Aggregate()]
# AGGREGATES is a python list that is already iterable by default.

# but we can create own own iterator on top anyway.
ITERABLE = Iterable(AGGREGATES)

while ITERABLE.has_next():
    ITERABLE.next().method()
