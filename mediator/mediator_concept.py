# pylint: disable=too-few-public-methods
"Mediator Concept Sample Code"


class Mediator():
    "The Mediator Concrete Class"

    def __init__(self):
        self.colleague1 = Colleague1()
        self.colleague2 = Colleague2()

    def colleague1_method(self):
        "Calls the method provided by Colleague1"
        return self.colleague1.method_1()

    def colleague2_method(self):
        "Calls the method provided by Colleague2"
        return self.colleague2.method_2()


class Colleague1():
    "This Colleague provides data for Colleague2"

    @staticmethod
    def method_1():
        "A simple method"
        return "Here is the Colleague1 specific data you asked for"


class Colleague2():
    "This Colleague provides data for Colleague1"

    @staticmethod
    def method_2():
        "A simple method"
        return "Here is the Colleague2 specific data you asked for"


# The Client
MEDIATOR = Mediator()

# Colleague1 wants some data from Colleague2
DATA = MEDIATOR.colleague2_method()
print(f"COLLEAGUE1 <--> {DATA}")

# Colleague2 wants some data from Colleague1
DATA = MEDIATOR.colleague1_method()
print(f"COLLEAGUE2 <--> {DATA}")
