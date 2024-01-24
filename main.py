if __name__ == "__main__":
    # Пример за поръчка на кафе
    coffee_factory = CoffeeFactory()

    # Поръчване на Espresso
    espresso = coffee_factory.createCoffee("Espresso")
    espresso.grindCoffee()
    espresso.makeCoffee()
    espresso.pourIntoCup()

    # Поръчване на Cappuccino
    cappuccino = coffee_factory.createCoffee("Cappuccino")
    cappuccino.grindCoffee()
    cappuccino.makeCoffee()
    cappuccino.pourIntoCup()

    # Поръчване на Americano
    americano = coffee_factory.createCoffee("Americano")
    americano.grindCoffee()
    americano.makeCoffee()
    americano.pourIntoCup()
