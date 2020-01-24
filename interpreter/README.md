terminal or a non-terminal expression

terminal means the terminated command.
non-termainl commands are the same as the composite commands
composite, can be reordered in hierachy like files and folders in a filesystem

best example is here
https://www.baeldung.com/java-interpreter-pattern
it uses a select sql statement as example

the terminal expression is the final result
the non-terminal expressionsa are the sub expressions
select [list] ffrom [list] where [list] = [list]

You want to create your own compiler
compiles stuff

Each abstract base class of the interpreter defines the interpret() method, and each concrete class inheriting from the base class implements the interpret() method, which translates the specific part of the language required at the moment.


Context 
AbstractExpression 
    interpret
Concretclasses(AbstractExpression)
    interpret

Roman numeral converter
converts roman numerals to int