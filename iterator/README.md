# Iterator Design Pattern

## Overview

The Iterator will commonly contain two methods that perform the following concepts.

* **next**: returns the next object in the aggregate (collection, object).
* **has_next**: returns a Boolean indicating if the Iterable is at the end of the iteration or not.

The benefits of using the Iterator pattern are that the client can traverse a collection of aggregates(objects) without needing to understand their internal representations and/or data structures.

## Terminology

* **Iterator Interface**: The Interface for an object to implement.
* **Concrete Iterator**: (Iterable) The instantiated object that implements the iterator and contains a collection of aggregates.
* **Aggregate Interface**: An interface for defining an aggregate (object).
* **Concrete Aggregate**: The object that implements the Aggregate interface.

## Iterator UML Diagram

![Iterator Pattern Overview](/img/iterator_concept.svg)

## Source Code

In this concept example, I create 4 objects called Aggregate and group them into a collection.

They are very minimal objects that implement one method that prints a line.

I then create an Iterable and pass in the collection of Aggregates.

I can now traverse the aggregates through the Iterable interface.

## Output

``` bash
python ./iterator/iterator_concept.py
This method has been invoked
This method has been invoked
This method has been invoked
This method has been invoked
```

## Example Use Case

One reason for not using the inbuilt Python data structures that implement iterators already, or using the [iter](#python-iter) function directly over an existing collection, is in the case when you want to create an object that can dynamically create iterated objects, you want a custom order of objects or an infinite iterator.

The iterator in this brief example will return the next number in the iterator multiplied by 2 modulus 11. It dynamically creates the returned object (number) at runtime.

It has no `has_next()` method since the result is modulated by 11, that will loop the results no matter how large the iterator index is. It will also appear to alternate between a series of even numbers and odd numbers.

Also, just to demonstrate that implementing abstract classes and interfaces is not always necessary, this example uses no abstract base classes or interfaces.

## Example UML Diagram

![Iterator Pattern Overview](/img/iterator_example.svg)

## Output

``` bash
python ./iterator/client.py
2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 0, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 0,
```

## New Coding Concepts

### Python iter()

Python [Lists](/builder#python-list), [Dictionaries](/singleton#python-dictionary), [Sets](/observer#python-set) and [Tuples](/bridge#python-tuple) are already iterable, so if you want basic iteration for use in a for loop, then you only need to add your objects into one of those and it can be used right away.

``` python
NAMES = ['SEAN','COSMO','EMMY']
for name in NAMES:
    print(name, end=", ")
#SEAN, COSMO, EMMY,
```

also, you can instantiate an iterable from the List, Dictionary, Tuple or Set by using the [Python iter()](#python-iter) method, or its own `__iter__()` dunder method, and then iterate over that using the `__next__()` method.

``` python
NAMES = ['SEAN','COSMO','EMMY']
ITERATOR = iter(NAMES)
print(ITERATOR.__next__())
print(ITERATOR.__next__())
print(ITERATOR.__next__())
```

or

``` python
NAMES = ['SEAN','COSMO','EMMY']
ITERATOR = NAMES.__iter__()
print(ITERATOR.__next__())
print(ITERATOR.__next__())
print(ITERATOR.__next__())
```

The Python `iter()` method also can accept a `sentinel` parameter. 

The `sentinel` parameter is useful for dynamically created objects that are returned from an iterator and indicates where the last item is in the iterator by raising a `StopIteration` exception. 

Usage : `iter(object, sentinel)`

When using the `sentinel`, the object passed as the first argument in the `iter()` method will need to be callable.

``` python
class Doubler():
    count = 1

    @classmethod
    def next(cls):
        cls.count *= 2
        return cls.count

    __call__ = next

ITERATOR = iter(Doubler(), 32)
print(list(ITERATOR))
# Outputs [2, 4, 8, 16]
```

The `__call__ = next` line in the example above is setting the default method of the class to be `next` and that makes the class callable. See [Dunder __call__ Method](/state#dunder-__call__-method) for more information.

Also note that the list being printed at the end is automatically filled from the iterator. The list constructor utilizes the default callable method and the `StopIteration` exception automatically during its creation without needing to write this in the code.

## Summary

* There are many ways to create Iterators. They are already built into Python and used instead of creating custom classes.
* Use an iterator when you need to traverse over a collection, or you want an object that can output a series of dynamically created objects.
* At minimum, an iterator needs a `next` equivalent method that returns an object. 
* Optionally you can also create a helper function that indicates whether an iterator is at the end or not. This is useful if you use your iterator in a `while` loop.
* Alternatively, use the `sentinel` option of the Python `iter()` method to indicate the last iteration. Note that the Iterator object needs to be callable. Set the `__call__` reference to its `next` method.
