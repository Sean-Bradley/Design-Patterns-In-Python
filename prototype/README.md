# Prototype Design Pattern

Prototype design pattern is good for when creating a new objects may require more resources than you want to use or have available, versus just making a new copy in memory.
Eg, A file you've downloaded from a server may be large, but since it is already in memory, you could just clone it, and work on the new copy independently of the original.

In the prototype patterns interface, you create a static clone method that should be implemented by all classes that use the interface.
How the clone method is implemented in the concrete class is up to you.
You will need to decide whether a shallow or deep copy is required.

* A shallow copy, copies and creates new references 1 level deep,
* A deep copy, copies and creates new references for all levels.

In Python you have mutable objects such as Lists, Dictionaries, Sets and any custom Objects you have created. A shallow copy, will create new copies of the objects with new references in memory, but the underlying data will point to the same location as the original copy. Be sure to test your implementation that
the copy method you use works as you expect. 

![Prototype UML Diagram](prototype.png)

## Video Tutorial

[![Prototype Design Pattern In Python](https://img.youtube.com/vi/_jBjhI6-VDI/0.jpg)](https://youtu.be/_jBjhI6-VDI)
