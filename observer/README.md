# Observer Pattern

## Videos

Section | Video Links
-|-
Observer Overview |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16397486/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Observer Overview"><img src="/img/udemy_btn_sm.gif" alt="Observer Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/w4d3KUhJbek" target="_blank" title="Observer Overview"><img src="/img/yt_btn_sm.gif" alt="Observer Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Observer Overview"><img src="/img/skillshare_btn_sm.gif" alt="Observer Overview"/></a>
Observer Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25582772/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Observer Use Case"><img src="/img/udemy_btn_sm.gif" alt="Observer Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/vCA5ZtP-bII" target="_blank" title="Observer Use Case"><img src="/img/yt_btn_sm.gif" alt="Observer Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Observer Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Observer Use Case"/></a>
Python **Set** | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25582780/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Python Set"><img src="/img/udemy_btn_sm.gif" alt="Python Set"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/RnF-yEFsZdc" target="_blank" title="Python Set"><img src="/img/yt_btn_sm.gif" alt="Python Set"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Python Set"><img src="/img/skillshare_btn_sm.gif" alt="Python Set"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

The **Observer** pattern is a software design pattern in which an object, called the **Subject** (**Observable**), manages a list of dependents, called **Observers**, and notifies them automatically of any internal state changes by calling one of their methods. 

The Observer pattern follows the publish/subscribe concept. A subscriber, subscribes to a publisher. The publisher then notifies the subscribers when necessary.

The observer stores state that should be consistent with the subject. The observer only needs to store what is necessary for its own purposes.

A typical place to use the observer pattern is between your application and presentation layers. Your application is the manager of the data and is the single source of truth, and when the data changes, it can update all of the subscribers, that could be part of multiple presentation layers. For example, the score was changed in a televised cricket game, so all the web browser clients, mobile phone applications, leaderboard display on the ground and television graphics overlay, can all now have the updated information synchronized.

Most applications that involve a separation of data into a presentation layer can be broken further down into the Model-View-Controller (MVC) concept.

* **Controller** : The single source of truth.
* **Model** : The link or relay between a controller and a view. It may use any of the structural patterns (adapter, bridge, facade, proxy, etc.) at some point.
* **View** : The presentation layer of the of the data from the model.

The observer pattern can be used to manage the transfer of data across any layer and even internally to itself to add a further abstraction. In the MVC structure, the View can be a subscriber to the Model, that in turn can also be a subscriber to the controller. It can also happen the other way around if the use case warrants. 

The Observer pattern allows you to vary subjects and observers independently. You can reuse subjects without reusing their observers, and vice versa. It lets you add observers without modifying the subject or any of the other observers. 

The observer pattern is commonly described as a push model, where the subject pushes updates to all observers. But observers can pull for updates and also only if it decides it is necessary.

Whether you decide to use a push or pull concept to move data, then there are pros and cons to each. You may decide to use a combination of both to manage reliability.

E.g., When sending messages across a network, the receiving client, can be slow to receive the full message that was sent, or even timeout. This pushing from the sender's side can increase the amount of network hooks or threads if there are many messages still waiting to be fully delivered. The subject is taking responsibility for the delivery.

On the other hand, if the observer requests for an update from the subscriber, then the subject (observable) can return the information as part of the requests response. The observer could also indicate as part of the request, to only return data applicable to X, which would then make the response message smaller to transfer at the expense of making the observable more coupled to the observer.

Use a push mechanism from the subject when updates are absolutely required in as close to real time from the perspective of the observer, noting that you may need to manage the potential of extra unresolved resources queueing up at the sender. 

If updates on the observer end are allowed to suffer from some delay, then a pull mechanism is most reliable and easiest to manage since it is the responsibly of the observer to synchronize its state. 

## Terminology

* **Subject Interface**: (Observable Interface) The interface that the subject should implement.
* **Concrete Subject**: (Observable) The object that is the subject.
* **Observer Interface**: The interface that the observer should implement.
* **Concrete Observer**:  The object that is the observer. There can be a variable number of observers which can subscribe/unsubscribe during runtime.

## Observer UML Diagram

![Observer Pattern Overview](/img/observer_concept.svg)

## Source Code

A Subject (Observable) is created.

Two Observers are created. They could be across a network, but for demonstration purposes are within the same client.

The Subject notifies the Observers.

One of the Observers unsubscribes, 

The Subject notifies the remaining Observer again.

## Output

``` bash
python ./observer/observer_concept.py
Observer id:2084220160272 received ('First Notification', [1, 2, 3])
Observer id:2084220160224 received ('First Notification', [1, 2, 3])
Observer id:2084220160272 received ('Second Notification', {'A': 1, 'B': 2, 'C': 3})
```

## Example Use Case

This example mimics the **MVC** approach described earlier.

There is an external process called a `DataController`, and a client process that holds a `DataModel` and multiple `DataViews` which are a Pie graph, Bar graph and Table view. 

Note that this example runs in a single process, but imagine that the `DataController` is actually an external process running on a different server.

The `DataModel` subscribes to the `DataController` and the `DataViews` subscribe to the `DataModel` .

The client sets up the various views with a subscription to the `DataModel` . 

The hypothetical external `DataController` then updates the external data, and the data then propagates through the layers to the views.

Note that in reality this example would be much more complex if multiple servers are involved. I am keeping it brief to demonstrate one possible use case of the observer pattern.

Also note that in the `DataController`, the references to the observers are contained in a [Set](#python-set), while in the `DataModel` I have used a [Dictionary](/singleton#python-dictionary) instead, so that you can see an alternate approach.

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

!!! Note

    If instantiating an empty **Set** then use `my_object = Set()` rather than `my_object = {}` to reduce ambiguity with creating an empty [Dictionary](/singleton#python-dictionary).
