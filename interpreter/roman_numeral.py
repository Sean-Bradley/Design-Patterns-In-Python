# pylint: disable=too-few-public-methods
"Roman Numeral Expression. This is a Non-Terminal Expression"
from abstract_expression import AbstractExpression
from number import Number


class RomanNumeral(AbstractExpression):
    "Non Terminal expression"

    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral
        self.context = [roman_numeral, 0]

    def interpret(self):
        RomanNumeral1000.interpret(self.context)
        RomanNumeral100.interpret(self.context)
        RomanNumeral10.interpret(self.context)
        RomanNumeral1.interpret(self.context)
        return Number(self.context[1]).interpret()

    def __repr__(self):
        return f"{self.roman_numeral}({self.context[1]})"


class RomanNumeral1(RomanNumeral):
    "Roman Numerals 1 - 9"
    one = "I"
    four = "IV"
    five = "V"
    nine = "IX"
    multiplier = 1

    @classmethod
    def interpret(cls, *args):

        context = args[0]

        if not context[0]:
            return Number(context[1]).interpret()

        if context[0][0: 2] == cls.nine:
            context[1] += (9 * cls.multiplier)
            context[0] = context[0][2:]
        elif context[0][0] == cls.five:
            context[1] += (5 * cls.multiplier)
            context[0] = context[0][1:]
        elif context[0][0: 2] == cls.four:
            context[1] += + (4 * cls.multiplier)
            context[0] = context[0][2:]

        while context[0] and context[0][0] == cls.one:
            context[1] += (1 * cls.multiplier)
            context[0] = context[0][1:]

        return Number(context[1]).interpret()


class RomanNumeral10(RomanNumeral1):
    "Roman Numerals 10 - 99"
    one = "X"
    four = "XL"
    five = "L"
    nine = "XC"
    multiplier = 10


class RomanNumeral100(RomanNumeral1):
    "Roman Numerals 100 - 999"
    one = "C"
    four = "CD"
    five = "D"
    nine = "CM"
    multiplier = 100


class RomanNumeral1000(RomanNumeral1):
    "Roman Numerals 1000 - 3999"
    one = "M"
    four = ""
    five = ""
    nine = ""
    multiplier = 1000
