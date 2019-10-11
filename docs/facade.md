# Facade Design Pattern

## Video Lecture
Skillshare : <a href="https://skl.sh/34SM2Xg" target="_blank" title="Facade Design Pattern">https://skl.sh/34SM2Xg</a>

Udemy : <a href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16397504/?referralCode=7B677DD7A9580F2FFD8F" target="_blank" title="Facade Design Pattern">Facade Design Pattern</a>

## Description

The Facade Pattern is a structural design pattern.
It provides a simplified interface to a set of other interfaces, abstractions and implementations within a system that may be full of complexity and/or tightly coupled.

![Facade Design Pattern](facade.png)

## Source Code

### **`facade.py`**
```python
class SubSystemClassA:
    @staticmethod
    def method():
        return "A"


class SubSystemClassB:
    @staticmethod
    def method():
        return "B"


class SubSystemClassC:
    @staticmethod
    def method():
        return "C"


# facade
class Facade:
    def __init__(self):
        self.sub_system_class_a = SubSystemClassA()
        self.sub_system_class_b = SubSystemClassB()
        self.sub_system_class_c = SubSystemClassC()

    def create(self):
        result = self.sub_system_class_a.method()
        result += self.sub_system_class_b.method()
        result += self.sub_system_class_c.method()
        return result


# client
FACADE = Facade()
RESULT = FACADE.create()
print("The Result = %s" % RESULT)

```