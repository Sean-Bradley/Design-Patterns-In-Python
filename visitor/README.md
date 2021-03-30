# Visitor Design Pattern

## Videos

Section | Video Links
-|-
Visitor Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25697738/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Visitor Overview"><img src="/img/udemy_btn_sm.gif" alt="Visitor Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/KLFLsDV-LXw&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Visitor Overview"><img src="/img/yt_btn_sm.gif" alt="Visitor Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Visitor Overview"><img src="/img/skillshare_btn_sm.gif" alt="Visitor Overview"/></a>
Visitor Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25697742/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Visitor Use Case"><img src="/img/udemy_btn_sm.gif" alt="Visitor Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/9JJO2ZaZD3A&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Visitor Use Case"><img src="/img/yt_btn_sm.gif" alt="Visitor Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Visitor Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Visitor Use Case"/></a>
hasattr() Method | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25697748/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="hasattr() Method"><img src="/img/udemy_btn_sm.gif" alt="hasattr() Method"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/cWNARNXP6dE&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="hasattr() Method"><img src="/img/yt_btn_sm.gif" alt="hasattr() Method"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="hasattr() Method"><img src="/img/skillshare_btn_sm.gif" alt="hasattr() Method"/></a>
expandtabs() Method | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25697758/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="expandtabs() Method"><img src="/img/udemy_btn_sm.gif" alt="expandtabs() Method"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/FT6XGI2vJqQ&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="expandtabs() Method"><img src="/img/yt_btn_sm.gif" alt="expandtabs() Method"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="expandtabs() Method"><img src="/img/skillshare_btn_sm.gif" alt="expandtabs() Method"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

Your object structure inside an application may be complicated and varied. A good example is what could be created using the [Composite](/composite) structure.

The objects that make up the hierarchy of objects, can be anything and most likely complicated to modify as your application grows. 

Instead, when designing the objects in your application that may be structured in a hierarchical fashion, you can allow them to implement a **Visitor** interface. 

The Visitor interface describes an `accept()` method that a different object, called a Visitor, will use in order to traverse through the existing object hierarchy and read the internal attributes of an object.

The Visitor pattern is useful when you want to analyze, or reproduce an alternative object hierarchy without implementing extra code in the object classes, except for the original requirements set by implementing the Visitor interface.

Similar to the template pattern it could be used to output different versions of a document but more suited to objects that may be members of a hierarchy.

## Terminology

* **Visitor Interface**: An interface for the Concrete Visitors.
* **Concrete Visitor**: The Concrete Visitor will traverse the hierarchy of elements.
* **Visitable Interface**: The interface that elements should implement which describes the `accept()` method that will allow them to be visited (traversed).
* **Concrete Element**: An object that will be visited. An application will contain a variable number of Elements than can be structured in any particular hierarchy.

## Visitor UML Diagram

![Visitor Pattern UML Diagram](/img/visitor_concept.svg)

## Source Code

In the concept code below, a hierarchy of any object is created. It is similar to a simplified composite. The objects of `Element` can also contain a hierarchy of sub elements.

The `Element` class could also consist of many variations, but this example uses only one.

Rather than writing specific code inside all these elements every time I wanted to handle a new custom operation, I can implement the `IVisitable` interface and create the `accept()` method which allows the Visitor to pass through it and access the Elements internal attributes.

Two different Visitor classes are created, `PrintElementNamesVisitor` and `CalculateElementTotalsVisitor` . They are instantiated and passed through the existing Object hierarchy using the same `IVisitable` interface.

## Output

``` bash
python ./visitor/visitor_concept.py  
D
B
C
A
561
```

## Visitor Example Use Case

In the example, the client creates a car with parts. 

The car and parts inherit an abstract car parts class with predefined property getters and setters. 

Instead of creating methods in the car parts classes and abstract class that run bespoke methods, the car parts can all implement the `IVisitor` interface.

This allows for the later creation of Visitor objects to run specific tasks on the existing hierarchy of objects.

## Visitor Example UML Diagram

![Visitor Pattern Use Case UML Diagram](/img/visitor_example.svg)

## Output

``` bash
python ./visitor/client.py
Utility     :ABC-123-21
V8 engine   :DEF-456-21
FrontLeft   :GHI-789FL-21
FrontRight  :GHI-789FR-21
BackLeft    :GHI-789BL-21
BackRight   :GHI-789BR-21
Total Price = 4132
```

## New Coding Concepts

### Instance `hasattr()`

In the Visitor objects in the example use case above, I test if the elements have a certain attribute during the visit operation.

``` python
def visit(cls, element):
    if hasattr(element, 'price'):
        ...
```

The `hasattr()` method can be used to test if an instantiated object has an attribute of a particular name.

``` python
class ClassA():
    name = "abc"
    value = 123

CLASS_A = ClassA()
print(hasattr(CLASS_A, "name"))
print(hasattr(CLASS_A, "value"))
print(hasattr(CLASS_A, "date"))

```

Outputs

``` bash
True
True
False
```

### String `expandtabs()`

When printing strings to the console, you can include special characters `\t` that print a series of extra spaces called tabs. The tabs help present multiline text in a more tabular form which appears to be neater to look at. 

``` bash
abc    123
defg   456
hi     78910
```

The number of spaces added depends on the size of the word before the `\t` character in the string. By default, a tab makes up 8 spaces.

Now, not all words separated by a tab will line up the same on the next line.

``` bash
abcdef  123
cdefghij        4563
ghi     789
jklmn   1011

```

The problem occurs usually when a word is already 8 or more characters long.

To help solve the spacing issue, you can use the `expandtabs()` method on a string to set how many characters a tab will use.

``` python
print("abcdef\t123".expandtabs(10))
print("cdefghij\t4563".expandtabs(10))
print("ghi\t789".expandtabs(10))
print("jklmn\t1011".expandtabs(10))
```

Now outputs

``` bash
abcdef    123
cdefghij  4563
ghi       789
jklmn     1011
```

