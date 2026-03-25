class Order:
    def __init__(self, order_id, cart, customer_id, rest_id, totalAmount, status, orderTime):
        self.order_id = order_id
        self.cart = cart
        self.customer_id = customer_id
        self.rest_id = rest_id
        self.totalAmount = totalAmount
        self.status = status
        self.orderTime = orderTime
        self.deliveryPersonId = None

    def __str__(self):
        return (f"Order ID: {self.order_id} | Status: {self.status} | Time: {self.orderTime.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"  {self.cart}")
