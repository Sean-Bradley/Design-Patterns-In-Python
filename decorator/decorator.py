"""
Decorator Design Pattern
"""

class UndecoratedObject:
    @staticmethod
    def get():
        return "UndecoratedObject"


class Decorate:
    def __init__(self, undecorated):
        self.undecorated = undecorated

    def get(self):
        return self.undecorated.get().replace("Undecorated", "Decorated")


# class DecorateWithANewMethod:
#     def __init__(self, undecorated):
#         self.undecorated = undecorated

#     def get(self):
#         return self.undecorated.get()

#     def draw(self):
#         print(self.undecorated.get())


UNDECORATED = UndecoratedObject()
print(UNDECORATED.get())
DECORATED = Decorate(UNDECORATED)
print(DECORATED.get())
#DECORATEDWITHNEWMETHOD = DecorateWithANewMethod(DECORATED)
#DECORATEDWITHNEWMETHOD.draw()
