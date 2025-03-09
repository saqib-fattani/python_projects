# Create a class called Order which stores items & its price.
# Use Dunder function __gt__() to convey that:
#          order1 > order2 if the price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price
    
odr1 = Order("Biscuit", 50)
odr2 = Order("Chips", 30)

print(odr1.__gt__(odr2))

odr3 = Order("Bread", 100)

print(odr2.__gt__(odr3))
