class Product:
    def __init__(self,price):
        self.price = price
    
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price Cannot be Negative")
        self.__price = value

product = Product(-10)
print(product.price)


#property is an object that sits in front of an attribute and allows us to get or set the value of an attribute