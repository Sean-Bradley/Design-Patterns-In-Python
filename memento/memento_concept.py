"Memento pattern concept"


class Memento():  # pylint: disable=too-few-public-methods
    "A container of state"

    def __init__(self, state):
        self.state = state


class Originator():
    "The Object in the application whose state changes"

    def __init__(self):
        self._state = ""

    @property
    def state(self):
        "A `getter` for the objects state"
        return self._state

    @state.setter
    def state(self, state):
        print(f"Originator: Setting state to `{state}`")
        self._state = state

    @property
    def memento(self):
        "A `getter` for the objects state but packaged as a Memento"
        print("Originator: Providing Memento of state to caretaker.")
        return Memento(self._state)

    @memento.setter
    def memento(self, memento):
        self._state = memento.state
        print(
            f"Originator: State after restoring from Memento: "
            f"`{self._state}`")


class CareTaker():
    "Guardian. Provides a narrow interface to the mementos"

    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def create(self):
        "Store a new Memento of the Originators current state"
        print("CareTaker: Getting a copy of Originators current state")
        memento = self._originator.memento
        self._mementos.append(memento)

    def restore(self, index):
        """
        Replace the Originators current state with the state
        stored in the saved Memento
        """
        print("CareTaker: Restoring Originators state from Memento")
        memento = self._mementos[index]
        self._originator.memento = memento


# The Client
ORIGINATOR = Originator()
CARETAKER = CareTaker(ORIGINATOR)

# originators state can change periodically due to application events
ORIGINATOR.state = "State #1"
ORIGINATOR.state = "State #2"

# lets backup the originators
CARETAKER.create()

# more changes, and then another backup
ORIGINATOR.state = "State #3"
CARETAKER.create()

# more changes
ORIGINATOR.state = "State #4"
print(ORIGINATOR.state)

# restore from first backup
CARETAKER.restore(0)
print(ORIGINATOR.state)

# restore from second backup
CARETAKER.restore(1)
print(ORIGINATOR.state)
