from abc import ABCMeta, abstractmethod

class IMemento(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def save(msg):
        """The required save_memento method"""

    @staticmethod
    @abstractmethod
    def restore(msg):
        """The required restore_memento method"""


class Memento():
    def __init__(self, state):
        self._state = state

    def get(self):
        return self._state


class Thing(IMemento):  # Creator
    _state = ""

    def set(self, state):
        print("Originator: Setting state to", state)
        self._state = state

    def get(self):
        return self._state

    def save(self):
        print("Saving Memento.")
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get()
        print("Restoring Memento:", self._state)

# client
MEMENTOS = []
ORIGINAL_OBJECT = Thing()

ORIGINAL_OBJECT.set("State #1")
ORIGINAL_OBJECT.set("State #2")
MEMENTOS.append(ORIGINAL_OBJECT.save())

ORIGINAL_OBJECT.set("State #3")
MEMENTOS.append(ORIGINAL_OBJECT.save())

ORIGINAL_OBJECT.set("State #4")
print(ORIGINAL_OBJECT.get())

ORIGINAL_OBJECT.restore(MEMENTOS[0])
print(ORIGINAL_OBJECT.get())

ORIGINAL_OBJECT.restore(MEMENTOS[1])
print(ORIGINAL_OBJECT.get())
