"""
A component interface describing the common
fields and methods of leaves and composites
"""
from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    "The Component Interface"

    reference_to_parent = None

    @staticmethod
    @abstractmethod
    def dir(indent):
        "A method each Leaf and composite container should implement"

    @staticmethod
    @abstractmethod
    def detach():
        """
        Called before a leaf is attached to a composite
        so that it can clean any parent references
        """
