# Mediator Design Pattern

## Videos

Section | Video Links
-|-
Mediator Overview |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16511990/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Mediator Overview"><img src="/img/udemy_btn_sm.gif" alt="Mediator Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/9bcLUtBoO04" target="_blank" title="Mediator Overview"><img src="/img/yt_btn_sm.gif" alt="Mediator Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Mediator Overview"><img src="/img/skillshare_btn_sm.gif" alt="Mediator Overview"/></a>
Mediator Use Case |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25615950/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Mediator Use Case"><img src="/img/udemy_btn_sm.gif" alt="Mediator Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/IIOkn92bVqA" target="_blank" title="Mediator Use Case"><img src="/img/yt_btn_sm.gif" alt="Mediator Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Mediator Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Mediator Use Case"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

Objects communicate through the **Mediator** rather than directly with each other.

As a system evolves and becomes larger and supports more complex functionality and business rules, the problem of communicating between these components becomes more complicated to understand and manage. It may be beneficial to refactor your system to centralize some or all of its functionality via some kind of mediation process.

The mediator pattern is similar to creating a [Facade](/facade) pattern between your classes and processes. Except the Mediator is expected to transact data both ways between two or more other classes or processes that would normally interact directly with each other.

The resulting Mediator interface will be very custom to the use cases that it is now supporting.

The Mediator will generally look like an object that is managing one of more [Observer](/observer) patterns perhaps between the other classes or processes (colleagues). Whether you use an Observer pattern to manage a particular piece of functionality or not depends on whether it is the best use of the resources you have available.

When refactoring your code, you may decide to approach your refactoring from the perspective of implementing an Observer pattern first. This means that all colleagues (Observers) will receive the notification whether it was intended for them or not. If you want to avoid redundant updates in the colleagues then you can write specific cases in your code, or create specific methods as I have done in [/mediator/mediator_concept.py](/mediator/mediator_concept.py) file.

Colleagues now will send and receive requests via a Mediator object rather than directly between each other. The Mediator is like a router in this case, but allows you to add extra programmatic functionality and also give the option of creating other kinds of colleagues that could utilize the communications in new ways.

## Terminology

* **Mediator Interface**: An interface that the Mediator and Colleagues implement. Note that different Colleagues will have varied use cases and won't need to implement all the methods described in the Mediator interface.
* **Concrete Mediator**: The single source of truth and coordinator of communications between the components (colleagues).
* **Colleague Classes**: One of the many types of concrete components that use the mediator for its own particular use case. 

## Mediator UML Diagram

![Mediator Pattern UML Diagram](/img/mediator_concept.svg)

## Source Code

In the example concept, there are two colleague classes that use each other's methods. Instead of the Colleagues calling each other's methods directly, they implement the Mediator interface and call each other via the Mediator. Each colleague class or process is designed for a different purpose, but they utilize some related functionality from each other.

The system would work without the Mediator, but adding the Mediator will allow extending functionality to a potential third colleague that provides a different service, such as AI analysis or monitoring, without needing to add specific support or knowledge into the two original colleagues.

## Output

``` bash
python ./mediator/mediator_concept.py    
COLLEAGUE1 <--> Here is the Colleague2 specific data you asked for
COLLEAGUE2 <--> Here is the Colleague1 specific data you asked for
```

## Example Use Case

This is a simplified game engine. There is the main game engine component, a scheduler that manages game events and there are game clients that act as separate game players submitting bets into a game round.

All of the components implement the Mediators interface. They all implement one or some of the methods differently depending on their purpose. While they all perform different types of functionality, they all require a single source of truth being the Game Engine that acts as the Mediator.

There is mixture of this Mediator example using the [Observer](/observer) pattern to notify the game clients, as well as specific methods not necessarily shared between the scheduler, game engine and clients but benefits from being managed via the Mediator.

Normally the processes being mediated will be running from different servers or programs, but in this example they are all part of the same client in order to demonstrate the concept easier.

## Example UML Diagram

![Mediator Pattern UML Diagram](/img/mediator_example.svg)

## Output

``` bash
python.exe ./mediator/client.py
Sean -> New Game, Place Bets
Cosmo -> New Game, Place Bets
Emmy -> New Game, Place Bets
Emmy -> You Are The Winner with result `10`. You Won 12. Your balance = 310
```

## New Coding Concepts

### The Underscore Only `_` Variable

In the `Player` class, there is a for loop that iterates the bets list.

``` python
for _ in bets:
    self.balance -= 1
```

The `_` is used instead of a more tradition `i`, `x`, `y` or another variable. If using a letter in the for loop, and not actually using it, like in the above example, then Pylint would indicate a warning of unused variable. Note that the Python interpreter would still run this code ok if using a letter as the variable name, but reducing Pylint warnings helps makes code look neater.

E.g., 

``` python
for i in bets:
    self.balance -= 1
```

The Pylint warning would be

``` bash
W0612: Unused variable 'i' (unused-variable)
```

So, using the `_` prevents this warning.
