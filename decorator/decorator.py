"""
Decorator Pattern Example
"""


class UndecoratedObject:
    def get(self):
        # print("here")
        return "UndecoratedObject"


class Decorate:
    def __init__(self, decorated):
        self.decorated = decorated

    def get(self):
        return self.decorated.get().replace("Undecorated", "Decorated")


class DecorateWithANewMethod:
    def __init__(self, decorated):
        self.decorated = decorated

    def get(self):
        return self.decorated.get()

    def draw(self):
        print(self.decorated.get())


UNDECORATED = UndecoratedObject()
# print(UNDECORATED.get())
DECORATED = Decorate(UNDECORATED)
# print(DECORATED.get())
DECORATEDWITHNEWMETHOD = DecorateWithANewMethod(DECORATED)
DECORATEDWITHNEWMETHOD.draw()
