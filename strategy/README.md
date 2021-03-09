# Strategy Design Pattern

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

The **Strategy** Pattern is similar to the [State](/state) Pattern, except that the client passes in the algorithm that the context should run and the execution of the algorithm does not affect the state of the context.

The algorithm should be contained within a class that implements the particular strategies interface.

An application that sorts data is a good example of where you can incorporate the Strategy pattern.

There are many methods of sorting a set of data. E.g., Quicksort, Mergesort, Introsort, Heapsort, Bubblesort. See [https://en.wikipedia.org/wiki/Sorting_algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm) for more examples. 

The user interface of the client application can provide a drop-down menu to allow the user to try the different sorting algorithms.

Upon user selection, a reference to the algorithm will be passed to the context and processed using this new algorithm instead.

The Strategy and [State](/state) appear very similar, a good way to differentiate them is to consider whether the context is considered to be in a new state or not at various times in the lifecycle. 

In the Strategy, an object/context runs a chosen algorithm, but the state of the object/context doesn't change in case you want to try a different algorithm.

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
python.exe ./strategy/strategy_concept.py
I am ConcreteStrategyA
I am ConcreteStrategyB
I am ConcreteStrategyC
```

## Strategy Example Use Case

A game character is moving through an environment. Depending on the situation within the current environment, the user decides to use a different movement algorithm. From the perspective of the object/context, it is still a move, but the implementation is encapsulated in the subclass at the handle. 

In a real game, the types of things that a particular move could affect is which animation is looped, whether physics attributes changed, the speed of movement, the camera follow mode and more.

## Strategy Example Use Case UML Diagram

![Strategy Example Use Case UML Diagram](/img/strategy_example.svg)

## Output

``` bash
python.exe ./strategy/client.py
I am Walking
I am Running
I am Crawling
```

## Summary

* While the Strategy pattern looks very similar to the State pattern, the assigned strategy sub class/algorithm is not changing any state of the context. The class/algorithm can be re-executed or replaced with a different class/algorithm with no effect to the state of the context.

* The Strategy pattern is about having a choice of implementations that accomplish the same relative task.

* The particular strategies algorithm is encapsulated in order to keep the implementation of it de coupled from the context. 

* As soon as the state of the context decides which subclass will be executed, then that is the State pattern, otherwise it is the Strategy pattern because the decision was made externally to the context and can be modified again without affecting the context.
