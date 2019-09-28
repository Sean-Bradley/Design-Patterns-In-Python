"""
Adapter pattern example.
"""
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

RECHARGE = ["Recharge started.", "Recharge finished."]

POWER_ADAPTERS = {"Android": "MicroUSB", "iPhone": "Lightning"}

CONNECTED = "{} connected."
CONNECT_FIRST = "Connect {} first."


class RechargeTemplate:
    __metaclass__ = ABCMeta

    @abstractmethod
    def recharge(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class FormatIPhone(RechargeTemplate):
    @abstractmethod
    def use_lightning(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class FormatAndroid(RechargeTemplate):
    @abstractmethod
    def use_micro_usb(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class IPhone(FormatIPhone):
    __name__ = "iPhone"

    def __init__(self):
        self.connector = False

    def use_lightning(self):
        self.connector = True
        print(CONNECTED.format(POWER_ADAPTERS[self.__name__]))

    def recharge(self):
        if self.connector:
            for state in RECHARGE:
                print(state)
        else:
            print(CONNECT_FIRST.format(POWER_ADAPTERS[self.__name__]))


class Android(FormatAndroid):
    __name__ = "Android"

    def __init__(self):
        self.connector = False

    def use_micro_usb(self):
        self.connector = True
        print(CONNECTED.format(POWER_ADAPTERS[self.__name__]))

    def recharge(self):
        if self.connector:
            for state in RECHARGE:
                print(state)
        else:
            print(CONNECT_FIRST.format(POWER_ADAPTERS[self.__name__]))


class IPhoneAdapter(FormatAndroid):
    def __init__(self, mobile):
        self.mobile = mobile

    def recharge(self):
        self.mobile.recharge()

    def use_micro_usb(self):
        print(CONNECTED.format(POWER_ADAPTERS["Android"]))
        self.mobile.use_lightning()


class AndroidRecharger():
    def __init__(self):
        self.phone = Android()
        self.phone.use_micro_usb()
        self.phone.recharge()


class IPhoneMicroUSBRecharger():
    def __init__(self):
        self.phone = IPhone()
        self.phone_adapter = IPhoneAdapter(self.phone)
        self.phone_adapter.use_micro_usb()
        self.phone_adapter.recharge()


class IPhoneRecharger():
    def __init__(self):
        self.phone = IPhone()
        self.phone.use_lightning()
        self.phone.recharge()


print("Recharging Android with MicroUSB recharger.")
AndroidRecharger()
print()

print("Recharging iPhone with MicroUSB using adapter pattern.")
IPhoneMicroUSBRecharger()
print()

print("Recharging iPhone with iPhone recharger.")
IPhoneRecharger()
