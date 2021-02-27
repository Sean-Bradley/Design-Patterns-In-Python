"A Custom Parser for creating an Abstract Syntax Tree"

from number import Number
from add import Add
from subtract import Subtract
from roman_numeral import RomanNumeral


class Parser:
    "Dynamically create the Abstract Syntax Tree"

    @classmethod
    def parse(cls, sentence):
        "Create the AST from the sentence"

        tokens = sentence.split(" ")
        print(tokens)

        tree = []  # Abstract Syntax Tree
        while len(tokens) > 1:

            left_expression = cls.decide_left_expression(tree, tokens)

            # get the operator, make the token list shorter
            operator = tokens.pop(0)

            right = tokens[0]

            if not right.isdigit():
                tree.append(RomanNumeral(tokens[0]))
                if operator == '-':
                    tree.append(Subtract(left_expression, tree[-1]))
                if operator == '+':
                    tree.append(Add(left_expression, tree[-1]))
            else:
                right_expression = Number(right)
                if not tree:  
                    # Empty Data Structures return False by default
                    if operator == '-':
                        tree.append(
                            Subtract(left_expression, right_expression))
                    if operator == '+':
                        tree.append(
                            Add(left_expression, right_expression))
                else:
                    if operator == '-':
                        tree.append(Subtract(tree[-1], right_expression))
                    if operator == '+':
                        tree.append(Add(tree[-1], right_expression))

        return tree.pop()

    @staticmethod
    def decide_left_expression(tree, tokens):
        """
        On the First iteration, the left expression can be either a
        number or roman numeral. Every consecutive expression is
        reference to an existing AST row
        """
        left = tokens.pop(0)
        left_expression = None
        if not tree:  # only applicable if first round
            if not left.isdigit():  # if 1st token a roman numeral
                tree.append(RomanNumeral(left))
                left_expression = tree[-1]
            else:
                left_expression = Number(left)
        else:
            left_expression = tree[-1]
        return left_expression
