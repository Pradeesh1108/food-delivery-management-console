from models.user import User

class deliveryPerson(User):
    def __init__(self, user_id, user_name, phone,address, email, location, availabilityStatus):
        super().__init__(user_id, user_name, phone,address, email, location)
        self.deliveryPersonId = user_id
        self.deliveryPersonName = user_name
        self.phone = phone
        self.address = address
        self.email = email
        self.location = location
        self.availabilityStatus = availabilityStatus

    def acceptOrder(self, order):
        order.deliveryPersonId = self.deliveryPersonId
        order.status = "Picked Up"
        self.availabilityStatus = "Busy"
        print(f"[{self.deliveryPersonName}] Accepted order {order.order_id}")

    def deliveryOrder(self, order):
        order.status = "Delivered"
        self.availabilityStatus = "Available"
        print(f"[{self.deliveryPersonName}] Delivered order {order.order_id}")

    def updateStatus(self, status):
        self.availabilityStatus = status