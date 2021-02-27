# Chain of Responsibility Design Pattern

## Overview

**Chain of Responsibility** pattern is a behavioral pattern used to achieve loose coupling in software design.

In this pattern, an object is passed to a **Successor**, and depending on some kind of logic, will or won't be passed onto another successor and processed. There can be any number of different successors and successors can be re-processed recursively. 

This process of passing objects through multiple successors is called a chain.

The object that is passed between each successor does not know about which successor will handle it. It is an independent object that may or may not be processed by a particular successor before being passed onto the next.

The chain that the object will pass through is normally dynamic at runtime, although you can hard code the order or start of the chain, so each successor will need to comply with a common interface that allows the object to be received and passed onto the next successor.

## Terminology

* **Handler Interface**: A common interface for handling and passing objects through each successor.
* **Concrete Handler**: The class acting as the **Successor** handling the requests and passing onto the next.
* **Client**: The application or class that initiates the call to the first concrete handler (successor) in the chain.

## Chain of Responsibility UML Diagram

![Chain of Responsibility Design Pattern](/img/chain_of_responsibility_concept.svg)

## Source Code

In this concept code, a chain is created with a default first successor. A number is passed to a successor, which then does a random test, and depending on the result will modify the number and then pass it onto the next successor. The process is randomized and will end at some point when there are no more successors designated.

## Output

``` bash
python ./chain_of_responsibility/chain_of_responsibility_concept.py
Successor1 payload = 1
Successor2 payload = -1
Successor2 payload = -0.5
Successor2 payload = -0.25
Successor1 payload = -0.5
Successor1 payload = 0.5
Successor2 payload = -1.5
Finished result = -1.5
```

## Example Use Case

In the ATM example below, the chain is hard coded in the client first to dispense amounts of £50s, then £20s and then £10s in order. 

This default chain order helps to ensure that the minimum number of notes will be dispensed. Otherwise, it might dispense 5 x £10 when it would have been better to dispense 1 x £50.

Each successor may be re-called recursively for each denomination depending on the value that was requested for withdrawal.

## Example UML Diagram

![Chain of Responsibility Design Pattern](/img/chain_of_responsibility_example.svg)

## Output

``` bash
python ./chain_of_responsibility/client.py
Enter amount to withdrawal : 180
Dispensing 3 £50 note(s)
Dispensing 1 £20 note(s)
Dispensing 1 £10 note
Now go spoil yourself
```

## New Coding Concepts

### Floor Division

Normally division uses a single **/** character and will return a float even if the numbers are integers or exactly divisible with no remainder, 

E.g., 

``` python
PS> python
>>> 9 / 3
3.0
```

Python Version 3 also has an option to return an integer version (floor) of the number by using the double **//** characters instead.

``` python
PS> python
>>> 9 // 3
3
```

See PEP-0238 : [https://www.python.org/dev/peps/pep-0238/](https://www.python.org/dev/peps/pep-0238/)

### Accepting User Input

In the file [/chain_of_responsibility/client.py](/chain_of_responsibility/client.py) above, there is a command `input` .

The `input` command allows your script to accept user input from the command prompt. 

In the ATM example, when you start it, it will ask the user to enter a number.

Then when the user presses the `enter` key, the input is converted to an integer and the value tested if valid.

``` python
AMOUNT = int(input("Enter amount to withdrawal : "))
if AMOUNT < 10 or AMOUNT % 10 != 0:
    ...continue

```

Note that in Python 2.x, use the `raw_input()` command instead of `input()` .

See PEP-3111 : [https://www.python.org/dev/peps/pep-3111/](https://www.python.org/dev/peps/pep-3111/)

## Summary

* The object will propagate through the chain until fully processed.
* The object does not know which successor or how many will process it.
* The next successor in the chain is chosen dynamically at runtime depending on logic from the current successor.
* Successors implement a common interface which makes them work independently of each other, so that they can be used recursively or possibly in a different order.
* A user wizard, or dynamic questionnaire are other common use cases for the chain of responsibility pattern.
* The chain of responsibility and [Composite](/composite) patterns are often used together because of their similar approach to hierarchy and possible re-ordering. The Composites parent/child relationship is set in an object's property by a process outside of the class and can be changed at runtime. While with the Chain of Responsibility, each successor runs a dynamic algorithm internally, to decide which successor is next in line.
* The chain can be fully dynamically created, or it can be set as a default with the possibility of changing at runtime.
