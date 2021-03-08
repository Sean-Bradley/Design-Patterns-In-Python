# pylint: disable=too-few-public-methods
"Prototype Concept Sample Code"
from abc import ABCMeta, abstractmethod


class IProtoType(metaclass=ABCMeta):
    "interface with clone method"
    @staticmethod
    @abstractmethod
    def clone():
        """The clone, deep or shallow.
        It is up to you how you want to implement
        the details in your concrete class"""


class MyClass(IProtoType):
    "A Concrete Class"

    def __init__(self, field):
        self.field = field  # any value of any type

    def clone(self):
        " This clone method uses a shallow copy technique "
        return type(self)(
            self.field  # a shallow copy is returned
            # self.field.copy() # this is also a shallow copy, but has
            # also shallow copied the first level of the field. So it
            # is essentially a shallow copy but 2 levels deep. To
            # recursively deep copy collections containing inner
            # collections,
            # eg lists of lists,
            # Use https://docs.python.org/3/library/copy.html instead.
            # See example below.
        )

    def __str__(self):
        return f"{id(self)}\tfield={self.field}\ttype={type(self.field)}"


# The Client
OBJECT1 = MyClass([1, 2, 3, 4])  # Create the object containing a list
print(f"OBJECT1 {OBJECT1}")

OBJECT2 = OBJECT1.clone()  # Clone

# Change the value of one of the list elements in OBJECT2,
# to see if it also modifies the list element in OBJECT1.
# If it changed OBJECT1s copy also, then the clone was done
# using a 1 level shallow copy process.
# Modify the clone method above to try a 2 level shallow copy instead
# and compare the output
OBJECT2.field[1] = 101

# Comparing OBJECT1 and OBJECT2
print(f"OBJECT2 {OBJECT2}")
print(f"OBJECT1 {OBJECT1}")
