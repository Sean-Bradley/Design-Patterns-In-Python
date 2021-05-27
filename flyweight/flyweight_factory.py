"Creating the FlyweightFactory as a singleton"
from flyweight import Flyweight


class FlyweightFactory():
    "Creating the FlyweightFactory as a singleton"

    _flyweights: dict[int, Flyweight] = {}  # Python 3.9
    # _flyweights = {}  # Python 3.8 or earlier

    def __new__(cls):
        return cls

    @classmethod
    def get_flyweight(cls, code: int) -> Flyweight:
        "A static method to get a flyweight based on a code"
        if not code in cls._flyweights:
            cls._flyweights[code] = Flyweight(code)
        return cls._flyweights[code]

    @classmethod
    def get_count(cls) -> int:
        "Return the number of flyweights in the cache"
        return len(cls._flyweights)
