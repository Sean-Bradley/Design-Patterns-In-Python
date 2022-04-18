# Iterator Design Pattern

## Videos

Section | Video Links
-|-
Iterator Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16510272/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Iterator Overview"><img src="/img/udemy_btn_sm.gif" alt="Iterator Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/TtszPXf3qjE&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Iterator Overview"><img src="/img/yt_btn_sm.gif" alt="Iterator Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Iterator Overview"><img src="/img/skillshare_btn_sm.gif" alt="Iterator Overview"/></a>
Iterator Use Case |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25598656/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Iterator Use Case"><img src="/img/udemy_btn_sm.gif" alt="Iterator Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/HvlAPUce_GU&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Iterator Use Case"><img src="/img/yt_btn_sm.gif" alt="Iterator Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Iterator Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Iterator Use Case"/></a>
Python iter() Function |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25598664/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Python iter() Function"><img src="/img/udemy_btn_sm.gif" alt="Python iter() Function"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/__sZY-XBt-A&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Python iter() Function"><img src="/img/yt_btn_sm.gif" alt="Python iter() Function"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Python iter() Function"><img src="/img/skillshare_btn_sm.gif" alt="Python iter() Function"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>

## Overview

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Terminology

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Iterator UML Diagram

![Iterator Pattern Overview](/img/iterator_concept.svg)

## Source Code

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Output

``` bash
python ./iterator/iterator_concept.py
This method has been invoked
This method has been invoked
This method has been invoked
This method has been invoked
```

## Example Use Case

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

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

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._