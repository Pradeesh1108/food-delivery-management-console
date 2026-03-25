class Restaurant:
    def __init__(self, rest_id, rest_name,location, rating):
        self.rest_id = rest_id
        self.rest_name = rest_name
        self.location = location
        self.rating = rating
        self.menu = {}
        self.pendingOrders = {}


    def addMenu(self,menuCard):
        self.menu[menuCard.menu_id] = menuCard

    def removeMenu(self, food):
        self.menu.remove(food)

    def viewPendingOrders(self):
        if not self.pendingOrders:
            print("No pending orders.")
            return
        for orderId, order in self.pendingOrders.items():
            print(order)
            print("-" * 20)
            
    def updateOrderStatus(self, orderId, newStatus):
        if orderId in self.pendingOrders:
            self.pendingOrders[orderId].status = newStatus
            return True
        return False
