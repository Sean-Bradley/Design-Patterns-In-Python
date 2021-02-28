# Decorator Design Pattern

## Overview

The **decorator pattern** is a structural pattern, that allows you to attach additional responsibilities to an object at runtime.

The decorator pattern is used in both the Object Oriented and Functional paradigms.

The decorator pattern is different than the Python language feature of [Python Decorators](https://www.python.org/dev/peps/pep-0318/#on-the-name-decorator) in its syntax and complete purpose. It is a similar concept in the way that it is a wrapper, but it also can be applied at runtime dynamically.

The decorator pattern adds extensibility without modifying the original object.

The decorator forwards requests to the enclosed object and can perform extra actions. 

You can nest decorators recursively.

## Terminology

* **Component Interface**: An interface for objects.
* **Component**: The object that may be decorated.
* **Decorator**: The class that applies the extra responsibilities to the component being decorated. It also implements the same component interface.

## Builder UML Diagram

![Decorator Pattern UML Diagram](/img/decorator_concept.svg)

## Output

``` bash
python ./decorator/decorator_concept.py
Component Method
Decorator Method(Component Method)
```

## Example Use Case

Let's create a custom class called `Value` that will hold a number. 

Then add decorators that allow addition (`Add`) and subtraction (`Sub`) to a number (`Value`).

The `Add` and `Sub` decorators can accept integers directly, a custom `Value` object or other `Add` and `Sub` decorators.

`Add`, `Sub` and `Value` all implement the `IValue` interface and can be used recursively.

## Example UML Diagram

![Decorator Pattern in Context](/img/decorator_example.svg)

## Output

``` bash
python ./decorator/client.py
3
101
4
6
-1
106
113
114
1
2
5
```

## New Coding Concepts

### Python `getattr*()` Function

Syntax: `getattr(object, attribute, default)`

In the `Sub` and `Add` classes, I use the `getattr()` method like a ternary operator. 

When initializing the `Add` or `Sub` classes, you have the option of providing an integer or an existing instance of the `Value`, `Sub` or `Add` classes. 

So, for example, the line in the `Sub` class, 

``` python

val1 = getattr(val1, 'value', val1)
```

is saying, if the `val1` just passed into the function already has an attribute `value`, then `val1` must be an object of `Value`, `Sub` or `Add` . Otherwise, the `val1` that was passed in is a new integer and it will use that instead to calculate the final value of the instance on the next few lines of code. This behavior allows the `Sub` and `Add` classes to be used recursively. 

E.g., 

``` python
A = Value(2)
Add(Sub(Add(200, 15), A), 100)
```

### Dunder `__str__` method

When you `print()` an object, it will print out the objects type and memory location in hex.

``` python
class ExampleClass:
    abc = 123

print(ExampleClass())
```

Outputs

``` text
<__main__.ExampleClass object at 0x00000283038B1D00>
```

You can change this default output by implementing the `__str__` dunder method in your class. Dunder is short for saying double underscore. 

Dunder methods are predefined methods in python that you can override with your own implementations.

``` python
class ExampleClass:
    abc = 123

    def __str__(self):
        return "Something different"

print(ExampleClass())
```

Now outputs

``` text
Something different
```

In all the classes in the above use case example that implement the `IValue` interface, the `__str__` method is overridden to return a string version of the integer value. This allows to print the numerical value of any object that implements the `IValue` interface rather than printing a string that resembles something like below.

``` bash
<__main__.ValueClass object at 0x00000283038B1D00>
```

The `__str__` dunder was also overridden in the [/prototype/prototype_concept.py](/prototype/prototype_concept.py) concept code.

## Summary

* Use the decorator when you want to add responsibilities to objects dynamically without affecting the inner object.
* You want the option to later remove the decorator from an object in case you no longer need it.
* It is an alternative method to creating multiple combinations of subclasses. I.e., Instead of creating a subclass with all combinations of objects A, B, C in any order, and including/excluding objects, you could create 3 objects that can decorate each other in any order you want. E.g., (D(A(C))) or (B(C)) or (A(B(A(C)))
* The decorator, compared to using static inheritance to extend, is more flexible since you can easily add/remove the decorators at runtime. E.g., use in a recursive function.
* A decorator supports recursive composition. E.g., halve(halve(number))
* A decorator shouldn't modify the internal objects data or references. This allows the original object to stay intact if the decorator is later removed.