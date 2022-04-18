# Factory Design Pattern

## Videos

Section | Video Links
-|-
Factory Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16396650/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Factory Overview"><img src="/img/udemy_btn_sm.gif" alt="Factory Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/cfN1_e_Fyjw&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Factory Overview"><img src="/img/yt_btn_sm.gif" alt="Factory Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Factory Overview"><img src="/img/skillshare_btn_sm.gif" alt="Factory Overview"/></a>
Factory Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362098/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Factory Use Case"><img src="/img/udemy_btn_sm.gif" alt="Factory Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/ywTF3yTAe3M&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Factory Use Case"><img src="/img/yt_btn_sm.gif" alt="Factory Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Factory Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Factory Use Case"/></a>
**ABCMeta** Module | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362152/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="ABCMeta Module"><img src="/img/udemy_btn_sm.gif" alt="ABCMeta Module"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/8HMurBw18wU&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="ABCMeta Module"><img src="/img/yt_btn_sm.gif" alt="ABCMeta Module"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="ABCMeta Module"><img src="/img/skillshare_btn_sm.gif" alt="ABCMeta Module"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>

## Overview

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Terminology

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Factory UML Diagram

![Factory Pattern Overview](/img/factory_concept.svg)

## Source Code

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Output

``` bash
python ./factory/factory_concept.py 
ConcreteProductB
```

## Example Use Case

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Factory Example UML Diagram

![Chair Factory](/img/factory_example.svg)

## Output

``` bash
python ./factory/client.py
{'width': 40, 'depth': 40, 'height': 40}

```

## New Coding Concepts

### ABCMeta

ABCMeta classes are a development tool that help you to write classes that conform to a specified interface that you've designed.

ABCMeta refers to **A**bstract **B**ase **C**lasses. 

The benefits of using ABCMeta classes to create abstract classes is that your IDE and Pylint will indicate to you at development time whether your inheriting classes conform to the class definition that you've asked them to.

Abstract classes are not instantiated directly in your scripts, but instead inherited by subclasses that will provide the implementation code for the abstract methods. E.g., you don't create `IChair`, but you create `SmallChair` that implemented the methods described in the `IChair` interface.

An abstract method is a method that is declared, but contains no implementation. The implementation happens at the class that inherits the abstract class.

You don't need to use ABCMeta classes and interfaces that you have created in your final python code. You code will still work without them. 

You can try it by removing the interfaces from all of the chair classes above, and you will see that your python program will still run.

eg, change

``` python
class BigChair(IChair):
```

to 

``` python
class BigChair():
```

and it will still work.

While it is possible to ensure your classes are correct without using abstract classes, it is often easier to use abstract classes as a backup method of checking correctness, especially if your projects become very large and involve many developers.

Note that in all my code examples, the abstract classes are prefixed with a capital **I**, to indicate that they are abstract interfaces. They have no code in their methods. They do not require a `self` or `cls` argument due to the use of `@staticmethod` . The inheriting class will implement the code in each of the methods that the abstract class is describing. If subclasses are inheriting an abstract base class, and they do not implement the methods as described, there will be [Pylint error or warning message (E0110)](/coding-conventions.md#common-pylint-warning-and-error-messages).

See PEP 3119 : [https://www.python.org/dev/peps/pep-3119/](https://www.python.org/dev/peps/pep-3119/)

## Summary

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._