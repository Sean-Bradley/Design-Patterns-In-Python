"""
Memento pattern example.
"""


class Memento():
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator():
    _state = ""

    def set_state(self, state):
        print("Originator: Setting state to", state)
        self._state = state

    def get_state(self):
        return self._state

    def save_to_memento(self):
        print("Originator: Saving to Memento.")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()
        print("Originator: State after restoring from Memento:", self._state)


class CareTaker():
    _memento_list = []

    def add(self, state):
        self._memento_list.append(state)

    def get(self, index):
        return self._memento_list[index]


# client
ORIGINATOR = Originator()
CARETAKER = CareTaker()

ORIGINATOR.set_state("State #1")
ORIGINATOR.set_state("State #2")
CARETAKER.add(ORIGINATOR.save_to_memento())

ORIGINATOR.set_state("State #3")
CARETAKER.add(ORIGINATOR.save_to_memento())

ORIGINATOR.set_state("State #4")
print(ORIGINATOR.get_state())

ORIGINATOR.restore_from_memento(CARETAKER.get(0))
print(ORIGINATOR.get_state())

ORIGINATOR.restore_from_memento(CARETAKER.get(1))
print(ORIGINATOR.get_state())
