# pylint: disable=too-few-public-methods
"The Facade pattern concept"


class SubSystemClassA:
    "A hypothetically complicated class"
    @staticmethod
    def method():
        "A hypothetically complicated method"
        return "A"


class SubSystemClassB:
    "A hypothetically complicated class"
    @staticmethod
    def method(value):
        "A hypothetically complicated method"
        return value


class SubSystemClassC:
    "A hypothetically complicated class"
    @staticmethod
    def method(value):
        "A hypothetically complicated method"
        return value


class Facade():
    "A simplified facade offering the services of subsystems"
    @staticmethod
    def sub_system_class_a():
        "Use the subsystems method"
        return SubSystemClassA().method()

    @staticmethod
    def sub_system_class_b(value):
        "Use the subsystems method"
        return SubSystemClassB().method(value)

    @staticmethod
    def sub_system_class_c(value):
        "Use the subsystems method"
        return SubSystemClassC().method(value)


# The Client
# call potentially complicated subsystems directly
print(SubSystemClassA.method())
print(SubSystemClassB.method("B"))
print(SubSystemClassC.method({"C": [1, 2, 3]}))

# or use the simplified facade
print(Facade().sub_system_class_a())
print(Facade().sub_system_class_b("B"))
print(Facade().sub_system_class_c({"C": [1, 2, 3]}))
