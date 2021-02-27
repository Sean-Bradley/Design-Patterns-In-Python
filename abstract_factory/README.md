# Abstract Factory Design Pattern

## Overview

The Abstract Factory Pattern adds an abstraction layer over multiple other creational pattern implementations.

To begin with, in simple terms, think if it as a Factory that can return Factories. Although you will find examples of it also begin used to return Builder, ProtoTypes, Singletons or other design pattern implementations.

## Terminology

* **Client**: The client application that calls the **Abstract Factory** and **Abstract Product** classes. It's the same process as the concrete creator in the [Factory](factory.md#terminology) design pattern.

* **Abstract Factory**: An interface to one of the Factories.

* **Concrete Factory**: The Factory returned via the interface and contains methods or attributes to allow creating the product.

* **Abstract Product**: The interface for the product within its own Factory.

* **Concrete Product**: The object finally returned.

## Abstract Factory UML Diagram

![Abstract Factory Overview](img/abstract_factory_concept.svg)

## Output

``` bash
python ./abstract_factory/abstract_factory_concept.py
<class 'factory_a.ConcreteProductB'>
<class 'factory_b.ConcreteProductC'>
```

## Abstract Factory Example Use Case

An example use case may be that you have a furniture shop front. You sell many different kinds of furniture. You sell chairs and tables. And they are manufactured at different factories using different unrelated processes that are not important for your concern. You only need the factory to deliver.

You can create an extra module called `FurnitureFactory`, to handle the chair and table factories, thus removing the implementation details from the client.

## Abstract Factory Example UML Diagram

See this UML diagram of an Abstract Furniture Factory implementation that returns chairs and tables.

![Abstract Furniture Factory](img/abstract_furniture_factory.svg)

## Output

``` bash
python ./abstract_factory/client.py
<class 'small_chair.SmallChair'> : {'width': 40, 'depth': 40, 'height': 40}
<class 'medium_table.MediumTable'> : {'width': 110, 'depth': 70, 'height': 60}
```

## New Coding Concepts

### Exception Handling

Your Python code may produce errors. It happens to everybody. It is hard to foresee all possible errors, but you can try to handle them in case anyway.

Use the `Try`, `Except` and optional `finally` keywords to manage error handling.

In the example code, if no chair or table is returned, an `Exception` error is raised and it includes a text string that can be read and written to the console.

Within your code you can use the `raise` keyword to trigger Python built in exceptions or even create your own.

``` python
def get_furniture(furniture):
    "Static get_factory method"
    try:
        if furniture in ['SmallChair', 'MediumChair', 'BigChair']:
            return ChairFactory().get_chair(furniture)
        if furniture in ['SmallTable', 'MediumTable', 'BigTable']:
            return TableFactory().get_table(furniture)
        raise Exception('No Factory Found')
    except Exception as _e:
        print(_e)
    return None
```

If `WoodenTable` is requested from the factory, it will print `No Factory Found`

You don't need to always raise an exception to make one happen. In that case you can handle the possibility of any type of error using just `try` and `except`, with the optional `finally` if you need it.

``` python
try:
  print(my_var)
except:
  print("An unknown error Occurred")
finally:
  print("This is optional and will get called even if there is no error")
```

The above code produces the message `An Error Occurred` because `my_var` is not defined. 

The `try/except` allows the program to continue running, as can be verified by the line printed in the `finally` statement. So, this has given you the opportunity to manage any unforeseen errors any way you wish.

Alternatively, if your code didn't include the `try/except` and optional `finally` statements, the Python interpreter would return the error `NameError: name 'my_var' is not defined` and the program will crash at that line.

Also note how the default Python inbuilt error starts with `NameError` . You can handle this specific error explicitly using an extra `except` keyword.

``` python
try:
    print(my_var)
except NameError:
    print("There was a `NameError`")
except:
    print("An unknown error Occurred")
finally:
    print("This is optional and will get called even if there is no error")

```

You can add exception handling for as many types of errors as you wish.

Python Errors and Exceptions : [https://docs.python.org/3/tutorial/errors.html](https://docs.python.org/3/tutorial/errors.html)

## Summary

* Use when you want to provide a library of relatively similar products from multiple different factories.
* You want the system to be independent of how the products are created.
* It fulfills all of the same use cases as the Factory method, but is a factory for creational pattern type methods.
* The client implements the abstract factory interface, rather than all the internal logic and Factories. This allows the possibility of creating a library that can be imported for using the Abstract Factory.
* The Abstract Factory defers the creation of the final products/objects to its concrete factory subclasses. 
* You want to enforce consistent interfaces across products.
* You want the possibility to exchange product families.
