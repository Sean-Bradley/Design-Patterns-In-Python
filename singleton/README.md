# Singleton Design Pattern

## Videos

Section | Video Links
-|-
Singleton Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362178/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Singleton Overview"><img src="/img/udemy_btn_sm.gif" alt="Singleton Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/wc1b70LueGA&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Singleton Overview"><img src="/img/yt_btn_sm.gif" alt="Singleton Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Singleton Overview"><img src="/img/skillshare_btn_sm.gif" alt="Singleton Overview"/></a>
Singleton Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362182/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Singleton Use Case"><img src="/img/udemy_btn_sm.gif" alt="Singleton Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/-F7OYXMpVJw&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Singleton Use Case"><img src="/img/yt_btn_sm.gif" alt="Singleton Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Singleton Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Singleton Use Case"/></a>
Python **Dictionary** | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362192/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Python Dictionary"><img src="/img/udemy_btn_sm.gif" alt="Python Dictionary"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/L7IPuo6VOjo&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Python Dictionary"><img src="/img/yt_btn_sm.gif" alt="Python Dictionary"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Python Dictionary"><img src="/img/skillshare_btn_sm.gif" alt="Python Dictionary"/></a>

## Book 

Cover | Links |
-|-|
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>|

## Overview

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Singleton UML Diagram

![Singleton UML Diagram](/img/singleton_concept.svg)

## Output

``` bash
python ./singleton/singleton_concept.py
id(Singleton)   = 2164775087968
id(OBJECT1)     = 2164775087968
id(OBJECT2)     = 2164775087968
id(OBJECT3)     = 2164775087968
```

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Example Use Case

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Example UML Diagram

![Singleton Use Case Diagram](/img/singleton_example.svg)

## Output

``` bash
python ./singleton/client.py
-----------Leaderboard-----------
|       1       |       Emmy    |
|       2       |       Cosmo   |
|       3       |       Sean    |

-----------Leaderboard-----------
|       1       |       Emmy    |
|       2       |       Cosmo   |
|       3       |       Sean    |

-----------Leaderboard-----------
|       1       |       Emmy    |
|       2       |       Cosmo   |
|       3       |       Sean    |
```

## New Coding Concepts

### Python Dictionary

In the file [/singleton/leaderboard.py](/singleton/leaderboard.py), 

``` python linenums="4"

    "The Leaderboard as a Singleton"
    _table = {}

``` 

The `{}` is indicating a Python **Dictionary**.

A Dictionary can be instantiated using the curly braces `{}` or `dict()`

The Dictionary is similar to a [List](/builder#python-list), except that the items are `key:value` pairs.

The Dictionary can store multiple `key:value` pairs, they can be changed, can be added and removed, can be re-ordered, can be pre-filled with `key:value` pairs when instantiated and is very flexible.

Since Python 3.7, dictionaries are ordered in the same way that they are created. 

The keys of the dictionary are unique.

You can refer to the dictionary items by key, which will return the value.

``` python
PS> python
>>> items = {"abc": 123, "def": 456, "ghi": 789}
>>> items["abc"] 
123
```

You can change the value at a key, 

``` python
PS> python
>>> items = {"abc": 123, "def": 456, "ghi": 789}
>>> items["def"] = 101112 
>>> items["def"]
101112
```

You can add new `key:value` pairs, and remove them by using the key.

``` python
PS> python
>>> items = {"abc": 123, "def": 456, "ghi": 789}
>>> items["jkl"] = 101112
>>> items["jkl"]
101112
>>> items.pop('def')
456
>>> items
{'abc': 123, 'ghi': 789, 'jkl': 101112}
```

You can order a dictionary alphabetically by key

``` python
PS> python
>>> items = {"abc": 123, "ghi": 789, "def": 456}
>>> items
{'abc': 123, 'ghi': 789, 'def': 456}
>>> dict(sorted(items.items()))
{'abc': 123, 'def': 456, 'ghi': 789}
```

## Summary

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._