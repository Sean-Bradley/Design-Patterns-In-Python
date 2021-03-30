# Builder Design Pattern

## Videos

Section | Video Links
-|-
Builder Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16396852/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Builder Overview"><img src="/img/udemy_btn_sm.gif" alt="Builder Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/pMadA6F4zGU&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Builder Overview"><img src="/img/yt_btn_sm.gif" alt="Builder Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Builder Overview"><img src="/img/skillshare_btn_sm.gif" alt="Builder Overview"/></a>
Builder Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362124/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Builder Use Case"><img src="/img/udemy_btn_sm.gif" alt="Builder Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/xvwOwCNxIXM&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Builder Use Case"><img src="/img/yt_btn_sm.gif" alt="Builder Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Builder Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Builder Use Case"/></a>
Python **List** | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362168/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Python List"><img src="/img/udemy_btn_sm.gif" alt="Python List"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/54jpHGmHlHQ&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Python List"><img src="/img/yt_btn_sm.gif" alt="Python List"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Python List"><img src="/img/skillshare_btn_sm.gif" alt="Python List"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

The Builder Pattern is a creational pattern whose intent is to separate the construction of a complex object from its representation so that you can use the same construction process to create different representations.

The Builder Pattern tries to solve, 

* How can a class create different representations of a complex object?
* How can a class that includes creating a complex object be simplified?

The Builder and Factory patterns are very similar in the fact they both instantiate new objects at runtime. The difference is when the process of creating the object is more complex, so rather than the Factory returning a new instance of `ObjectA`, it calls the builders director constructor method `ObjectA.construct()` that goes through a more complex construction process involving several steps. Both return an Object/Product.

## Terminology

* **Product**: The Product being built.
* **Builder**: Builds the concrete product. Implements the `IBuilder` interface.
* **Builder Interface**: The Interface that the Concrete builder should implement.
* **Director**: Has a `construct()` method which when called creates a customized product.

## Builder UML Diagram

![Builder Pattern Overview](/img/builder_concept.svg)

## Source Code

1. Client creates the **Director**.
2. The Client calls the Directors `construct()` method that manages each step of the build process.
3. The Director returns the product to the client or alternatively could also provide a method for the client to retrieve it later.

## Output

``` bash
python ./builder/builder_concept.py
['a', 'b', 'c']
```

## Example Use Case

Using the Builder Pattern in the context of a House Builder. 

There are multiple directors that can create their own complex objects.

Note that in the `IglooDirector` class, not all of the methods of the `HouseBuilder` were called. 

The builder can construct complex objects in any order and include/exclude whichever parts it likes.

## Example UML Diagram

![Builder Pattern in Context](/img/builder_example.svg)

## Output

``` bash
python ./builder/client.py
This is a Ice Igloo with 1 door(s) and 0 window(s).
This is a Sandstone Castle with 100 door(s) and 200 window(s).
This is a Wood House Boat with 6 door(s) and 8 window(s).
```

## New Coding Concepts

### Python List

In the file [/builder/builder_concept.py](/builder/builder_concept.py)

``` python linenums="47"

    def __init__(self):
        self.parts = []

``` 

The `[]` is indicating a Python **List**.

The list can store multiple items, they can be changed, they can have items added and removed, can be re-ordered, can be pre-filled with items when instantiated and is also very flexible.

``` python
PS> python
>>> items = []
>>> items.append("shouldn't've")
>>> items.append("y'aint")
>>> items.extend(["whomst", "superfluity"])
>>> items
["shouldn't've", "y'aint", 'whomst', 'superfluity']
>>> items.reverse()
>>> items
['superfluity', 'whomst', "y'aint", "shouldn't've"]
>>> items.remove("y'aint")
>>> items
['superfluity', 'whomst', "shouldn't've"]
>>> items.insert(1, "phoque")
>>> items
['superfluity', 'phoque', 'whomst', "shouldn't've"]
>>> items.append("whomst")
>>> items.count("whomst")
2
>>> len(items)
5
>>> items[2] = "bagnose"
>>> items
['superfluity', 'phoque', 'bagnose', "shouldn't've", 'whomst']
>>> items[-2]
"shouldn't've"
```

Lists are used in almost every code example in this book. You will see all the many ways they can be used. 

In fact, a list was used in the [/abstract_factory/furniture_factory.py](/abstract_factory/furniture_factory.py) example, 

``` python
if furniture in ['SmallChair', 'MediumChair', 'BigChair']:
    ...
```

This line, creates a list at runtime including the strings 'SmallChair', 'MediumChair' and 'BigChair'. If the value in `furniture` equals the same string as one of those items in the list, then the condition is true and the code within the if statement block will execute.
