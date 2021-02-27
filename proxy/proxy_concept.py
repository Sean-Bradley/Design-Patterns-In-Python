# pylint: disable=too-few-public-methods
"A Proxy Concept Example"

from abc import ABCMeta, abstractmethod

class ISubject(metaclass=ABCMeta):
    "An interface implemented by both the Proxy and Real Subject"
    @staticmethod
    @abstractmethod
    def request():
        "A method to implement"

class RealSubject(ISubject):
    "The actual real object that the proxy is representing"

    def __init__(self):
        # hypothetically enormous amounts of data
        self.enormous_data = [1, 2, 3]

    def request(self):
        return self.enormous_data

class Proxy(ISubject):
    """
    The proxy. In this case the proxy will act as a cache for
    `enormous_data` and only populate the enormous_data when it
    is actually necessary
    """

    def __init__(self):
        self.enormous_data = []
        self.real_subject = RealSubject()

    def request(self):
        """
        Using the proxy as a cache, and loading data into it only if
        it is needed
        """
        if self.enormous_data == []:
            print("pulling data from RealSubject")
            self.enormous_data = self.real_subject.request()
            return self.enormous_data
        print("pulling data from Proxy cache")
        return self.enormous_data

# The Client
SUBJECT = Proxy()
# use SUBJECT
print(id(SUBJECT))
# load the enormous amounts of data because now we want to show it.
print(SUBJECT.request())
# show the data again, but this time it retrieves it from the local cache
print(SUBJECT.request())