# Chain of Responsibility Design Pattern

## Videos

Section | Video Links
-|-
Chain of Responsibility |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/16397342/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Chain of Responsibility Overview"><img src="/img/udemy_btn_sm.gif" alt="Chain of Responsibility Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/Ayb6UShWcUU&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Chain of Responsibility Overview"><img src="/img/yt_btn_sm.gif" alt="Chain of Responsibility Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Chain of Responsibility Overview"><img src="/img/skillshare_btn_sm.gif" alt="Chain of Responsibility Overview"/></a>
Use Case |  <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25567252/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Chain of Responsibility Use Case"><img src="/img/udemy_btn_sm.gif" alt="Chain of Responsibility Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/BxiAyLGAJqw&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Chain of Responsibility Use Case"><img src="/img/yt_btn_sm.gif" alt="Chain of Responsibility Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Chain of Responsibility Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Chain of Responsibility Use Case"/></a>
Python Floor Division | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25567266/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Python Floor Division"><img src="/img/udemy_btn_sm.gif" alt="Python Floor Division"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/kR4pYqVpNb0&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Python Floor Division"><img src="/img/yt_btn_sm.gif" alt="Python Floor Division"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Python Floor Division"><img src="/img/skillshare_btn_sm.gif" alt="Python Floor Division"/></a>
Accepting User Input | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25567278/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Accepting User Input"><img src="/img/udemy_btn_sm.gif" alt="Accepting User Input"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/wC2gBf1D1CU&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Accepting User Input"><img src="/img/yt_btn_sm.gif" alt="Accepting User Input"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Accepting User Input"><img src="/img/skillshare_btn_sm.gif" alt="Accepting User Input"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

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
