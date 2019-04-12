# Factory Design Pattern

The Factory Pattern is a creational pattern that defines an Interface for creating an object and defers instantiation until runtime.

Used when you don't know how many or what type of objects will be needed until or during runtime

![Factory Pattern Overview](factory_pattern.png)

The Factory Pattern in the context of a Chair Factory
![Factory Pattern In Context](factory_pattern_chair.png)

```python
class ObjectFactory:  
    """Tha Factory Class"""

    @staticmethod
    def get_concrete_object(object_type):
        """A static method to get a concrete object of type class"""
        try:
            if object_type == "ObjectA":
                return ObjectA()
            if object_type == "ObjectB":
                return ObjectB()
            if object_type == "ObjectC":
                return ObjectC()
            raise AssertionError("Object Not Found")
        except AssertionError as _e:
            print(_e)
        return None
```

Each Object implements a Common Interface
```python
class ObjectA(IObjectType):  
    """The Object Concrete Class which implements the IObjectType interface"""

    ...
```

Request from the factory at run time
```python
if __name__ == "__main__":
    MY_OBJECT = ObjectFactory().get_concrete_object("ObjectB")
    print(MY_OBJECT.dimensions())
```

## Video Tututorial Of the Factory Pattern in python

[![Video Tututorial Of the Factory Pattern in python](https://img.youtube.com/vi/04J_fL5zg3U/0.jpg)](https://youtu.be/04J_fL5zg3U)