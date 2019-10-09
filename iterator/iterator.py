from abc import ABCMeta, abstractmethod


class IIterator(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def has_next():
        """Returns Boolean whether at end of collection or not"""

    @staticmethod
    @abstractmethod
    def next():
        """Return the object in collection"""

class MyCars(IIterator):
    def __init__(self):
        self.index = 0

    def next(self):
        if self.index < 7:
            x = self.index
            self.index += 1
            return x
        else:
            raise Exception("AtEndOfIteratorException", "At End of Iterator")

    def has_next(self):
        return self.index < 7


myclass = MyCars()
#myiter = iter(myclass)

print(myclass.next())
print(myclass.next())
print(myclass.next())
print(myclass.next())

print()
while myclass.has_next(): #or x in myiter:
    print(myclass.next())
