"An abstract document containing a combination of hooks and abstract methods"
from abc import ABCMeta, abstractmethod


class AbstractDocument(metaclass=ABCMeta):
    "A template class containing a template method and primitive methods"

    @staticmethod
    @abstractmethod
    def title(document):
        "must implement"

    @staticmethod
    def description(document):
        "optional"

    @staticmethod
    def author(document):
        "optional"

    @staticmethod
    def background_colour(document):
        "optional with a default behavior"
        document["background_colour"] = "white"

    @staticmethod
    @abstractmethod
    def text(document, text):
        "must implement"

    @staticmethod
    def footer(document):
        "optional"

    @staticmethod
    def print(document):
        "optional with a default behavior"
        print("----------------------")
        for attribute in document:
            print(f"{attribute}\t: {document[attribute]}")
        print()

    @classmethod
    def create_document(cls, text):
        "The template method"
        _document = {}
        cls.title(_document)
        cls.description(_document)
        cls.author(_document)
        cls.background_colour(_document)
        cls.text(_document, text)
        cls.footer(_document)
        cls.print(_document)
