"The Game Character whose state changes"
from memento import Memento


class GameCharacter():
    "The Game Character whose state changes"

    def __init__(self):
        self._score = 0
        self._inventory = set()
        self._level = 0
        self._location = {"x": 0, "y": 0, "z": 0}

    @property
    def score(self):
        "A `getter` for the objects score"
        return self._score

    def register_kill(self):
        "The character kills its enemies as it progesses"
        self._score += 100

    def add_inventory(self, item):
        "The character finds objects in the game"
        self._inventory.add(item)

    def progress_to_next_level(self):
        "The characer progresses to the next level"
        self._level += 1

    def move_forward(self, amount):
        "The character moves around the environment"
        self._location["z"] += amount

    def __str__(self):
        return(
            f"Score: {self._score}, "
            f"Level: {self._level}, "
            f"Location: {self._location}\n"
            f"Inventory: {self._inventory}\n"
        )

    @ property
    def memento(self):
        "A `getter` for the characters attributes as a Memento"
        return Memento(
            self._score,
            self._inventory.copy(),
            self._level,
            self._location.copy())

    @ memento.setter
    def memento(self, memento):
        self._score = memento.score
        self._inventory = memento.inventory
        self._level = memento.level
        self._location = memento.location
