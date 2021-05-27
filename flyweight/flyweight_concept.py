# pylint: disable=too-few-public-methods
"The Flyweight Concept"


class IFlyweight():
    "Nothing to implement"


class Flyweight(IFlyweight):
    "The Concrete Flyweight"

    def __init__(self, code: int) -> None:
        self.code = code


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


class Context():
    """
    An example context that holds references to the flyweights in a
    particular order and converts the code to an ascii letter
    """

    def __init__(self, codes: str) -> None:
        self.codes = list(codes)

    def output(self):
        "The context specific output that uses flyweights"
        ret = ""
        for code in self.codes:
            ret = ret + FlyweightFactory.get_flyweight(code).code
        return ret


# The Client
CONTEXT = Context("abracadabra")

# use flyweights in a context
print(CONTEXT.output())

print(f"abracadabra has {len('abracadabra')} letters")
print(f"FlyweightFactory has {FlyweightFactory.get_count()} flyweights")
