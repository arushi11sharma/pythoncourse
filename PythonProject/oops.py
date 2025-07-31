class Vegetables:
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour

    def printNameAndPrice(self):
        print(self.name, self.price)

tomato = Vegetables("tomato", 20, "red")
tomato.printNameAndPrice()

onion = Vegetables("onion", 20, "purple")
onion.printNameAndPrice()