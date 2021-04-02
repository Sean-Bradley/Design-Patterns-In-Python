# Decorator Design Pattern

## Videos

Section | Video Links
-|-
Decorator Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16397502/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Decorator Overview"><img src="/img/udemy_btn_sm.gif" alt="Decorator Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/XRCIKQD81rQ&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Decorator Overview"><img src="/img/yt_btn_sm.gif" alt="Decorator Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Decorator Overview"><img src="/img/skillshare_btn_sm.gif" alt="Decorator Overview"/></a>
Decorator Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25378590/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Decorator Use Case"><img src="/img/udemy_btn_sm.gif" alt="Decorator Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/8uDGo9DjHUc&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Decorator Use Case"><img src="/img/yt_btn_sm.gif" alt="Decorator Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Decorator Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Decorator Use Case"/></a>
**\__str\__** Dunder Method| <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25378604/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="__str__ Dunder Method"><img src="/img/udemy_btn_sm.gif" alt="__str__ Dunder Method"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/X84ZnxYGKFs&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="__str__ Dunder Method"><img src="/img/yt_btn_sm.gif" alt="__str__ Dunder Method"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="__str__ Dunder Method"><img src="/img/skillshare_btn_sm.gif" alt="__str__ Dunder Method"/></a>
Python **getattr()** Method | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25378618/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="getattr() Method"><img src="/img/udemy_btn_sm.gif" alt="getattr() Method"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/y27BD51JKU4&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="getattr() Method"><img src="/img/yt_btn_sm.gif" alt="getattr() Method"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="getattr() Method"><img src="/img/skillshare_btn_sm.gif" alt="getattr() Method"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

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

*...Refer to Book or Videos for extra content.*

<!-- Let's create a custom class called `Value` that will hold a number. 

Then add decorators that allow addition (`Add`) and subtraction (`Sub`) to a number (`Value`).

The `Add` and `Sub` decorators can accept integers directly, a custom `Value` object or other `Add` and `Sub` decorators.

`Add`, `Sub` and `Value` all implement the `IValue` interface and can be used recursively. -->

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

### Python `getattr()` Function

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

*...Refer to Book or Videos for extra content.*