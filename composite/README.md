# Composite Design Pattern

## Videos

Section | Video Links
-|-
Composite Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16511234/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Composite Overview"><img src="/img/udemy_btn_sm.gif" alt="Composite Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/Wihw5oIsh2g&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Composite Overview"><img src="/img/yt_btn_sm.gif" alt="Composite Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Composite Overview"><img src="/img/skillshare_btn_sm.gif" alt="Composite Overview"/></a>
Composite Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25473576/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Composite Use Case"><img src="/img/udemy_btn_sm.gif" alt="Composite Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/5MjYcxO_TUk&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Composite Use Case"><img src="/img/yt_btn_sm.gif" alt="Composite Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Composite Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Composite Use Case"/></a>
Conditional Expressions | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25473582/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Conditional Expressions"><img src="/img/udemy_btn_sm.gif" alt="Conditional Expressions"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/meX3QlEJI2Q&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Conditional Expressions"><img src="/img/yt_btn_sm.gif" alt="Conditional Expressions"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Conditional Expressions"><img src="/img/skillshare_btn_sm.gif" alt="Conditional Expressions"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>

## Overview

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Terminology

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Composite UML Diagram

![Composite Pattern UML Diagram](/img/composite_concept.svg)

## Source Code

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Output

``` bash
python ./composite/composite_concept.py

LEAF_A          id:2050574298848
LEAF_B          id:2050574298656
COMPOSITE_1     id:2050574298272
COMPOSITE_2     id:2050574298128

<Leaf>          id:2050574298656        Parent: None
<Composite>     id:2050574298128        Parent: None    Components:2
<Leaf>          id:2050574298848        Parent: 2050574298128
<Composite>     id:2050574298272        Parent: 2050574298128   Components:0
```

## Composite Example Use Case

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Composite Example UML Diagram

![Composite Pattern Use Case UML Diagram](/img/composite_example.svg)

## Output

``` bash
python ./composite/client.py
<DIR>  root             id:2028913323984        Components: 4
..<FILE> abc.txt        id:2028913323888        Parent: 2028913323984
..<FILE> 123.txt        id:2028913323792        Parent: 2028913323984
..<DIR>  folder_a       id:2028913432848        Components: 1
....<FILE> xyz.txt      id:2028913433088        Parent: 2028913432848
..<DIR>  folder_b       id:2028913433184        Components: 1
....<FILE> 456.txt      id:2028913434432        Parent: 2028913433184

<DIR>  root             id:2028913323984        Components: 3
..<FILE> abc.txt        id:2028913323888        Parent: 2028913323984
..<FILE> 123.txt        id:2028913323792        Parent: 2028913323984
..<DIR>  folder_b       id:2028913433184        Components: 2
....<FILE> 456.txt      id:2028913434432        Parent: 2028913433184
....<DIR>  folder_a     id:2028913432848        Components: 1
......<FILE> xyz.txt    id:2028913433088        Parent: 2028913432848
```

## New Coding Concepts

### Conditional Expressions (Ternary Operators).

In [/composite/composite_concept.py](/composite/composite_concept.py), there are two conditional expressions. 

Conditional expressions an alternate form of `if/else` statement.

``` python
id(self.reference_to_parent) if self.reference_to_parent is not None else None
```

If the `self.reference_to_parent` is not `None`, it will return the memory address (id) of `self.reference_to_parent`, otherwise it returns `None`.

This conditional expression follows the format

``` python
value_if_true if condition else value_if_false
```

eg, 

``` python
SUN = "bright"
SUN_IS_BRIGHT = True if SUN == "bright" else False
print(SUN_IS_BRIGHT)
```

or

``` python
ICE_IS_COLD = True
ICE_TEMPERATURE = "cold" if ICE_IS_COLD == True else "hot"
print(ICE_TEMPERATURE)
```

or

``` python
CURRENT_VALUE = 99
DANGER = 100
ALERTING = True if CURRENT_VALUE >= DANGER else False
print(ALERTING)
```

Visit [https://docs.python.org/3/reference/expressions.html#conditional-expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions) for more examples of conditional expressions.

## Summary

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._