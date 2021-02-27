"A Memento to store character attributes"


class Memento():  # pylint: disable=too-few-public-methods
    "A container of characters attributes"

    def __init__(self, score, inventory, level, location):
        self.score = score
        self.inventory = inventory
        self.level = level
        self.location = location
