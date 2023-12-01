class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def use(self):
        print(f"I'm currently using an {self.model} by {self.brand} which i bought for {self.price}")

class BOsmartphone(Smartphone):
    def __init__(self, brand, model, price, term_of_use):
        super().__init__(brand, model, price)
        self.term_of_use = term_of_use

    def sell(self):
        print(f"I sell my {self.model} from {self.brand}, which i have been using for {self.term_of_use} for {self.price}")

my_smartphone = BOsmartphone("Apple", "iPhone 11", "65000", "3 years")
my_smartphone.use()
my_smartphone.sell()

