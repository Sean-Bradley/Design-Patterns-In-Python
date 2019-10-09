# Iterator Design Pattern

An interafece with  next and has_next methods
next returns the next object in the aggregate(collection, list)
has_next retunrs a vaule indicating if at the end of teh collection or not.


An aggregate object such as a list should give you a way to access its elements without exposing its internal structure.

What problems can the Iterator design pattern solve?
The elements of an aggregate object should be accessed and traversed without exposing its representation (data structures).
New traversal operations should be defined for an aggregate object without changing its interface.

Defining access and traversal operations in the aggregate interface is inflexible because it commits the 
aggregate to particular access and traversal operations and makes it impossible to add new operations later without having to change the aggregate interface. 

What solution does the Iterator design pattern describe? 
Define a separate (iterator) object that encapsulates accessing and traversing an aggregate object.
Clients use an iterator to access and traverse an aggregate without knowing its representation (data structures).