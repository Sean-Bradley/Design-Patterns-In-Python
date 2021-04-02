# Flyweight Design Pattern

## Videos

Section | Video Links
-|-
Flyweight Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25493486/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Flyweight Overview"><img src="/img/udemy_btn_sm.gif" alt="Flyweight Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/F_r2FAVIw5E&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Flyweight Overview"><img src="/img/yt_btn_sm.gif" alt="Flyweight Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Flyweight Overview"><img src="/img/skillshare_btn_sm.gif" alt="Flyweight Overview"/></a>
Flyweight Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25493490/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Flyweight Use Case"><img src="/img/udemy_btn_sm.gif" alt="Flyweight Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/sqVswGe7Zec&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Flyweight Use Case"><img src="/img/yt_btn_sm.gif" alt="Flyweight Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Flyweight Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Flyweight Use Case"/></a>
String Justification | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25493496/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="String Justification"><img src="/img/udemy_btn_sm.gif" alt="String Justification"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/a4iM-mT6okg&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="String Justification"><img src="/img/yt_btn_sm.gif" alt="String Justification"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="String Justification"><img src="/img/skillshare_btn_sm.gif" alt="String Justification"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

**Fly** in the term **Flyweight** means light/not heavy. 

Instead of creating thousands of objects that share common attributes, and result in a situation where a large amount of memory or other resources are used, you can modify your classes to share multiple instances simultaneously by using some kind of reference to the shared object instead.

The best example to describe this is a document containing many words and sentences and made up of many letters. Rather than storing a new object for each individual letter describing its font, position, color, padding and many other potential things. You can store just a lookup id of a character in a collection of some sort and then dynamically create the object with its proper formatting etc., only as you need to.

This approach saves a lot of memory at the expense of using some extra CPU instead to create the object at presentation time.

The Flyweight pattern, describes how you can share objects rather than creating thousands of almost repeated objects unnecessarily.

A Flyweight acts as an independent object in any number of contexts. A context can be a cell in a table, or a div on a html page. A context is using the Flyweight.

You can have many contexts, and when they ask for a Flyweight, they will get an object that may already be shared amongst other contexts, or already within it self somewhere else.

When describing flyweights, it is useful to describe it in terms of intrinsic and extrinsic attributes.

**Intrinsic** (in or including) are the attributes of a flyweight that are internal and unique from the other flyweights. E.g., a new flyweight for every letter of the alphabet. Each letter is intrinsic to the flyweight.

**Extrinsic** (outside or external) are the attributes that are used to present the flyweight in terms of the context where it will be used. E.g., many letters in a string can be right aligned with each other. The extrinsic property of each letter is the new positioning of its X and Y on a grid.

## Terminology

* **Flyweight Interface**: An interface where a flyweight receives its extrinsic attributes.
* **Concrete Flyweight**: The flyweight object that stores the intrinsic attributes and implements the interface to apply extrinsic attributes.
* **Unshared Flyweights**: Not all flyweights will be shared, the flyweight enables sharing, not enforcing it. It also possible that flyweights can share other flyweights but still not yet be used in any contexts anywhere.
* **Flyweight Factory**: Creates and manages flyweights at runtime. It reuses flyweights in memory, or creates a new one in demand.
* **Client**: The client application that uses and creates the Flyweight.

## Flyweight UML Diagram

![Flyweight Pattern UML Diagram](/img/flyweight_concept.svg)

## Source Code

*...Refer to Book or Videos for extra content.*

## Output

``` bash
python ./flyweight/flyweight_concept.py
abracadabra
abracadabra has 11 letters
FlyweightFactory has 5 flyweights
```

## Example Use Case

*...Refer to Book or Videos for extra content.*

## Example UML Diagram

![Flyweight Pattern Use Case UML Diagram](/img/flyweight_example.svg)

## Output

``` bash
python ./flyweight/client.py    
-----------------------------------------
|abra       |     112233    |    cadabra|
|racadab    |     12345     |     332211|
|cadabra    |     445566    |   aa 22 bb|
-----------------------------------------
FlyweightFactory has 12 flyweights
```

## New Coding Concepts

### String Justification

In [/flyweight/column.py](/flyweight/column.py), there are commands `center()`, `ljust()` and `rjust()` . 

These are special commands on strings that allow you to pad strings and align them left, right, center depending on total string length.

eg, 

``` powershell
>>> "abcd".center(10)
'   abcd   '
```

``` powershell
>>> "abcd".rjust(10)  
'      abcd'
```

``` powershell
>>> "abcd".ljust(10) 
'abcd      '
```

## Summary

*...Refer to Book or Videos for extra content.*