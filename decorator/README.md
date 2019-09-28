In object-oriented programming, the decorator pattern is a design pattern that allows behavior to be added to an individual object, at run time.

This is different than the Python language feature of Python Decorators in it's syntax, but the the application of it is the same in tha way it acts as a wrapper.

Decorator is a design pattern that achieves high levels of extensibility, without modifying the original function. It provides us a way to enhance our functions dinamically, by composition.

The decorator pattern is used in both the Object Oriented and Functional paradigms.

It's very similar to the chain of responsibility pattern, except with a decorator, you always do some work, whereas with chain of responsibility, you might do some work depending on conditions, and you can either retunr the orignal obejct, or the extended object.

The decorator pattern is structural, and the chain of responsibility is behavioural.

decorator pattern is structural and its intents are 
* Attach additional responsibilities to an object dynamically 
* Provide a flexible alternative to subclassing for extending functionality 

An example of this is adding borders or scroll bars to a text view 


For chain of responsibility pattern is behavioral and its intents are: 
* Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request 
* Chain the receiving objects and pass the request along the chain until an object handles it 

An example of this is purchasing authorization (branch manager → regional director → vice president → president). Another is java exception handling. 