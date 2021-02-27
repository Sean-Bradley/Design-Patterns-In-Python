# pylint: disable=too-few-public-methods
"The Template Method Pattern Concept"
from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):
    "A template class containing a template method and primitive methods"

    @staticmethod
    def step_one():
        """
        Hooks are normally empty in the abstract class. The
        implementing class can optionally override providing a custom
        implementation
        """

    @staticmethod
    @abstractmethod
    def step_two():
        """
        An abstract method that must be overridden in the implementing
        class. It has been given `@abstractmethod` decorator so that
        pylint shows the error.
        """

    @staticmethod
    def step_three():
        """
        Hooks can also contain default behavior and can be optionally
        overridden
        """
        print("Step Three is a hook that prints this line by default.")

    @classmethod
    def template_method(cls):
        """
        This is the template method that the subclass will call.
        The subclass (implementing class) doesn't need to override this
        method since it has would have already optionally overridden
        the following methods with its own implementations
        """
        cls.step_one()
        cls.step_two()
        cls.step_three()


class ConcreteClassA(AbstractClass):
    "A concrete class that only overrides step two"
    @staticmethod
    def step_two():
        print("Class_A : Step Two (overridden)")


class ConcreteClassB(AbstractClass):
    "A concrete class that only overrides steps one, two and three"
    @staticmethod
    def step_one():
        print("Class_B : Step One (overridden)")

    @staticmethod
    def step_two():
        print("Class_B : Step Two. (overridden)")

    @staticmethod
    def step_three():
        print("Class_B : Step Three. (overridden)")


# The Client
CLASS_A = ConcreteClassA()
CLASS_A.template_method()

CLASS_B = ConcreteClassB()
CLASS_B.template_method()
