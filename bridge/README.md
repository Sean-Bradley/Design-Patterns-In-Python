# Bridge Design Pattern

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

The **Bridge pattern** is similar to the [Adapter](/adapter) pattern except in the intent that you developed it. 

The Bridge is an approach to refactor already existing code, whereas the Adapter creates an interface on top of existing code through existing available means without refactoring any existing code or interfaces.

The motivation for converting your code to the Bridge pattern is that it may be tightly coupled. There is logic and abstraction close together that is limiting your choices in how you can extend your solution in the way that you need.

E.g., you may have one Car class, that produces a very nice car. But you would like the option of varying the design a little, or outsourcing responsibility of creating the different components.

The Bridge pattern is a process about separating abstraction and implementation, so this will give you plenty of new ways of using your classes.

``` python
CAR = Car()
print(CAR)
> Car has wheels and engine and windows and everything else. 
```

But you would like to delegate the engine dynamically from a separate set of classes or solutions.

``` python
ENGINE = EngineA()
CAR = Car(EngineA)
```

A Bridge didn't exist before, but since after the separation of interface and logic, each side can be extended independently of each other.

Also, the application of a Bridge in your code should use composition instead of inheritance. This means that you assign the relationship at runtime, rather than hard coded in the class definition.

I.e., `CAR = Car(EngineA)` rather than `class Car(EngineA):`

A Bridge implementation will generally be cleaner than an Adapter solution that was bolted on. Since it involved refactoring existing code, rather than layering on top of legacy or third-party solutions that may not have been intended for your particular use case.

You are the designer of the Bridge, but both approaches to the problem may work regardless.

The implementer part of a Bridge, can have one or more possible implementations for each refined abstraction. E.g., The implementor can print to paper, or screen, or format for a web browser. And the abstraction side could allow for many permutations of every shape that you can imagine.

## Terminology

* **Abstraction Interface**: An interface implemented by the refined abstraction describing the common methods to implement.
* **Refined Abstraction**: A refinement of an idea into another class or two. The classes should implement the Abstraction Interface and assign which concrete implementer.
* **Implementer Interface**: The implementer interface that concrete implementers implement.
* **Concrete Implementer**: The implementation logic that the refined abstraction will use.

## Bridge UML Diagram

![Bridge Pattern UML Diagram](/img/bridge_concept.svg)

## Source Code

In the concept demonstration code, imagine that the classes were tightly coupled. The concrete class would print out some text to the console.

After abstracting the class along a common ground, it is now more versatile. The implementation and has been separated from the abstraction and now it can print out the same text in two different ways.

The befit now is that each refined abstraction and implementer can now be worked on independently without affecting the other implementations.

## Output

``` bash
python ./bridge/bridge_concept.py
('a', 'b', 'c')
a
b
c
```

## Example Use Case

In this example, I draw a square and a circle. Both of these can be categorized as shapes.

The shape is set up as the abstraction interface. The refined abstractions, `Square` and `Circle`, implement the `IShape` interface.

When the Square and Circle objects are created, they are also assigned their appropriate implementers being `SquareImplementer` and `CircleImplementer` .

When each shape's `draw` method is called, the equivalent method within their implementer is called.

The Square and Circle are bridged and each implementer and abstraction can be worked on independently.

## Example UML Diagram

![Bridge Pattern in Context](/img/bridge_example.svg)

## Output

``` bash
python ./bridge/client.py
    ******
  **      **
 *          *
*            *
*            *
 *          *
  **      **
    ******
**************
*            *
*            *
*            *
*            *
*            *
*            *
**************
```

## New Coding Concepts

### The `*args` Argument. 

The `*args` argument takes all arguments that were sent to this method, and packs them into a [Tuple](#python-tuple).

It is useful when you don't know how many arguments, or what types, will be sent to a method, and you want the method to support any number of arguments or types being sent to it. 

If you want your method to be strict about the types that it can accept, the set it specifically to accept [List](/builder#python-list), [Dictionary](/singleton#python-dictionary), [Set](/observer#python-set) or [Tuple](#python-tuple), and treat the argument as such within the method body, but the `*args` argument is another common option that you will see in source code throughout the internet.

E.g., when using the `*args` in your method signature, you can call it with any number of arguments of any type.

``` python
def my_method(*args):
    for arg in args:
        print(arg)

my_method(1, 22, [3], {4})
```

Outputs

``` bash
1
22
[3]
{4}
```

### Python Tuple

A Python **Tuple** is similar to a [List](/builder#python-list). Except that the items in the Tuple are ordered, unchangeable and allow duplicates.

A Tuple can be instantiated using the round brackets `()` or `tuple()`, verses `[]` for a [List](/builder#python-list) and `{}` for a [Set](/observer#python-set) or [Dictionary](/singleton#python-dictionary).

``` python
PS> python
>>> items = ("alpha", "bravo", "charlie", "alpha")
>>> print(items)
('alpha', 'bravo', 'charlie', 'alpha')
>>> print(len(items))
4
```

## Summary

* Use when you want to separate a solution where the abstraction and implementation may be tightly coupled and you want to break it up into smaller conceptual parts.
* Once you have added the bridge abstraction, you should be able to extend each side of it separately without breaking the other.
* Also, once the bridge abstraction exists, you can more easily create extra concrete implementations for other similar products that may also happen to be split across similar conceptual lines.
* The Bridge pattern is similar to the adapter pattern except in the intent that you developed it. The bridge is an approach to refactor already existing code, whereas the adapter adapts to the existing code through its existing interfaces and methods without changing the internals.
