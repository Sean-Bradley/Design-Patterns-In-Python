# Interpreter Design Pattern

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

In this example, I interpret the string `5 + 4 - 3 + 7 - 2` and then calculate the result.

The grammar of the string follows a pattern of Number -> Operator -> Number -> etc.

I convert the string into a list of tokens that I can refer to by index in the list.

I then construct the AST manually, by adding a

1. Non-Terminal `Add` row containing two Terminals for the `5` and `4`, 
2. Non-Terminal `Subtract` row containing the previous Non-Terminal row and the `3`
3. Non-Terminal `Add` row containing the previous Non-Terminal row and the `7`
4. Non-Terminal `Subtract` row containing the previous Non-Terminal row and the `2`

The AST root becomes the final row that was added, and then I can run the `interpret()` method on that, which will interpret the full AST recursively because each AST row references the row above it.

## Output

``` bash
python ./interpreter/interpreter_concept.py
5 + 4 - 3 + 7 - 2
['5', '+', '4', '-', '3', '+', '7', '-', '2']
11
((((5 Add 4) Subtract 3) Add 7) Subtract 2)
```

## Example Use Case

The example use case will expand on the concept example by dynamically creating the AST and converting roman numerals to integers as well as calculating the final result.

The Image below, is an AST for the expression `5 + IV - 3 + VII - 2`

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

* ASTs are hard to create and are an enormous subject in themselves. My recommended approach is to create them manually first using a sample sentence to help understand all the steps individually, and then progress the conversion to be fully dynamic one step at a time ensuring that the grammatical constructs still work as you continue to progress.

* The Interpreter pattern uses a class to represent each grammatical rule.

* ASTs consist of multiple Non-Terminal and Terminal Expressions, that all implement an `interpret()` method.

* Note that in the sample code above, the `interpret()` methods in the Non-Terminal expressions, all call further `interpret()` recursively. Only the Terminal expressions `interpret()` method returns an explicit value. See the [Number](/interpreter/number.py) class in the above code.
