# Command Design Pattern

## Overview

The **Command** pattern is a behavioral design pattern, in which an abstraction exists between an object that invokes a command, and the object that performs it.

E.g., a button will call the **Invoker**, that will call a pre-registered **Command**, that the **Receiver** will perform.

A Concrete Class will delegate a request to a command object, instead of implementing the request directly.

Using a command design pattern allows you to separate concerns and to solve problems of the concerns independently of each other.

E.g., logging the execution of a command and its outcome.

The command pattern is a good solution for implementing UNDO/REDO functionality into your application.

Uses:

* GUI Buttons, menus
* Macro recording
* Multi-level undo/redo
* Networking - send whole command objects across a network, even as a batch
* Parallel processing or thread pools
* Transactional behavior
* Wizards

## Terminology

* **Receiver**: The object that will receive and execute the command.
* **Invoker**: The object that sends the command to the receiver. E.g., A button.
* **Command Object**: Itself, an object, that implements an execute, or action method, and contains all required information to execute it.
* **Client**: The application or component that is aware of the Receiver, Invoker and Commands.

## Command Pattern UML Diagram

![The Command Pattern UML Diagram](/img/command_concept.svg)

## Source Code

The Client instantiates a Receiver that accepts certain commands.

The Client then creates two Command objects that will call one of the specific commands on the Receiver.

The Client then creates an Invoker, E.g., a user interface with buttons, and registers both Commands into the Invokers dictionary of commands.

The Client doesn't call the receivers commands directly, but the via the Invoker, which then calls the registered Command objects `execute()` method.

This abstraction between the invoker, command and receiver, allows the Invoker to add extra functionality such as history, replay, UNDO/REDO, logging, alerting and any other useful things that may be required.

## Output

``` bash
python ./command/command_concept.py
Executing Command 1
Executing Command 2
Executing Command 1
Executing Command 2
```

## Example Use Case

This will be a smart light switch. 

This light switch will keep a history of each time one of its commands was called. 

And it can replay its commands. 

A smart light switch could be extended in the future to be called remotely or automated depending on sensors.

## Example UML Diagram

![The Command Pattern UML Diagram](/img/command_example.svg)

## Output

``` bash
python ./command/client.py
Light turned ON
Light turned OFF
Light turned ON
Light turned OFF
11:23:35 : ON
11:23:35 : OFF
11:23:35 : ON
11:23:35 : OFF
Light turned ON
Light turned OFF
```

## New Coding Concepts

### _Single Leading Underscore

The single leading underscore **`_variable`**, on your class variables is a useful indicator to other developers that this property should be considered private.

Private, in C style languages, means that the variable/field/property is hidden and cannot be accessed outside of the class. It can only be used internally by its own class methods.

Python does not have a public/private accessor concept so the variable is not actually private and can still be used outside of the class in other modules. 

It is just a useful construct that you will see developers use as a recommendation not to reference this variable directly outside of this class, but use a dedicated method or property instead.

## Summary

* State should not be managed in the Command object itself.
* There can be one or more Invokers which can execute the Command at a later time.
* The Command object is especially useful if you want to UNDO/REDO commands at later time.
* The Command pattern is similar to the [Memento](/memento) pattern in the way that it can also be used for UNDO/REDO purposes. However, the Memento pattern is about recording and replacing the state of an object, whereas the Command pattern executes a predefined command. E.g., Draw, Turn, Resize, Save, etc. 
