# Template Method Design Pattern

## Videos

Section | Video Links
-|-
Template Method Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25682448/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Template Method Overview"><img src="/img/udemy_btn_sm.gif" alt="Template Method Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/bZWvQbmUHy8&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Template Method Overview"><img src="/img/yt_btn_sm.gif" alt="Template Method Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Template Method Overview"><img src="/img/skillshare_btn_sm.gif" alt="Template Method Overview"/></a>
Template Method Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25682452/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Template Method Use Case"><img src="/img/udemy_btn_sm.gif" alt="Template Method Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/iGLpIEXPGzg&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Template Method Use Case"><img src="/img/yt_btn_sm.gif" alt="Template Method Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Template Method Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Template Method Use Case"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

In the **Template Method** pattern, you create an abstract class (template) that contains a **Template Method** which is a series of instructions which are a combination of abstract and hook methods.

Abstract methods need to be overridden in the subclasses that extend the abstract (template) class.

Hook methods normally have empty bodies in the abstract class. Subclasses can optionally override the hook methods to create custom implementations.

So, what you have, is an abstract class, with several types of methods, being the main template method, and a combination of abstract and/or hooks, that can be extended by different subclasses which all have the option of customizing the behavior of the template class without changing its underlying algorithm structure.

Template methods are useful to help you factor out common behavior within your library classes.

Note that this pattern describes the behavior of a **method** and how its inner method calls behave.

Hooks are default behavior and can be overridden. They are normally empty by default.

Abstract methods, must be overridden in the concrete class that extends the template class.

## Terminology

* **Abstract Class**: Defines the template method and the primitive steps as abstract and/or hook methods.
* **Concrete Class**: A subclass that extends some or all of the abstract class primitive methods.

## Template Method UML Diagram

![Template Method UML Diagram](/img/template_concept.svg)

## Source Code

Note that in both the concrete classes in this concept example, the `template_method()` was not overridden since it was already inherited. Only the primitives (abstract or hooks) were optionally overridden.

To create an empty abstract method in your abstract class, that must be overridden in a subclass, then use the ABCMeta `@abstractmethod` decorator.

## Output 

``` bash
python ./template/template_concept.py
Class_A : Step Two (overridden)
Step Three is a hook that prints this line by default.
Class_B : Step One (overridden)
Class_B : Step Two. (overridden)
Class_B : Step Three. (overridden)
```

## Template Method Example Use Case

In the example use case, there is an `AbstractDocument` with several methods, some are optional and others must be overridden. 

The document will be written out in two different formats.

Depending on the concrete class used, the `text()` method will wrap new lines with `<p>` tags and the `print()` method will format text with tabs, or include html tags.

## Template Method Use Case UML Diagram

![Template Method Use Case UML Diagram](/img/template_example.svg)

## Output

``` bash
python ./template/client.py
----------------------
title   : New Text Document
background_colour       : white
text    : Some Text
footer  : -- Page 1 --

<html>
  <head>
    <title>New HTML Document</title>
    <style>
      body {
        background-color: white;
      }
    </style>
  </head>
  <body>
    <p>Line 1</p>
    <p>Line 2</p>
  </body>
</html>
```

## Summary

*...Refer to Book or Videos for extra content.*