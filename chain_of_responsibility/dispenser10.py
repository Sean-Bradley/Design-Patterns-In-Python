"A dispenser of £10 notes"
from interface_dispenser import IDispenser


class Dispenser10(IDispenser):
    "Dispenses £10s if applicable, otherwise continues to next successor"

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        "Set the next successor"
        self._successor = successor

    def handle(self, amount):
        "Handle the dispensing of notes"
        if amount >= 10:
            num = amount // 10
            remainder = amount % 10
            print(f"Dispensing {num} £10 note")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
