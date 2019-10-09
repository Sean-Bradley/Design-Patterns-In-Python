# Proxy Design Pattern

The proxy design pattern, in it's most basic form, is a class functioning as an interface to something else.
A proxy could be for anything, such as a network connection, an object in memory, a file, or anything else that you man want to provide an abstraction between.
It is a wrapper called by a client to access the real underlying object.
Addition functionality can be provided at in the proxy abstraction if required.
eg, caching, authorisation, validation, lazy initialization, logging.

Use if you want to control access to the object, or add additional functionality without modifying the original object.

The proxy should implement the subject interface as much as practicable so that the proxy and subject appear identical to the client.

THe Proxy Pattern may occasionally be referred to as Monkey Patching or Object Augmentation


