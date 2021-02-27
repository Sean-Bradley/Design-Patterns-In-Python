"The Save/Restore Game functionality"


class CareTaker():
    "Guardian. Provides a narrow interface to the mementos"

    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def save(self):
        "Store a new Memento of the Characters current state"
        print("CareTaker: Game Save")
        memento = self._originator.memento
        self._mementos.append(memento)

    def restore(self, index):
        """
        Replace the Characters current attributes with the state
        stored in the saved Memento
        """
        print("CareTaker: Restoring Characters attributes from Memento")
        memento = self._mementos[index]
        self._originator.memento = memento
