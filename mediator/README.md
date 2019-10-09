# Mediator Design Pattern

In software engineering, the mediator pattern defines an object that encapsulates how a set of objects interact. This pattern is considered to be a behavioral pattern due to the way it can alter the program's running behavior.

With the mediator pattern, communication between objects is encapsulated within a mediator object. Objects no longer communicate directly with each other, but instead communicate through the mediator. This reduces the dependencies between communicating objects, thereby reducing coupling. 

The Mediator interface declares a method used by components to notify the
mediator about various events. The Mediator may react to these events and
pass the execution to other components.

The Base Component provides the basic functionality of storing a mediator's
instance inside component objects.

Concrete Components implement various functionality. They don't depend on other
components. They also don't depend on any concrete mediator classes.