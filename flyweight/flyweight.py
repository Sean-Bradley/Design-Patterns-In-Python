"The Flyweight that contains an intrinsic value called code"


class Flyweight():  # pylint: disable=too-few-public-methods
    "The Flyweight that contains an intrinsic value called code"

    def __init__(self, code: str) -> None:
        self.code = code
