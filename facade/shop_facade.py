"""A Facade Demo"""


class Discount:
    @staticmethod
    def calc(value):
        return value * 0.9


class Shipping:
    @staticmethod
    def calc():
        return 5


class Fees:
    @staticmethod
    def calc(value):
        return value * 1.5


# facade
class ShopFacade:
    def __init__(self):
        self.discount = Discount()
        self.shipping = Shipping()
        self.fees = Fees()

    def calc_price(self, price):
        price = self.discount.calc(price)
        price = self.fees.calc(price)
        price += self.shipping.calc()
        return price


# client
SHOPFACADE = ShopFacade()
COST = SHOPFACADE.calc_price(100)
print("The Final Cost = %.2f" % COST)
