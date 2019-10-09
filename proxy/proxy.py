"""
Proxy pattern example.
"""
from abc import ABCMeta, abstractmethod


NOT_IMPLEMENTED = "You should implement this."


class AbstractCar:
    __metaclass__ = ABCMeta

    @abstractmethod
    def drive(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Car(AbstractCar):
    def drive(self):
        print("Car has been driven!")


class Driver(object):
    def __init__(self, age):
        self.age = age


class ProxyCar(AbstractCar):
    def __init__(self, driver):
        self.car = Car()
        self.driver = driver

    def drive(self):
        if self.driver.age <= 16:
            print("Sorry, the driver is too young to drive.")
        else:
            self.car.drive()


driver = Driver(16)
car = ProxyCar(driver)
car.drive()

driver = Driver(25)
car = ProxyCar(driver)
car.drive()
