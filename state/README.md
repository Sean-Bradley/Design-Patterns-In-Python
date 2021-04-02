# State Design Pattern

## Videos

Section | Video Links
-|-
State Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25650184/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="State Overview"><img src="/img/udemy_btn_sm.gif" alt="State Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/Uh8hnm0jVgI&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="State Overview"><img src="/img/yt_btn_sm.gif" alt="State Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="State Overview"><img src="/img/skillshare_btn_sm.gif" alt="State Overview"/></a>
State Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25650190/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="State Use Case"><img src="/img/udemy_btn_sm.gif" alt="State Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/XMLVWYuxpuo&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="State Use Case"><img src="/img/yt_btn_sm.gif" alt="State Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="State Use Case"><img src="/img/skillshare_btn_sm.gif" alt="State Use Case"/></a>
**\_\_call\_\_** Attribute | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25650196/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Dunder __call__ Attribute"><img src="/img/udemy_btn_sm.gif" alt="Dunder __call__ Attribute"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/gGlSJo5NoRA&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Dunder __call__ Attribute"><img src="/img/yt_btn_sm.gif" alt="Dunder __call__ Attribute"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Dunder __call__ Attribute"><img src="/img/skillshare_btn_sm.gif" alt="Dunder __call__ Attribute"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

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

*...Refer to Book or Videos for extra content.*

<!-- In the concept example, there are three possible states. Every time the `request()` method is called, the concrete state subclass is randomly selected by the context. -->

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

*...Refer to Book or Videos for extra content.*

<!-- This example takes the concept example further and uses an iterator rather than choosing the states subclasses randomly. 

When the iterator gets to the end, it raises a `StopIteration` error and recreates the iterator so that the process can loop again. -->

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

*...Refer to Book or Videos for extra content.*