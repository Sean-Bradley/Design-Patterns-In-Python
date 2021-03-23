# Mediator Design Pattern

## Videos

Section | Video Links
-|-
Mediator Overview |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16511990/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Mediator Overview"><img src="/img/udemy_btn_sm.gif" alt="Mediator Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/9bcLUtBoO04" target="_blank" title="Mediator Overview"><img src="/img/yt_btn_sm.gif" alt="Mediator Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Mediator Overview"><img src="/img/skillshare_btn_sm.gif" alt="Mediator Overview"/></a>
Mediator Use Case |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25615950/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Mediator Use Case"><img src="/img/udemy_btn_sm.gif" alt="Mediator Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/IIOkn92bVqA" target="_blank" title="Mediator Use Case"><img src="/img/yt_btn_sm.gif" alt="Mediator Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Mediator Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Mediator Use Case"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

Objects communicate through the **Mediator** rather than directly with each other.

As a system evolves and becomes larger and supports more complex functionality and business rules, the problem of communicating between these components becomes more complicated to understand and manage. It may be beneficial to refactor your system to centralize some or all of its functionality via some kind of mediation process.

The mediator pattern is similar to implementing a [Facade](/facade) pattern between your objects and processes. Except that the structure of the Mediator allows multi directional communication between the objects or processes that would normally be interacting directly with each other.

While the Facade is a structural pattern, and the Mediator also implies structure in the way that it exists between two or more other objects or processes, it also allows changing the behavior of the interaction to make it more cooperative in some way. E.g., the centralization  of application logic, managing the routing behavior, caching, logging, etc.

## Terminology

* **Mediator**: The coordinator of communications between the components (colleagues).
* **Colleagues**: One of the many types of concrete components that use the mediator. 

## Mediator UML Diagram

![Mediator Pattern UML Diagram](/img/mediator_concept.svg)

## Source Code

In the example concept, there are two colleague classes that use each other's methods. Instead of the Colleagues calling each other's methods directly, they implement the Mediator interface and call each other via the Mediator. Each colleague is designed for a different purpose, but they utilize some related functionality from each other. 

The system, in this case, would work without the Mediator, but adding the Mediator would allow extending functionality to a potential third colleague that provides a different service, such as AI analysis or monitoring, without needing to add specific support or knowledge into the two original colleagues.

In this first example the Mediator is structurally acting as a multi directional relay between the two colleagues.

## Output

``` bash
python ./mediator/mediator_concept.py    
COLLEAGUE1 <--> Here is the Colleague2 specific data you asked for
COLLEAGUE2 <--> Here is the Colleague1 specific data you asked for
```

## Example Use Case

In this example use case, we will implement some behavior into the mediation process.

Before the mediation logic is added, consider that the below example is a series of components all subscribed to a central location being the subject. They all implement the [Observer](/observer) pattern.

Each component is updated independently by external forces, but when it has new information, it notifies the subject which in turn then notifies the other subscribed components.

During the synchronization of all the subscribed components, without the extra mediation, the component that provided the new information will receive back the same message that it just notified the subject of. In order to manage the unnecessary duplicate message, the notifications will be mediated to exclude to component where the original message originated from.

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
