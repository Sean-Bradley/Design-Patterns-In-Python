# Prototype Design Pattern

## Videos

Section | Video Links
-|-
Prototype Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16396926/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Prototype Overview"><img src="/img/udemy_btn_sm.gif" alt="Prototype Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/2tFv9Rf2XGg&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Prototype Overview"><img src="/img/yt_btn_sm.gif" alt="Prototype Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Prototype Overview"><img src="/img/skillshare_btn_sm.gif" alt="Prototype Overview"/></a>
Prototype Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362134/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Prototype Use Case"><img src="/img/udemy_btn_sm.gif" alt="Prototype Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/kiMgCLXckU0&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Prototype Use Case"><img src="/img/yt_btn_sm.gif" alt="Prototype Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Prototype Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Prototype Use Case"/></a>
Python **id()** function | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25362172/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="python id function"><img src="/img/udemy_btn_sm.gif" alt="python id function"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/tgbGqu3OQD8&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="python id function"><img src="/img/yt_btn_sm.gif" alt="python id function"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="python id function"><img src="/img/skillshare_btn_sm.gif" alt="python id function"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

The **Prototype** design pattern is good for when creating new objects requires more resources than you want to use or have available. You can save resources by just creating a copy of any existing object that is already in memory.

E.g., A file you've downloaded from a server may be large, but since it is already in memory, you could just clone it, and work on the new copy independently of the original.

In the Prototype patterns interface, you create a static clone method that should be implemented by all classes that use the interface.
How the clone method is implemented in the concrete class is up to you.
You will need to decide whether a shallow or deep copy is required.

* A shallow copy, copies and creates new references one level deep, 
* A deep copy, copies and creates new references for all levels.

In Python you have mutable objects such as [Lists](/builder#python-list), [Dictionaries](/singleton#python-dictionary), [Sets](/observer#python-set) and any custom Objects you may have created. A shallow copy, will create new copies of the objects with new references in memory, but the underlying sub data, e.g., the elements in a list, will point to the same memory location as the original object being copied. You will now have two lists, but the elements within the lists will point to the same memory location. So, changing any elements of a copied list will affect the original list also. Be sure to test your implementation that the copy method you use works as expected. Shallow copies are much faster to process than deep copies and deep copies are not always necessary if you are not going to benefit from using it.

## Terminology

* **Prototype Interface**: The interface that describes the `clone()` method.
* **Prototype**: The Object/Product that implements the Prototype interface.
* **Client**: The client application that uses and creates the ProtoType.

## Prototype UML Diagram

![Prototype UML Diagram](/img/prototype_concept.svg)

## Source Code

Experiment with the concept code. 

By default, it will shallow copy the object you've asked to be cloned. The object can be any type from number to string to dictionary to anything custom that you've created.

In my example, I have created a list of numbers. At first impressions, when this list is copied, it will appear that the list was fully cloned. But the inner items of the list were not. They will point to the same memory location as the original list; however, the memory identifier of the new list is new and different from the original.

In the `MyClass.clone()` method, there is a line `self.field.copy()` that is commented out. Uncomment out this line, and comment out the line before it to now be `# self.field` . Re execute the file, and now the list items will be copied as well. This however is still not a full deep copy. If the list items were actually other lists, dictionaries or other collections, rather than the numbers that they are, then only the 1st level of that copy would have been cloned to new memory identifiers. I call this a 2-level copy.

For a full recursive copy, use the `copy.deepcopy()` method that is part of an extra dedicated `copy` import included with Python. I demonstrate this in the [/prototype/document.py](/prototype/document.py) file. 

Remember that full deep copies can potentially be much slower for very complicated object hierarchies.

## Summary

*...Refer to Book or Videos for extra content.*