class CoffeeFactory:
    def createCoffee(self, coffee_type):
        if coffee_type == "Espresso":
            return Espresso()
        elif coffee_type == "Cappuccino":
            return Cappuccino()
        elif coffee_type == "Americano":
            return Americano()
        else:
            raise ValueError("Invalid coffee type")
