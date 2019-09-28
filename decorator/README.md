
Adapter : Converts one interface to another so that it matches what the client is expecting 
Decorator : Dynamically adds responsibility to the interface by wrapping the original code 
Facade : Provides a simplified interface 


## Decorator Design Pattern

The decorator pattern is a structural pattern, that allows you to attach additional responsibilites to an object at run time.

The decorator pattern is used in both the Object Oriented and Functional paradigms.

The decorator pattern is different than the Python language feature of Python Decorators in it's syntax, but the the application of it is the same, in the way that it is essentially a wrapper.

The Decorator pattern adds extensibility, without modifying the original function. 


Dynamically adds responsibility to the interface by wrapping the original code


An example of this is adding butter to a slice of bread, 
and then you can also add jam.


motivation
As an example, consider a window in a windowing system. To allow scrolling of the window's contents, one may wish to add horizontal or vertical scrollbars to it, as appropriate. Assume windows are represented by instances of the Window interface, and assume this class has no functionality for adding scrollbars. One could create a subclass ScrollingWindow that provides them, or create a ScrollingWindowDecorator that adds this functionality to existing Window objects. At this point, either solution would be fine. 
Now, assume one also desires the ability to add borders to windows. Again, the original Window class has no support. The ScrollingWindow subclass now poses a problem, because it has effectively created a new kind of window. If one wishes to add border support to many but not all windows, one must create subclasses WindowWithBorder and ScrollingWindowWithBorder etc. This problem gets worse with every new feature or window subtype to be added. For the decorator solution, we simply create a new BorderedWindowDecorator—at runtime, we can decorate existing windows with the ScrollingWindowDecorator or the BorderedWindowDecorator or both, as we see fit. Notice that if the functionality needs to be added to all Windows, you could modify the base class and that will do. On the other hand, sometimes (e.g., using external frameworks) it is not possible, legal, or convenient to modify the base class. 
Note, in the previous example, that the "SimpleWindow" and "WindowDecorator" classes implement the "Window" interface, which defines the "draw()" method and the "getDescription()" method, that are required in this scenario, in order to decorate a window control. 
from https://en.wikipedia.org/wiki/Decorator_pattern
