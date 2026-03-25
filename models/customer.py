from models.user import User

class customer(User):
    
    def __init__(self,user_id, user_name, phone, email, location,address):
        super().__init__(user_id, user_name, phone, email, location)
        self.address = address
        self.orders = []
        self.cart = []
