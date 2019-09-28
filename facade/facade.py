# complex parts
# subsystem ClassA
# subsystem ClassB
# subsystem ClassC

"""A Facade Demo"""


class SubSystemClassA:
    @staticmethod
    def func():
        return "A"


class SubSystemClassB:
    @staticmethod
    def func():
        return "B"


class SubSystemClassC:
    @staticmethod
    def func():
        return "C"


# facade
class Facade:
    def __init__(self):
        self.sub_system_class_a = SubSystemClassA()
        self.sub_system_class_b = SubSystemClassB()
        self.sub_system_class_c = SubSystemClassC()

    def do_func(self):
        result = self.sub_system_class_a.func()
        result += self.sub_system_class_b.func()
        result += self.sub_system_class_c.func()
        return result


# client
FACADE = Facade()
RESULT = FACADE.do_func()
print("The Result = %s" % RESULT)
