# pylint: disable=too-few-public-methods
"FactoryA Sample Code"
from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    "A Hypothetical Class Interface (Product)"

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method"


class ConcreteProductA(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductA"

    def create_object(self):
        return self


class ConcreteProductB(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductB"

    def create_object(self):
        return self


class ConcreteProductC(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductC"

    def create_object(self):
        return self


class FactoryA:
    "The FactoryA Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        try:
            if some_property == 'a':
                return ConcreteProductA()
            if some_property == 'b':
                return ConcreteProductB()
            if some_property == 'c':
                return ConcreteProductC()
            raise Exception('Class Not Found')
        except Exception as _e:
            print(_e)
        return None
