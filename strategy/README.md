# Strategy Design Pattern

## Videos

Section | Video Links
-|-
Strategy Overview |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25667386/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Strategy Overview"><img src="/img/udemy_btn_sm.gif" alt="Strategy Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/nk6VWTdFPUM&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Strategy Overview"><img src="/img/yt_btn_sm.gif" alt="Strategy Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Strategy Overview"><img src="/img/skillshare_btn_sm.gif" alt="Strategy Overview"/></a>
Strategy Use Case |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25667396/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Strategy Use Case"><img src="/img/udemy_btn_sm.gif" alt="Strategy Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/PvW4-icGaaI&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Strategy Use Case"><img src="/img/yt_btn_sm.gif" alt="Strategy Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Strategy Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Strategy Use Case"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

The **Strategy** Pattern is similar to the [State](state.md) Pattern, except that the client passes in the algorithm that the context should run.

The algorithm should be contained within a class that implements the particular strategies interface.

An application that sorts data is a good example of where you can incorporate the Strategy pattern.

There are many methods of sorting a set of data. E.g., Quicksort, Mergesort, Introsort, Heapsort, Bubblesort. See [https://en.wikipedia.org/wiki/Sorting_algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm) for more examples. 

The user interface of the client application can provide a drop-down menu to allow the user to try the different sorting algorithms.

Upon user selection, a reference to the algorithm will be passed to the context and processed using this new algorithm instead.

The Strategy and [State](state.md) appear very similar, a good way to differentiate them is to consider whether the state of the context is choosing the algorithm at runtime, or whether the algorithm is being passed into it.

Software Plugins can be implemented using the Strategy pattern. 

## Terminology

* **Strategy Interface**: An interface that all Strategy subclasses/algorithms must implement.
* **Concrete Strategy**: The subclass that implements an alternative algorithm.
* **Context**: This is the object that receives the concrete strategy in order to execute it.

## Strategy UML Diagram

![Strategy UML Diagram](/img/strategy_concept.svg)

## Source Code

There is a Context, and three different strategies to choose from. 

Each Strategy is executed in turn by the context.

## Output

``` bash
python ./strategy/strategy_concept.py
I am ConcreteStrategyA
I am ConcreteStrategyB
I am ConcreteStrategyC
```

## Strategy Example Use Case

A game character is moving through an environment. Depending on the situation within the current environment, the user decides to use a different movement algorithm. From the perspective of the object/context, it is still a move, but the implementation is encapsulated in the subclass at the handle. 

In a real game, the types of things that a particular move could affect is which animation is looped, the audio, the speed, the camera follow mode and more.

## Strategy Example Use Case UML Diagram

![Strategy Example Use Case UML Diagram](/img/strategy_example.svg)

## Output

``` bash
python ./strategy/client.py
I am Walking. New position = [1, 0]
I am Running. New position = [3, 0]
I am Crawling. New position = [3.5, 0]
```

## Summary

*...Refer to Book or Videos for extra content.*