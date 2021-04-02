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

*...Refer to Book or Videos for extra content.*

## Summary

*...Refer to Book or Videos for extra content.*