"A dispenser of £50 notes"
from interface_dispenser import IDispenser


class Dispenser50(IDispenser):
    "Dispenses £50s if applicable, otherwise continues to next successor"

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        "Set the next successor"
        self._successor = successor

    def handle(self, amount):
        "Handle the dispensing of notes"
        if amount >= 50:
            num = amount // 50
            remainder = amount % 50
            print(f"Dispensing {num} £50 note(s)")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
