from abc import ABCMeta, abstractmethod
import datetime

class AbstractComponent(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method(self):
        """A method to implement"""


class Component(AbstractComponent):
    def method(self):
        print("The method has been called")


class ProxyComponent(AbstractComponent):
    def __init__(self):
        self.component = Component()

    def method(self):
        f = open("log.txt",'a')
        f.write("%s : method was proxied\n" % (datetime.datetime.now()))
        self.component.method()


COMPONENT = Component()
COMPONENT.method()

COMPONENT = ProxyComponent()
COMPONENT.method()
