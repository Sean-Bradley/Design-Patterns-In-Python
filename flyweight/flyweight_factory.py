"Creating the FlyweightFactory as a singleton"
from flyweight import Flyweight


class FlyweightFactory():
    "Creating the FlyweightFactory as a singleton"

    _instance = None
    _flyweights: dict[int, Flyweight] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = FlyweightFactory
        return cls._instance

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
