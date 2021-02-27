"The Proteus Interface"

from abc import ABCMeta, abstractmethod


class IProteus(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    "A Greek mythological character that can change to many forms"

    @staticmethod
    @abstractmethod
    def tell_me_the_future():
        "Proteus will change form rather than tell you the future"

    @staticmethod
    @abstractmethod
    def tell_me_your_form():
        "The form of Proteus is elusive like the sea"
