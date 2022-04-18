# Memento Design Pattern

## Videos

Section | Video Links
-|-
Memento Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25632774/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Memento Overview"><img src="/img/udemy_btn_sm.gif" alt="Memento Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/gQnKnmSu8xA&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Memento Overview"><img src="/img/yt_btn_sm.gif" alt="Memento Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Memento Overview"><img src="/img/skillshare_btn_sm.gif" alt="Memento Overview"/></a>
Memento Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25632770/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Memento Use Case"><img src="/img/udemy_btn_sm.gif" alt="Memento Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/DFEvyjiUA_A&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Memento Use Case"><img src="/img/yt_btn_sm.gif" alt="Memento Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Memento Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Memento Use Case"/></a>
Getters/Setters | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25632784/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Getters/Setters"><img src="/img/udemy_btn_sm.gif" alt="Getters/Setters"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/6ijrepx6jgM&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Getters/Setters"><img src="/img/yt_btn_sm.gif" alt="Getters/Setters"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Getters/Setters"><img src="/img/skillshare_btn_sm.gif" alt="Getters/Setters"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>

## Overview

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Terminology

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Memento UML Diagram

![Memento UML Diagram](/img/memento_concept.svg)

## Source Code

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

### Output

``` bash
python ./memento/memento_concept.py
Originator: Setting state to `State #1`
Originator: Setting state to `State #2`
CareTaker: Getting a copy of Originators current state
Originator: Providing Memento of state to caretaker.
Originator: Setting state to `State #3`
CareTaker: Getting a copy of Originators current state
Originator: Providing Memento of state to caretaker.
Originator: Setting state to `State #4`
State #4
CareTaker: Restoring Originators state from Memento
Originator: State after restoring from Memento: `State #2`
State #2
CareTaker: Restoring Originators state from Memento
Originator: State after restoring from Memento: `State #3`
State #3
```

## Example Use Case

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Example UML Diagram

![Memento Use Case UML Diagram](/img/memento_example.svg)

## Output

``` bash
python ./memento/client.py
Score: 200, Level: 0, Location: {'x': 0, 'y': 0, 'z': 2}
Inventory: {'rifle', 'sword'}

CareTaker: Game Save
Score: 500, Level: 1, Location: {'x': 0, 'y': 0, 'z': 13}
Inventory: {'motorbike', 'rifle', 'sword'}

CareTaker: Game Save
Score: 600, Level: 2, Location: {'x': 0, 'y': 0, 'z': 14}
Inventory: {'motorbike', 'rifle', 'sword'}

CareTaker: Restoring Characters attributes from Memento
Score: 200, Level: 0, Location: {'x': 0, 'y': 0, 'z': 2}
Inventory: {'rifle', 'sword'}
```

## New Coding Concepts

### Python Getter/Setters

Often when coding attributes in classes, you may want to provide methods to allow external functions to read or modify a classes internal attributes.

A common approach would be to add two methods prefixed with `get_` and `set_`, 

``` python
class ExampleClass:
    def __init__(self):
        self._value = 123
    
    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

example = ExampleClass()
print(example.get_value())
```

This makes perfect sense what the intentions are, but there is a more pythonic way of doing this and that is by using the inbuilt Python `@property` decorator.

``` python
class ExampleClass:
    def __init__(self):
        self._value = 123

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

example = ExampleClass()
print(example.value)
```

Note that in the above example, there is an extra decorator named `@value.setter` . This is used for setting the `_value` attribute.

Along with the above two new getter/setter methods, there is also another method for deleting an attribute called `deleter` .

``` python
class ExampleClass:
    def __init__(self):
        self._value = 123

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.deleter
    def value(self):
        print('Deleting _value')
        del self._value

example = ExampleClass()
print(example.value)
del example.value
print(example.value) # now raises an AttributeError
```

## Summary

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._