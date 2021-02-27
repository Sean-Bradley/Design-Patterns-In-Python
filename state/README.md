# State Design Pattern

## Overview

Not to be confused with object state, i.e., one of more attributes that can be copied as a snapshot, the **State Pattern** is more concerned about changing the handle of an object's method dynamically. This makes an object itself more dynamic and may reduce the need of many conditional statements.

Instead of storing a value in an attribute, and then then using conditional statements within an objects method to produce different output, a subclass is assigned as a handle instead. The object/context doesn't need to know about the inner working of the assigned subclass that the task was delegated to. 

In the state pattern, the behavior of an objects state is encapsulated within the subclasses that are dynamically assigned to handle it.

## Terminology

* **State Interface**: An interface for encapsulating the behavior associated with a particular state of the Context.
* **Concrete Subclasses**: Each subclass implements a behavior associated with the particular state.
* **Context**: This is the object where the state is defined, but the execution of the state behavior is redirected to the concrete subclass.

## State UML Diagram

![State UML Diagram](/img/state_concept.svg)

## Source Code

In the concept example, there are three possible states. Every time the `request()` method is called, the concrete state subclass is randomly selected by the context.

### Output

``` bash
python.exe ./state/state_concept.py
I am ConcreteStateB
I am ConcreteStateA
I am ConcreteStateB
I am ConcreteStateA
I am ConcreteStateC
```

## State Example Use Case

This example takes the concept example further and uses an iterator rather than choosing the states subclasses randomly. 

When the iterator gets to the end, it raises a `StopIteration` error and recreates the iterator so that the process can loop again.

## State Example Use Case UML Diagram

![State Example Use Case UML Diagram](/img/state_example.svg)

## Output

``` bash
python.exe ./state/client.py
Task Started
Task Running
Task Finished
Task Started
Task Running
```

## New Coding Concepts

### Dunder `__call__` Method

Overloading the `__call__` method makes an instance of a class callable like a function when by default it isn't. You need to call a method within the class directly. 

``` python
class ExampleClass:
    @staticmethod
    def do_this_by_default():
        print("doing this")

EXAMPLE = ExampleClass()
EXAMPLE.do_this_by_default() # needs to be explicitly called to execute
```

If you want a default method in your class, you can point to it using by the `__call__` method.

``` python
class ExampleClass:
    @staticmethod
    def do_this_by_default():
        print("doing this")

    __call__ = do_this_by_default

EXAMPLE = ExampleClass()
EXAMPLE() # function now gets called by default
```

## Summary

* Makes an object change its behavior when its internal state changes. 
* The client and the context are not concerned about the details of how the state is created/assembled/calculated. The client will call a method of the context and it will be handled by a subclass.
* The State pattern appears very similar to the [Strategy](/strategy) pattern, except in the State pattern, the object/context has changed to a different state and will run a different subclass depending on that state.
