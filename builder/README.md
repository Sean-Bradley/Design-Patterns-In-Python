# Builder Design Pattern

The intent of the Builder design pattern is to separate the construction of a complex object from its representation. By doing so the same construction process can create different representations

The Builder Pattern tries to solve,
- How can a class (the same construction process) create different
representations of a complex object?
- How can a class that includes creating a complex object be simplified?

Parts of the Builder Pattern
1. **Product** - The Product being built
2. **Concrete Builder** - Build the concrete product. Implemets the IBuilder interface
3. **Builder Inteface** - The Interface which the Concrete builder should implement
4. **Director** - Has a construct method which when called creates a custom type of product

![Builder Pattern Overiew](builder.png)

The Builder Pattern in the context of a House Builder. There are multiple directors creating there own complex objects

![Builder Pattern in Context](house_builder.png). 
