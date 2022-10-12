# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
"Decorator Concept Sample Code"
from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    "Methods the component must implement"
    @staticmethod
    @abstractmethod
    def method():
        "A method to implement"


class Component(IComponent):
    "A component that can be decorated or not"

    def method(self):
        "An example method"
        return "Component Method"


class Decorator(IComponent):
    "The Decorator also implements the IComponent"

    def __init__(self, obj):
        "Set a reference to the decorated object"
        self.object = obj

    def method(self):
        "A method to implement"
        return f"Decorator Method({self.object.method()})"


# The Client
COMPONENT = Component()
print(COMPONENT.method())
print(Decorator(COMPONENT).method())
