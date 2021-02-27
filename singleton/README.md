# Singleton Design Pattern

## Overview

Sometimes you need an object in an application where there is only one instance. A constant or static variable for example.

You don't want there to be many versions, for example, you have a game with a score and you want to adjust it. You may have accidentally created several instances of the class holding the score object. Or, you may be opening a database connection, there is no need to create many, when you can use the existing one that is already in memory. You may want a logging component, and you want to ensure all classes use the same instance. So, every class could declare their own logger component, but behind the scenes, they all point to the same memory address (id).

By creating a class using the **Singleton** pattern, you can enforce that even if a second instance was created, it will still refer to the original.

The Singleton can be accessible globally, but it is not a global variable. It is a class that can be instanced at any time, but after it is first instanced, any new instances will point to the same instance as the first.

## Singleton UML Diagram

![Singleton UML Diagram](/img/singleton_concept.svg)

## Output

``` bash
python ./singleton/singleton_concept.py
id(Singleton)   = 2757349313120
id(Singleton()) = 2757349313120
id(OBJECT1)     = 2757349313120
id(OBJECT2)     = 2757349313120
id(Singleton.class_method())    = 140731233742040
id(Singleton().class_method())  = 140731233742040
id(OBJECT1.class_method())      = 140731233742040
id(OBJECT2.class_method())      = 140731233742040
```

!!! Notes

    Variables declared at class level are static variables that can be accessed directly using the class name without the class needing to be instantiated first.

    **cls** is a reference to the class

    **\__new\__** gets called before **\__init\__**,

    **\__new\__** has access to class level variables

    **\__init\__** references self which is created when the class is instantiated

    By using **\__new\__**, instead of **\__init\__**, we can use the singleton without instantiating it. It is enough to just import it or create the class definition inline to begin using the singleton.

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

In the file [singleton/leaderboard.py](singleton/leaderboard.py),

``` python linenums="4"

    "The Leaderboard as a Singleton"
    _instance = None
    _table = {}

``` 

The `{}` is indicating a Python **Dictionary**.

A Dictionary can be instantiated using the curly braces `{}` or `dict()`

The Dictionary is similar to a [List](builder#python-list), except that the items are `key:value` pairs.

The Dictionary can store multiple `key:value` pairs, they can be changed, can be added and removed, can be re-ordered, can be pre-filled with `key:value` pairs when instantiated and is very flexible.

Since Python 3.7, dictionaries are ordered in the same way that they are created and the keys are unique.

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

* To be a Singleton, there must only be one instance of the Singleton, no matter how many times, or in which class it was instantiated.
* You want the attributes or methods to be globally accessible across your application, so that other classes may be able to use the Singleton.
* You can extend classes with a Singleton method, as I did with the leaderboard, but it still points to the same Singleton memory location regardless.
* You want controlled access to a sole instance.
