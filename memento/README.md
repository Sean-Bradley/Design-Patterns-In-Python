# Memento Design Pattern

## Overview

Throughout the lifecycle of an application, an objects state may change. You might want to store a copy of the current state in case of later retrieval. E.g., when writing a document, you may want to auto save the current state every 10 minutes. Or you have a game, and you want to save the current position of your player in the level, with its score and current inventory.

You can use the **Memento** pattern for saving a copy of state and for later retrieval if necessary. 

The Memento pattern, like the Command pattern, is also commonly used for implementing UNDO/REDO functionality within your application.

The difference between the [Command](/command) and the Memento patterns for UNDO/REDO, is that in the Command pattern, you re-execute commands in the same order that changed attributes of a state, and with the Memento, you completely replace the state by retrieving from a cache/store.

## Terminology

* **Originator**: The originator is an object with an internal state that changes on occasion.
* **Caretaker**: (Guardian) A Class that asks the Originator to create or restore Mementos. The Caretaker than saves them into a cache or store of mementos. 
* **Memento**: A copy of the internal state of the Originator that can later be restored back into the Originator to replace its current state. 

## Memento UML Diagram

![Memento UML Diagram](/img/memento_concept.svg)

## Source Code

In the concept code, the client creates an object whose state will be periodically recorded. The object will be the Originator.

A Caretaker is also created with a reference to the Originator.

The Originators internal state is changed several times. It is then decided that the Caretaker should make a backup.

More changes are made to the Originator, and then another backup is made.

More changes are made to the Originator, and then it is decided that the first backup should be restored instead.

And then the second backup is restored.

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

There is a game, and the character is progressing through the levels. It has acquired several new items in its inventory, the score is very good and you want to save your progress and continue later. 

You then decide you made a mistake and need to go back to a previous save because you took a wrong turn.

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

* You don't need to create a new Memento each time an Originators state changes. You can do it only when considered necessary. E.g., an occasional backup to a file.

* Mementos can be stored in memory or saved/cached externally. The Caretaker will abstract the complications of storing and retrieving Mementos from the Originator.

* Consider the [Command](/command) pattern for fine grained changes to an objects state to manage UNDO/REDO between memento saves. Or even save command history into a Memento that can be later replayed.

* In my examples, the whole state is recorded and changed with the Memento. You can use the Memento to record and change partial states instead if required. 

* When copying state, be aware of shallow/deep copying. In complicated projects, your restore functionality will probably contain a combination of both the [Command](/command) and Memento patterns.
