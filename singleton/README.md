# Singleton Design Pattern

## Videos

Section | Video Links
-|-
Singleton Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362178/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Singleton Overview"><img src="/img/udemy_btn_sm.gif" alt="Singleton Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/wc1b70LueGA" target="_blank" title="Singleton Overview"><img src="/img/yt_btn_sm.gif" alt="Singleton Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Singleton Overview"><img src="/img/skillshare_btn_sm.gif" alt="Singleton Overview"/></a>
Singleton Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362182/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Singleton Use Case"><img src="/img/udemy_btn_sm.gif" alt="Singleton Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/-F7OYXMpVJw" target="_blank" title="Singleton Use Case"><img src="/img/yt_btn_sm.gif" alt="Singleton Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Singleton Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Singleton Use Case"/></a>
Python **Dictionary** | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362192/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Python Dictionary"><img src="/img/udemy_btn_sm.gif" alt="Python Dictionary"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/L7IPuo6VOjo" target="_blank" title="Python Dictionary"><img src="/img/yt_btn_sm.gif" alt="Python Dictionary"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Python Dictionary"><img src="/img/skillshare_btn_sm.gif" alt="Python Dictionary"/></a>

## Book 

Cover | Links |
-|-|
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>|

## Overview

Sometimes you need an object in an application where there is only one instance.

You don't want there to be many versions, for example, you have a game with a score and you want to adjust it. You may have accidentally created several instances of the class holding the score object. Or, you may be opening a database connection, there is no need to create many, when you can use the existing one that is already in memory. You may want a logging component, and you want to ensure all classes use the same instance. So, every class could declare their own logger component, but behind the scenes, they all point to the same memory address (id).

By creating a class using the **Singleton** pattern, you can enforce that even if a second instance was created, it will still refer to the original.

The Singleton can be accessible globally, but it is not a global variable. It is a class that can be instanced at any time, but after it is first instanced, any new instances will point to the same instance as the first.

For a class to behave as a Singleton, it should not contain any references to `self` but use static variables, static methods and/or class methods.

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

Variables declared at class level are static variables that can be accessed directly using the class name without the class needing to be instantiated first.

**cls** is a reference to the class

**self** is a reference to the instance of the class

**\__new\__** gets called before **\__init\__**

**\__new\__** has access to class level variables

**\__init\__** references self which is created when the class is instantiated

By using **\__new\__**, and returning a reference to **cls**, we can force the class to act as a singleton. For a class to act as a singleton, it should not contain any references to **self**.

## Example Use Case

In the example, there are three games created. They are all independent instances created from their own class, but they all share the same leaderboard. The leaderboard is a singleton.

It doesn't matter how the Games where created, or how they reference the leaderboard, it is always a singleton.

Each game independently adds a winner, and all games can read the altered leaderboard regardless of which game updated it.

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
