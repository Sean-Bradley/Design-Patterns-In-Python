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
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>

## Overview

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Terminology

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Flyweight UML Diagram

![Flyweight Pattern UML Diagram](/img/flyweight_concept.svg)

## Source Code

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Output

``` bash
python ./flyweight/flyweight_concept.py
abracadabra
abracadabra has 11 letters
FlyweightFactory has 5 flyweights
```

## Example Use Case

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

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

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._