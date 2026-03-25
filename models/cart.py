class Cart:
    def __init__(self):
        self.currentCart = {}
        self.totalAmount = 0

    def addItemToCart(self, item):
        self.currentCart[item.item_id] = item

    def calculateTotal(self):
        self.totalAmount = 0
        for item_id, item in self.currentCart.items():
            self.totalAmount += item.price
        return self.totalAmount

    def __str__(self):
        items = [item.name for item in self.currentCart.values()]
        return f"Items: {', '.join(items)} | Total: {self.totalAmount}"
