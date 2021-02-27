"A text document concrete class of AbstractDocument"
from abstract_document import AbstractDocument


class TextDocument(AbstractDocument):
    "Prints out a text document"
    @staticmethod
    def title(document):
        document["title"] = "New Text Document"

    @staticmethod
    def text(document, text):
        document["text"] = text

    @staticmethod
    def footer(document):
        document["footer"] = "-- Page 1 --"
