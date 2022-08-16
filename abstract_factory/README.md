# Abstract Factory Design Pattern

## Videos

Section | Video Links
-|-
Abstract Factory Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16396782/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Abstract Factory Overview"><img src="/img/udemy_btn_sm.gif" alt="Abstract Factory Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/eXNLpSQjCzU&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Abstract Factory Overview"><img src="/img/yt_btn_sm.gif" alt="Abstract Factory Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Abstract Factory Overview"><img src="/img/skillshare_btn_sm.gif" alt="Abstract Factory Overview"/></a>
Abstract Factory Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362118/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Abstract Factory Use Case"><img src="/img/udemy_btn_sm.gif" alt="Abstract Factory Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/H18COAHTdVs&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Abstract Factory Use Case"><img src="/img/yt_btn_sm.gif" alt="Abstract Factory Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Abstract Factory Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Abstract Factory Use Case"/></a>
Exception Handling | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362160/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Exception Handling"><img src="/img/udemy_btn_sm.gif" alt="Exception Handling"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/jOxJSA3sxcQ&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Exception Handling"><img src="/img/yt_btn_sm.gif" alt="Exception Handling"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Exception Handling"><img src="/img/skillshare_btn_sm.gif" alt="Exception Handling"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>

## Overview

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Terminology

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Abstract Factory UML Diagram

![Abstract Factory Overview](/img/abstract_factory_concept.svg)

## Output

``` bash
python ./abstract_factory/abstract_factory_concept.py
<class 'factory_a.ConcreteProductB'>
<class 'factory_b.ConcreteProductC'>
```

## Abstract Factory Example Use Case

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Abstract Factory Example UML Diagram

See this UML diagram of an Abstract Furniture Factory implementation that returns chairs and tables.

![Abstract Furniture Factory](/img/abstract_furniture_factory.svg)

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

In the example code, if no chair or table is returned, an `Exception` error is raised, and it includes a text string that can be read and written to the console.

Within your code you can use the `raise` keyword to trigger Python built in exceptions or even create your own.

``` python
def get_furniture(furniture):
    "Static get_factory method"
    try:
        if furniture in ['SmallChair', 'MediumChair', 'BigChair']:
            return ChairFactory.get_chair(furniture)
        if furniture in ['SmallTable', 'MediumTable', 'BigTable']:
            return TableFactory.get_table(furniture)
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

Also note how the default Python inbuilt error starts with `NameError`. You can handle this specific error explicitly using an extra `except` keyword.

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

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._