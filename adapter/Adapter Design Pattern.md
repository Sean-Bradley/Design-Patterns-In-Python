# Adapter Design Pattern

The adapter design pattern solves these problems:

- How can a class be reused that does not have an interface that a client requires?
- How can classes that have incompatible interfaces work together?
- How can an alternative interface be provided for a class?

In this lecture, I have 2 clasess, they don't share the same inteface. The client requires it's objects to use an already standardised interface.

So we need to create an adapter, that wraps the incompatible object, but implements the standardised interface.

## Two Incompatible Classes
![Adapter Design Pattern](adapter_before.png)

## After Creating an Adapter
![Adapter Design Pattern](adapter.png)
