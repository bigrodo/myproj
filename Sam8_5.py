class Juice:
    def drink(self):
        return "Wow, its very tasty!"

class Water:
    def drink(self):
        return "It's not as delicious as juice"

def drink_drinks(drink):
        return drink.drink()

drink_juice = Juice()
drink_water = Water()

print(drink_drinks(drink_juice))
print(drink_drinks(drink_water))