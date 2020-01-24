# Memento Design Pattern

The Memento pattern is a behavioral design pattern that allows you to take a snapshot of an object's state and restore it back at a later time. It is a very common pattern to use whn implementing undo/redo functionality within your application.

There 3 main objects
Originator - (Creator) The originator is some object that has an internal state
Caretaker - (Guardian) The caretaker is going to do something to the originator, but wants to be able to undo the change
Memento - the copy of the state before the caretaker changed it

the Caretaker class refers to the Originator class for saving (createMemento()) and restoring (restore(memento)) originator's internal state. 
The Originator class implements 
(1) createMemento() by creating and returning a Memento object that stores originator's current internal state and 
(2) restore(memento) by restoring state from the passed in Memento object. 



If you are undoing/redoing by executing commands on the state, that is the command pattern. 
If you are undoing/redoing by replacing state from a cache of states, that is the memento.

The Client, tells the Origianetor(Object) to create a memento (copy) of itself into the mememto.
The Client then tells the Guardian, to store a copy of the memonto.
