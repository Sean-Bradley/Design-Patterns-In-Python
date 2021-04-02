# Interpreter Design Pattern

## Videos

Section | Video Links
-|-
Interpreter Overview | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25512242/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Interpreter Overview"><img src="/img/udemy_btn_sm.gif" alt="Interpreter Overview"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/SahV6h8qU-k&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Interpreter Overview"><img src="/img/yt_btn_sm.gif" alt="Interpreter Overview"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Interpreter Overview"><img src="/img/skillshare_btn_sm.gif" alt="Interpreter Overview"/></a>
Interpreter Use Case | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25512246/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="Interpreter Use Case"><img src="/img/udemy_btn_sm.gif" alt="Interpreter Use Case"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/6Q8FJbF-bpA&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="Interpreter Use Case"><img src="/img/yt_btn_sm.gif" alt="Interpreter Use Case"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="Interpreter Use Case"><img src="/img/skillshare_btn_sm.gif" alt="Interpreter Use Case"/></a>
String Slicing | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25598670/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="String Slicing"><img src="/img/udemy_btn_sm.gif" alt="String Slicing"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/Q4JRceZzsQk&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="String Slicing"><img src="/img/yt_btn_sm.gif" alt="String Slicing"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="String Slicing"><img src="/img/skillshare_btn_sm.gif" alt="String Slicing"/></a>
__repr__ Dunder Method | <a id="udemyVideoLink" href="https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25551608/?referralCode=7493DBBBF97FF2B0D24D" target="_blank" title="__repr__ Dunder Method"><img src="/img/udemy_btn_sm.gif" alt="__repr__ Dunder Method"/></a>&nbsp;<a id="ytVideoLink" href="https://youtu.be/sAlqyUggptU&list=PLKWUX7aMnlEJzRvCXnwFEdk_WJDNjMDOo" target="_blank" title="__repr__ Dunder Method"><img src="/img/yt_btn_sm.gif" alt="__repr__ Dunder Method"/></a>&nbsp;<a id="skillShareVideoLink" href="https://skl.sh/34SM2Xg" target="_blank" title="__repr__ Dunder Method"><img src="/img/skillshare_btn_sm.gif" alt="__repr__ Dunder Method"/></a>

## Book 

Cover | Links
-|-
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a>

## Overview

The **Interpreter** pattern helps to convert information from one language into another. 

The language can be anything such as words in a sentence, numerical formulas or even software code.

The process is to convert the source information, into an **Abstract Syntax Tree (AST)** of **Terminal** and **Non-Terminal** expressions that all implement an `interpret()` method.

A Non-Terminal expression is a combination of other Non-Terminal and/or Terminal expressions.

Terminal means terminated, i.e., there is no further processing involved.

An AST root starts with a Non-Terminal expression and then resolves down each branch until all expressions terminate.

An example expression is `A + B` .

The `A` and `B` are Terminal expressions and the `+` is Non-Terminal because it depends on the two other Terminal expressions.

The Image below, is an AST for the expression `5 + 4 - 3 + 7 - 2`

![Abstract Syntax Tree Example](/img/interpreter_ast.svg)

The official Interpreter pattern described in the original GoF Design Patterns book does not state how to construct an Abstract Syntax Tree. How your tree is constructed will depend on the grammatical constructs of your sentence that you want to interpret. 

Abstract Syntax Trees can be created manually or dynamically from a custom parser script. In the first example code below, I construct the AST manually.

Once the AST is created, you can then choose the root node and then run the Interpret operation on that and it should interpret the whole tree recursively.

## Terminology

* **Abstract Expression**: Describe the method(s) that Terminal and Non-Terminal expressions should implement.
* **Non-Terminal Expression**: A composite of Terminal and/or Non-Terminal expressions. 
* **Terminal Expression**: A leaf node Expression.
* **Context**: Context is state that can be passed through interpret operations if necessary.
* **Client**: Builds or is given an Abstract Syntax Tree to interpret.

## Interpreter UML Diagram

![Interpreter UML Diagram](/img/interpreter_concept.svg)

## Source Code

*...Refer to Book or Videos for extra content.*

## Output

``` bash
python ./interpreter/interpreter_concept.py
5 + 4 - 3 + 7 - 2
['5', '+', '4', '-', '3', '+', '7', '-', '2']
11
((((5 Add 4) Subtract 3) Add 7) Subtract 2)
```

## Example Use Case

*...Refer to Book or Videos for extra content.*

![Abstract Syntax Tree Example](/img/interpreter_ast_roman_numeral.svg)

## Example UML Diagram

![Interpreter Pattern Overview](/img/interpreter_example.svg)

## Output

``` bash
python ./interpreter/client.py 
5 + IV - 3 + VII - 2
['5', '+', 'IV', '-', '3', '+', 'VII', '-', '2']
11
((((5 Add IV(4)) Subtract 3) Add VII(7)) Subtract 2)
```

## New Coding Concepts

### String Slicing

Sometimes you want part of a string. In the example code, when I am interpreting the roman numerals, I am comparing the first one or two characters in the context with `IV` or `CM` or many other roman numeral combinations. If the match is true then I continue with further commands.

The format is

``` python
string[start: end: step]
```

E.g., the string may be

``` text
MMMCMXCIX
```

and I want the first three characters, 

``` python
test = "MMMCMXCIX"
print(test[0: 3])
```

Outputs

``` text
MMM
```

or I want the last 4 characters

``` python
test = "MMMCMXCIX"
print(test[-4:])
```

Outputs

``` text
XCIX
```

or I want a section in the middle

``` python
test = "MMMCMXCIX"
print(test[2:5])
```

Outputs

``` text
MCM
```

or stepped

``` python
test = "MMMCMXCIX"
print(test[2:9:2])
```

Outputs

``` text
MMCX
```

or even reversed

``` python
test = "MMMCMXCIX"
print(test[::-1])
```

Outputs

``` text
XICXMCMMM
```

The technique is very common in examples of Python source code throughout the internet. So, when you see the `[]` with numbers and colons inside, eg, `[:-1:]`, it is likely to do with extracting a portion of a data structure. 

Note that the technique also works on [Lists](/builder#python-list) and [Tuples](/bridge#python-tuple).

``` python
test = [1,2,3,4,5,6,7,8,9]
print(test[0: 3])
print(test[-4:])
print(test[2:5])
print(test[2:9:2])
print(test[::-1])
print(test[:-1:])
```

Outputs

``` text
[1, 2, 3]
[6, 7, 8, 9]
[3, 4, 5]
[3, 5, 7, 9]
[9, 8, 7, 6, 5, 4, 3, 2, 1]
[1, 2, 3, 4, 5, 6, 7, 8]
```

## Summary

*...Refer to Book or Videos for extra content.*