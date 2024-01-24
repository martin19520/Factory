class Coffee:
    def grindCoffee(self):
        pass

    def makeCoffee(self):
        pass

    def pourIntoCup(self):
        pass


class Espresso(Coffee):
    def grindCoffee(self):
        print("Grinding coffee beans for Espresso")

    def makeCoffee(self):
        print("Making Espresso")

    def pourIntoCup(self):
        print("Pouring Espresso into the cup")


class Cappuccino(Coffee):
    def grindCoffee(self):
        print("Grinding coffee beans for Cappuccino")

    def makeCoffee(self):
        print("Making Cappuccino")

    def pourIntoCup(self):
        print("Pouring Cappuccino into the cup")


class Americano(Coffee):
    def grindCoffee(self):
        print("Grinding coffee beans for Americano")

    def makeCoffee(self):
        print("Making Americano")

    def pourIntoCup(self):
        print("Pouring Americano into the cup")
