# pylint: disable=too-few-public-methods
"Abstract Factory Concept Sample Code"
from abc import ABCMeta, abstractmethod
from factory_a import FactoryA
from factory_b import FactoryB


class IAbstractFactory(metaclass=ABCMeta):
    "Abstract Factory Interface"

    @staticmethod
    @abstractmethod
    def create_object(factory):
        "The static Abstract factory interface method"


class AbstractFactory(IAbstractFactory):
    "The Abstract Factory Concrete Class"

    @staticmethod
    def create_object(factory):
        "Static get_factory method"
        try:
            if factory in ['aa', 'ab', 'ac']:
                return FactoryA().create_object(factory[1])
            if factory in ['ba', 'bb', 'bc']:
                return FactoryB().create_object(factory[1])
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None


# The Client
PRODUCT = AbstractFactory.create_object('ab')
print(f"{PRODUCT.__class__}")

PRODUCT = AbstractFactory.create_object('bc')
print(f"{PRODUCT.__class__}")
