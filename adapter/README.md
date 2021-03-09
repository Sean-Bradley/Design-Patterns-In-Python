# Adapter Design Pattern

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

Sometimes classes have been written and you don't have the option of modifying their interface to suit your needs. This happens if the method you are calling is on a different system across a network, a library that you may import or generally something that is not viable to modify directly for your particular needs.

The **Adapter** design pattern solves these problems:

* How can a class be reused that does not have an interface that a client requires?
* How can classes that have incompatible interfaces work together?
* How can an alternative interface be provided for a class?

You may have two classes that are similar, but they have different method signatures, so you create an Adapter over top of one of the method signatures so that it is easier to implement and extend in the client.

An adapter is similar to the [Decorator](/decorator) in the way that it also acts like a wrapper to an object. It is also used at runtime; however, it is not designed to be used recursively.

It is an alternative interface over an existing interface. It can also provide extra functionality that the interface being adapted may not already provide.

The adapter is similar to the [Facade](/facade), but you are modifying the method signature, combining other methods and/or transforming data that is exchanged between the existing interface and the client.

The Adapter is used when you have an existing interface that doesn't directly map to an interface that the client requires. So, then you create the Adapter which has a similar functional role, but with a new compatible interface.

## Terminology

* **Target**: The domain specific interface or class that needs to be adapted.
* **Adapter Interface**: The interface of the target that the adapter will need to implement.
* **Adapter**: The concrete adapter class containing the adaption process.
* **Client**: The client application that will use the Adapter.

## Adapter UML Diagram

![Adapter Pattern UML Diagram](/img/adapter_concept.svg)

## Source Code

In this concept source code, there are two classes, `ClassA` and `ClassB`, with different method signatures. Let's consider that `ClassA` provides the most compatible and preferred interface for the client.

I can create objects of both classes in the client and it works. But before using each objects method, I need to do a conditional check to see which type of class it is that I am calling since the method signatures are different.

It means that the client is doing extra work. Instead, I can create an Adapter interface for the incompatible `ClassB`, that reduces the need for the extra conditional logic.

## Output

``` bash
python ./adapter/adapter_concept.py
method A
method B
method A
method B
```

## Example Use Case

The example client can manufacture a **Cube** using different tools. Each solution is invented by a different company.
The client user interface manages the Cube product by indicating the **width**, **height** and **depth**. This is compatible with the company A that produces the Cube tool, but not the company B that produces their own version of the Cube tool that uses a different interface with different parameters. 

In this example, the client will re-use the interface for company A's Cube and create a compatible Cube from company B. 

An adapter will be needed so that the same method signature can be used by the client without the need to ask company B to modify their Cube tool for our specific domains use case.

My imaginary company needs to use both cube suppliers since there is a large demand for cubes and when one supplier is busy, I can then ask the other supplier.

## Example UML Diagram

![Adapter Pattern in Context](/img/adapter_example.svg)

## Output

``` bash
python ./adapter/client.py
Company A is busy, trying company B
Company B is busy, trying company A
Company A is busy, trying company B
Company B is busy, trying company A
Company A building Cube id:2968196317136, 2x3x7
Company A is busy, trying company B
Company B building Cube id:2968196317136, 8x2x8
Company A building Cube id:2968196317040, 4x6x4
Company A is busy, trying company B
Company B is busy, trying company A
Company A building Cube id:2968196317136, 5x4x8
Company A is busy, trying company B
Company B building Cube id:2968196317136, 2x2x9
5 cubes have been manufactured
```

## New Coding Concepts

### Python `isinstance()` Function

Syntax: `isinstance(object, type)`

Returns: `True` or `False`

You can use the inbuilt function `isinstance()` to conditionally check the `type` of an object.

``` python
>>> isinstance(1,int) 
True
>>> isinstance(1,bool) 
False
>>> isinstance(True,bool) 
True
>>> isinstance("abc",str)    
True
>>> isinstance("abc",(int,list,dict,tuple,set)) 
False
>>> isinstance("abc",(int,list,dict,tuple,set,str)) 
True
```

You can also test your custom classes.

``` python
class my_class:
    "nothing to see here"

CLASS_A = my_class()
print(type(CLASS_A))
print(isinstance(CLASS_A, bool))
print(isinstance(CLASS_A, my_class))
```

Outputs

``` 

<class '__main__.my_class'>
False
True
```

You can use it in logical statements as I do in [/adapter/adapter_concept.py](/adapter/adapter_concept.py).

### Python `time` Module

The time module provides time related functions, most notably in my case, the current epoch (ticks) since `January 1, 1970, 00:00:00 (UTC)` .

The `time` module provides many options that are outlined in more detail at [https://docs.python.org/3/library/time.html](https://docs.python.org/3/library/time.html)

In [/adapter/cube_a.py](/adapter/cube_a.py), I check the `time.time()` at various intervals to compare how long a task took. 

``` python
    now = int(time.time())
    if now > int(CubeA.last_time + 1):
        CubeA.last_time = now
        return True
```

I also use the `time` module to sleep for a second between loops to simulate a 1 second delay. See [/adapter/client.py](/adapter/client.py)

``` python
    # wait some time before manufacturing a new cube
    time.sleep(1)
```

When executing [/adapter/cube_a.py](/adapter/cube_a.py) you will notice that the process will run for about 10 seconds outputting the gradual progress of the construction of each cube.

## Summary

* Use the Adapter when you want to use an existing class, but its interface does not match what you need.
* The adapter adapts to the interface of its parent class for those situations when it is not viable to modify the parent class to be domain-specific for your use case.
* Adapters will most likely provide an alternative interface over an existing object, class or interface, but it can also provide extra functionality that the object being adapted may not already provide.
* An adapter is similar to a [Decorator](/decorator) except that it changes the interface to the object, whereas the decorator adds responsibility without changing the interface. This also allows the Decorator to be used recursively.
* An adapter is similar to the [Bridge](/bridge) pattern and may look identical after the refactoring has been completed. However, the intent of creating the Adapter is different. The Bridge is a result of refactoring existing interfaces, whereas the Adapter is about adapting over existing interfaces that are not viable to modify due to many existing constraints. E.g., you don't have access to the original code or it may have dependencies that already use it and modifying it would affect those dependencies negatively.
