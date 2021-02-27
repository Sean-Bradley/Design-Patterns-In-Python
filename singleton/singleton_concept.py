# pylint: disable=too-few-public-methods
"Singleton Concept Sample Code"
import copy


class Singleton():
    "The Singleton Class"
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = Singleton
        return cls._instance

    @classmethod
    def class_method(cls):
        "A class level method"


# The Client
# All uses of singleton point to the same memory address (id)
print(f"id(Singleton)\t= {id(Singleton)}")
print(f"id(Singleton())\t= {id(Singleton())}")

OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

# And all singleton class methods will also all point to the same id
print(
    f"id(Singleton.class_method())\t= {id(Singleton.class_method())}")
print(
    f"id(Singleton().class_method())\t= {id(Singleton().class_method())}")
print(
    f"id(OBJECT1.class_method())\t= {id(OBJECT1.class_method())}")
print(
    f"id(OBJECT2.class_method())\t= {id(OBJECT2.class_method())}")
