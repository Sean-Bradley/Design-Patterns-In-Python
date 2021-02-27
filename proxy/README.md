# Proxy Design Pattern

## Overview

The **Proxy** design pattern is a class functioning as an interface to another class or object.

A Proxy could be for anything, such as a network connection, an object in memory, a file, or anything else you need to provide an abstraction between.

Types of proxies, 

* **Virtual Proxy**: An object that can cache parts of the real object, and then complete loading the full object when necessary.

* **Remote Proxy**: Can relay messages to a real object that exists in a different address space.

* **Protection Proxy**: Apply an authentication layer in front of the real object.

* **Smart Reference**: An object which whose internal attributes can be overridden or replaced.

Additional functionality can be provided at the proxy abstraction if required. E.g., caching, authorization, validation, lazy initialization, logging.

The proxy should implement the subject interface as much as practicable so that the proxy and subject appear identical to the client.

The Proxy Pattern can also be called **Monkey Patching** or **Object Augmentation**

## Terminology

* **Proxy**: An object with an interface identical to the real subject. Can act as a placeholder until the real subject is loaded or as gatekeeper applying extra functionality.
* **Subject Interface**: An interface implemented by both the Proxy and Real Subject. 
* **Real Subject**: The actual real object that the proxy is representing.
* **Client**: The client application that uses and creates the Proxy.

## Proxy UML Diagram

![Proxy Pattern UML Diagram](/img/proxy_concept.svg)

## Output

``` bash
python ./proxy/proxy_concept.py
1848118706080
pulling data from RealSubject
[1, 2, 3]
pulling data from Proxy cache
[1, 2, 3]
```

## Example Use Case

In this example, I dynamically change the class of an object. So, I am essentially using an object as a proxy to other classes.

Every time the `tell_me_the_future()` method is called; it will randomly change the object to use a different class.

The object `PROTEUS` will then use the same static attributes and class methods of the new class instead.

## Example UML Diagram

![Proxy Use Case Example](/img/proxy_example.svg)

## Output

``` bash
python ./proxy/client.py
I am the form of a Lion
I am the form of a Leopard
I am the form of a Serpent
I am the form of a Leopard
I am the form of a Lion
```

## New Coding Concepts

### Changing An Objects Class At Runtime.

You change the class of an object by running `self.__class__ = SomeOtherClass`

Note that doing this does not affect any variables created during initialisation, eg `self.variable_name = 'abc'`, since the object itself hasn't changed. Only its class methods and static attributes have been replaced with the class methods and static attributes of the other class. 

This explains how calling `tell_me_the_future()` and `tell_me_your_form()` produced different results after changing `self.__class__`

### Avoiding Circular Imports.

Normally in all the examples so far, I have been importing using the form

``` python
from module import Class
```

In [/proxy/client.py](/proxy/client.py) I import the `Lion` module. The `Lion` module itself imports the `Leopard` and `Serpent` modules, which in turn also re import the `Lion` module again. This is a circular import and occurs in some situations when you separate your modules into individual files.

Circular imports will prevent the python interpreter from compiling your `.py` file into byte code.

The error will appear like, 

```
cannot import name 'Lion' from partially initialized module 'lion' (most likely due to a circular import)
```

To avoid circular import errors, you can import modules using the form.

``` python
import module
```

and when the import is actually needed in some method

``` python
OBJECT = module.ClassName
```

See the [Lion](/proxy/lion.py), [Serpent](/proxy/serpent.py) and [Leopard](/proxy/leopard.py) classes for examples.

## Summary

* Proxy forwards requests onto the Real Subject when applicable, depending on the kind of proxy.
* A virtual proxy can cache elements of a real subject before loading the full object into memory.
* A protection proxy can provide an authentication layer. For example, an NGINX proxy can add Basic Authentication restriction to a HTTP request.
* A proxy can perform multiple tasks if necessary.
* A proxy is different than an [Adapter](/adapter). The Adapter will try to adapt two existing interfaces together. The Proxy will use the same interface as the subject. 
* It is also very similar to the [Facade](/facade), except you can add extra responsibilities, just like the [Decorator](/decorator). The Decorator however can be used recursively.
* The intent of the Proxy is to provide a stand in for when it is inconvenient to access a real subject directly.
* The Proxy design pattern may also be called the Surrogate design pattern.