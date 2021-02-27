"A Number. This is a leaf node Expression"
from abstract_expression import AbstractExpression

class Number(AbstractExpression):
    "Terminal Expression"

    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

    def __repr__(self):
        return str(self.value)
