# Coding Conventions

## Python Interactive Console Versus *.py Scripts

You can execute Python code by writing your scripts into text files and commonly using the `.py` extension. Text files on most operating systems will be UTF-8 encoded by default. Python also reads UTF-8 encoded text files by default. 

Create a new text file called `example.py` and add the following text.

``` python
print("Hello World!")
```

and then you can execute it using `python` or `python3` depending on your operating system and Python version.

``` bash
PS> python ./example.py
Hello World!
```

You can also enter Python code directly into the Python Interactive Console by typing just `python` or `python3` from the command line and then press `Enter` . You then get a prompt like below.

``` python
PS> python
Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC ...
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can now enter python commands directly.

``` 

>>> print("Hello World!")
Hello World!
>>> 
```

To exit the Python Interactive Console, you can usually type `quit()` or press `Ctrl-Z` then press `Enter`

This repository will show examples of using both `*.py` scripts and the interactive console to execute Python. Look out for the `>>>` characters in the code blocks to indicate if I was using the Python Interactive Console or a `*.py` script.

## PEP8

The code styling in this repository is formatted using mostly PEP8 styling recommendations.

* **UPPER_CASE** : Constants will be defined using UPPER_CASE naming style.
* **PascalCase** : Class names will use PascalCase naming style
* **snake_case** : For variables names, method names and method arguments.
* **Docstrings** : Classes and methods contain extra documentation that is descriptive text enclosed in " or """ for multiline strings.
* **_leading_underscore** : Use a leading underscore to indicate variables that should be considered as private class variables.

See PEP-0008 : [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

## Pylint

I use the Pylint tool to check for code styling recommendations.

On most operating systems you would generally install Pylint by using the `PIP` or `PIP3` installer.

``` powershell
pip install pylint
```

If using VSCode, open the Command Palette (Ctrl+Shift+P), then set the 

`Python: Enable Linting` to `on`

and 

`Python: Select Linter` to `Pylint`

## Common Pylint Warning and Error Messages

| ID | Message | Description |
|-|-|-|
| R0201 | Method could be a function (no-self-use)<img width="500"/> | Your method has an attribute that refers to `self` or `cls`, but it is not necessary since your are **NOT** using `self` or `cls` within the method body. You have the option of using the `@staticmethod` decorator on your methods instead, and to remove the `self` or `cls` from the method attributes. |
| R0903 | Too few public methods (1/2) (too-few-public-methods) | The error assumes that your class may be used for just storing data. You could use a dictionary instead. However the assumption is not always correct. You may be extending a class, or often in my case, I am trying to keep examples very small, readable and to the point. So you have the option to insert a pylint declaration at the top of the file, or at a particular method declaration to ignore this pylint error. `# pylint: disable=too-few-public-methods` |
| E0110 | Abstract class '*ClassName*' with abstract methods instantiated (abstract-class-instantiated) | The Class that inherits your abstract class is not implementing all the abstract methods as described in the interfaces signature.|
| W0221 | Parameters differ from overridden '*method*' method (arguments-differ) | The arguments in your abstract class don't match the arguments in your implementing class. Check spelling of arguments.|
| C0304 | Final newline missing (missing-final-newline) | Pylint preferes a file to end with a new line. When copying code from a webpage into a `.py` file, the copied code may not finish with a new line character. You can add one manually by pressing the `enter` key on your keyboard at the end of your code, or if you use VSCode, pressing the key combination of **SHIFT-ALT-F** will auto format your `*.py` file with a final newline when you have the Pylint linter, or other linter, enabled.|
| W0612 | Unused variable | You can remove the unused variable from your code. If you cannot remove the unused variable then use a `_` as the variable name. See the section [the-underscore-only-_variable](mediator#the-underscore-only-_-variable) in the [Mediator](mediator) pattern for more information.

## Command Line Interfaces

Command Line Interfaces (CLI) on different operating systems (Windows, Linux, MacOSX, RaspberryPI) vary in appearance quite a lot.

You can use CMD, PowerShell or Git BASH on Windows, Bash on Linux or Terminal on MacOSX.

``` text
-- Windows PowerShell -- 
PS> python example.py
PS E:\python_design_patterns> python example.py

-- Windows CMD -- 
C:\> python example.py

-- Git BASH
Username@hostname MINGW64 /e/python_design_patterns
$ python example.py

-- Linux -- 
user@domain:~# python3 example.py
user@domain:$/ python3 example.py
user@domain:/python-design-patterns# python3 example.py
$ python3 example.py
# python3 example.py

-- MacOSX--
hostname:~ username$ python3 example.py
```

Wikipedia - Command-line interface : [https://en.wikipedia.org/wiki/Command-line_interface](https://en.wikipedia.org/wiki/Command-line_interface)
