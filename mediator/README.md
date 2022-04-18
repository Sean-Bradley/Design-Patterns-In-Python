# Mediator Design Pattern

## Videos

Section | Video Links
-|-
Mediator Overview |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16511990/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Mediator Overview"><img src="/img/udemy_btn_sm.gif" alt="Mediator Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/9bcLUtBoO04&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Mediator Overview"><img src="/img/yt_btn_sm.gif" alt="Mediator Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Mediator Overview"><img src="/img/skillshare_btn_sm.gif" alt="Mediator Overview"/></a>
Mediator Use Case |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25615950/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Mediator Use Case"><img src="/img/udemy_btn_sm.gif" alt="Mediator Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/IIOkn92bVqA&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Mediator Use Case"><img src="/img/yt_btn_sm.gif" alt="Mediator Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Mediator Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Mediator Use Case"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>

## Overview

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Terminology

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Mediator UML Diagram

![Mediator Pattern UML Diagram](/img/mediator_concept.svg)

## Source Code

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Output

``` bash
python ./mediator/mediator_concept.py    
COLLEAGUE1 <--> Here is the Colleague2 specific data you asked for
COLLEAGUE2 <--> Here is the Colleague1 specific data you asked for
```

## Example Use Case

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Example UML Diagram

![Mediator Pattern UML Diagram](/img/mediator_example.svg)

## Output

``` bash
python ./mediator/client.py
Component1: >>> Out >>> : data A
Component2: <<< In <<< : data A
Component3: <<< In <<< : data A
Component2: >>> Out >>> : data B
Component3: <<< In <<< : data B
Component1: <<< In <<< : data B
Component3: >>> Out >>> : data C
Component2: <<< In <<< : data C
Component1: <<< In <<< : data C
```

## Summary

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._