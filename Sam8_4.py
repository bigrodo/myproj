class Smartphone:
    def __init__(self, brand, model, price):
        self._brand = brand
        self._model = model
        self.__price = price

    def use(self):
        print(f"I'm currently using an {self._model} by {self._brand} which i bought for {self.__price}")

my_smartphone = Smartphone("Apple", "iPhone 11", "65000")
print(my_smartphone._brand)
my_smartphone.use()