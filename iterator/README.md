# Iterator Design Pattern

An interface with **next** and **has_next** methods.
**next** returns the next object in the aggregate(collection, list)
**has_next** returns a value, usually a boolean indicating if the iterable is at the end of the list or not.

The benefits of using the Iterator pattern is that the client, can traverse an aggregate without needing to understand it's internal representation
and data structures.
