# Observer Pattern

## Videos

Section | Video Links
-|-
Observer Overview |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16397486/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Observer Overview"><img src="/img/udemy_btn_sm.gif" alt="Observer Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/w4d3KUhJbek&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Observer Overview"><img src="/img/yt_btn_sm.gif" alt="Observer Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Observer Overview"><img src="/img/skillshare_btn_sm.gif" alt="Observer Overview"/></a>
Observer Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25582772/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Observer Use Case"><img src="/img/udemy_btn_sm.gif" alt="Observer Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/vCA5ZtP-bII&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Observer Use Case"><img src="/img/yt_btn_sm.gif" alt="Observer Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Observer Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Observer Use Case"/></a>
Python **Set** | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25582780/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Python Set"><img src="/img/udemy_btn_sm.gif" alt="Python Set"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/RnF-yEFsZdc&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Python Set"><img src="/img/yt_btn_sm.gif" alt="Python Set"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Python Set"><img src="/img/skillshare_btn_sm.gif" alt="Python Set"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>

## Overview

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Terminology

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Observer UML Diagram

![Observer Pattern Overview](/img/observer_concept.svg)

## Source Code

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Output

``` bash
python ./observer/observer_concept.py
Observer id:2084220160272 received ('First Notification', [1, 2, 3])
Observer id:2084220160224 received ('First Notification', [1, 2, 3])
Observer id:2084220160272 received ('Second Notification', {'A': 1, 'B': 2, 'C': 3})
```

## Example Use Case

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Example UML Diagram

![Observer Pattern in Context](/img/observer_example.svg)

## Output

``` bash
python ./observer/client.py
PieGraph, id:1
Drawing a Pie graph using data:[1, 2, 3]
BarGraph, id:2
Drawing a Bar graph using data:[1, 2, 3]
TableView, id:3
Drawing a Table view using data:[1, 2, 3]
PieGraph, id:1
Drawing a Pie graph using data:[4, 5, 6]
TableView, id:3
Drawing a Table view using data:[4, 5, 6]
```

## New Coding Concepts

### Python Set

A Python **Set** is similar to a List. Except that the items in the Set are guaranteed to be unique, even if you try to add a duplicate. A set is a good choice for keeping a collection of observables, since the problem of duplicate observables is automatically handled.

A Set can be instantiated using the curly braces `{}` or `set()`, verses `[]` for a [List](/builder#python-list) and `()` for a [Tuple](/bridge#python-tuple). It is not the same as a [Dictionary](/singleton#python-dictionary), which also uses `{}`, since the dictionary items are created as `key:value` pairs. ie `{"a": 1, "b": 2, "c": 3}`

``` python
PS> python
>>> items = {"yankee", "doodle", "dandy", "doodle"}
>>> items
{'yankee', 'doodle', 'dandy'}
>>> items.add("grandy")
>>> items
{'grandy', 'yankee', 'doodle', 'dandy'}
>>> items.remove("doodle")
>>> items
{'grandy', 'yankee', 'dandy'}
```

Note, if instantiating an empty **Set** then use `my_object = Set()` rather than `my_object = {}` to reduce ambiguity with creating an empty [Dictionary](/singleton#python-dictionary).

## Summary

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._