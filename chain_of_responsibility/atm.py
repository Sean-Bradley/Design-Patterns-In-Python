"""Chain of Responsibility Pattern
Chain of responsibility pattern is a behavioral pattern used to achieve loose coupling
in software design.
Example, a request from a client is passed to a chain of objects to process them. 
The objects in the chain will decide themselves how the request is handled and/or 
passed to the next processor in the chain.
"""

from abc import ABCMeta, abstractstaticmethod


class IDispenseChain(metaclass=ABCMeta):

    @abstractstaticmethod
    def set_next_chain(next_chain):
        """Set the next processor in the chain"""

    @abstractstaticmethod
    def dispense(currency):
        """Dispense the amount"""


class Dispenser50(IDispenseChain):

    def __init__(self):
        self.chain = None

    def set_next_chain(self, next_chain):
        self.chain = next_chain

    def dispense(self, amount):
        if amount >= 50:
            num = amount // 50
            remainder = amount % 50
            print(f"Dispensing {num} £50 note")
            if remainder != 0:
                self.chain.dispense(remainder)
        else:
            self.chain.dispense(amount)


class Dispenser20(IDispenseChain):

    def __init__(self):
        self.chain = None

    def set_next_chain(self, next_chain):
        self.chain = next_chain

    def dispense(self, amount):
        if amount >= 20:
            num = amount // 20
            remainder = amount % 20
            print(f"Dispensing {num} £20 note")
            if remainder != 0:
                self.chain.dispense(remainder)
        else:
            self.chain.dispense(amount)


class Dispenser10(IDispenseChain):

    def __init__(self):
        self.chain = None

    def set_next_chain(self, next_chain):
        self.chain = next_chain

    def dispense(self, amount):
        if amount >= 10:
            num = amount // 10
            remainder = amount % 10
            print(f"Dispensing {num} £10 note")
            if remainder != 0:
                self.chain.dispense(remainder)
        else:
            self.chain.dispense(amount)


class ATMDispenserChain:

    def __init__(self):
        # initialize the chain

        self.chain1 = Dispenser50()
        self.chain2 = Dispenser20()
        self.chain3 = Dispenser10()

        # set the chain of responsibility
        self.chain1.set_next_chain(self.chain2)
        self.chain2.set_next_chain(self.chain3)


if __name__ == "__main__":

    ATM = ATMDispenserChain()
    
    print("Enter amount to withdrawal")
    AMOUNT = int(input())
    if AMOUNT % 10 != 0:
        print("Amount should be in multiple of 10s.")
    # process the request
    ATM.chain1.dispense(AMOUNT)
