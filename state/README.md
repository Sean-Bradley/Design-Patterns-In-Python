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
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>

## Overview

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Terminology

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## State UML Diagram

![State UML Diagram](/img/state_concept.svg)

## Source Code

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

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

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

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

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._