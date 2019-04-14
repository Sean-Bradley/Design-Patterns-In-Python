# Chain of Responsibility Design Pattern

Chain of responsibility pattern is a behavioral pattern used to achieve loose coupling
in software design.
Example, a request from a client is passed to a chain of objects to process them. 
The objects in the chain will decide themselves how the request is handled and/or 
passed to the next processor in the chain.

![Chain of Responsibility UML Diagram in the context of an ATM](atm.png)

```bash
$ python atm.py
Enter amount to withdrawal
130
Dispensing 2 £50 note
Dispensing 1 £20 note
Dispensing 1 £10 note
```