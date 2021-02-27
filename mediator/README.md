# Mediator Design Pattern

## Overview

Objects communicate through the **Mediator** rather than directly with each other.

As a system evolves and becomes larger and supports more complex functionality and business rules, the problem of communicating between these components becomes more complicated to understand and manage. It may be beneficial to refactor your system to centralize some or all of its functionality via some kind of mediation process.

The mediator pattern is similar to creating a [Facade](facade) pattern between your classes and processes. Except the Mediator is expected to transact data both ways between two or more other classes or processes that would normally interact directly with each other.

The resulting Mediator interface will be very custom to the use cases that it is now supporting.

The Mediator will generally look like an object that is managing one of more [Observer](observer) patterns perhaps between the other classes or processes (colleagues). Whether you use an Observer pattern to manage a particular piece of functionality or not depends on whether it is the best use of the resources you have available.

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

This is a simplified game engine. There is the main game engine component, a scheduler which manages game events and there are game clients which act as separate game players submitting bets into a game round.

All of the components implement the Mediators interface. They all implement one or some of the methods differently depending on their purpose. While they all perform different types of functionality, they all require a single source of truth being the Game Engine which acts as the Mediator.

There is mixture of this Mediator example using the [Observer](observer) pattern to notify the game clients, as well as specific methods not necessarily shared between the scheduler, game engine and clients but benefits from being managed via the Mediator.

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

## Summary

* A mediator replaces a structure with many-to-many interactions between its classes and processes, with a one-to-many centralized structure where the interface supports all of the methods of the many-to-many structure, but via the mediator component instead.
* The mediator pattern encourages usage of shared objects that can now be centrally managed and synchronized.
* The mediator pattern creates an abstraction between two or more components which then makes a system easier to understand and manage.
* The mediator pattern is similar to the [Facade](facade) pattern, except the Mediator is expected to transact data both ways between two or more other classes or processes that would normally interact directly with each other.

