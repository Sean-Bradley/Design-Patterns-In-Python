# Command Design Pattern

## Videos

Section | Video Links
-|-
Command Overview |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16397092/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Command Overview"><img src="/img/udemy_btn_sm.gif" alt="Command Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/jOxlrGeAKQ4&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Command Overview"><img src="/img/yt_btn_sm.gif" alt="Command Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Command Overview"><img src="/img/skillshare_btn_sm.gif" alt="Command Overview"/></a>
Command Use Case |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25551578/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Command Use Case"><img src="/img/udemy_btn_sm.gif" alt="Command Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/qDM8ZFcQwZM&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Command Use Case"><img src="/img/yt_btn_sm.gif" alt="Command Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Command Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Command Use Case"/></a>
Single Leading Underscore | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25551594/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Single Leading Underscore"><img src="/img/udemy_btn_sm.gif" alt="Single Leading Underscore"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/dDIqJI9aTAc&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Single Leading Underscore"><img src="/img/yt_btn_sm.gif" alt="Single Leading Underscore"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Single Leading Underscore"><img src="/img/skillshare_btn_sm.gif" alt="Single Leading Underscore"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>

## Overview

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Terminology

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Command Pattern UML Diagram

![The Command Pattern UML Diagram](/img/command_concept.svg)

## Source Code

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Output

``` bash
python ./command/command_concept.py
Executing Command 1
Executing Command 2
Executing Command 1
Executing Command 2
```

## Example Use Case

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Example UML Diagram

![The Command Pattern UML Diagram](/img/command_example.svg)

## Output

``` bash
python ./command/client.py
Light turned ON
Light turned OFF
Light turned ON
Light turned OFF
11:23:35 : ON
11:23:35 : OFF
11:23:35 : ON
11:23:35 : OFF
Light turned ON
Light turned OFF
```

## New Coding Concepts

### _Single Leading Underscore

The single leading underscore **`_variable`**, on your class variables is a useful indicator to other developers that this property should be considered private.

Private, in C style languages, means that the variable/field/property is hidden and cannot be accessed outside of the class. It can only be used internally by its own class methods.

Python does not have a public/private accessor concept so the variable is not actually private and can still be used outside of the class in other modules. 

It is just a useful construct that you will see developers use as a recommendation not to reference this variable directly outside of this class, but use a dedicated method or property instead.

## Summary

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._