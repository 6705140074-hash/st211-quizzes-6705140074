class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        self.items.append({"name": name, "price": price})

    def total(self):
        return sum(itme["price"] for itme in self.items)

    def count(self):
        return len(self.items)