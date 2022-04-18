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
![Design Patterns In Python (ASIN : B08XLJ8Z2J)](/img/design_patterns_in_python_book_125x178.jpg) | &nbsp;<a href="https://www.amazon.com/dp/B08XLJ8Z2J"><img src="/img/flag_us.gif">&nbsp; https://www.amazon.com/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.uk/dp/B08XLJ8Z2J"><img src="/img/flag_uk.gif">&nbsp; https://www.amazon.co.uk/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.in/dp/B08Z282SBC"><img src="/img/flag_in.gif">&nbsp; https://www.amazon.in/dp/B08Z282SBC</a><br/>&nbsp;<a href="https://www.amazon.de/dp/B08XLJ8Z2J"><img src="/img/flag_de.gif">&nbsp; https://www.amazon.de/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.fr/dp/B08XLJ8Z2J"><img src="/img/flag_fr.gif">&nbsp; https://www.amazon.fr/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.es/dp/B08XLJ8Z2J"><img src="/img/flag_es.gif">&nbsp; https://www.amazon.es/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.it/dp/B08XLJ8Z2J"><img src="/img/flag_it.gif">&nbsp; https://www.amazon.it/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.co.jp/dp/B08XLJ8Z2J"><img src="/img/flag_jp.gif">&nbsp; https://www.amazon.co.jp/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.ca/dp/B08XLJ8Z2J"><img src="/img/flag_ca.gif">&nbsp; https://www.amazon.ca/dp/B08XLJ8Z2J</a><br/>&nbsp;<a href="https://www.amazon.com.au/dp/B08Z282SBC"><img src="/img/flag_au.gif">&nbsp; https://www.amazon.com.au/dp/B08Z282SBC</a>

## Overview

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Terminology

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Interpreter UML Diagram

![Interpreter UML Diagram](/img/interpreter_concept.svg)

## Source Code

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

## Output

``` bash
python ./interpreter/interpreter_concept.py
5 + 4 - 3 + 7 - 2
['5', '+', '4', '-', '3', '+', '7', '-', '2']
11
((((5 Add 4) Subtract 3) Add 7) Subtract 2)
```

## Example Use Case

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._

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

_... Refer to [Book](https://www.amazon.com/dp/B08Z282SBC), pause [Video Lectures](#videos) or subscribe to [Medium Membership](https://sean-bradley.medium.com/membership) to read textual content._