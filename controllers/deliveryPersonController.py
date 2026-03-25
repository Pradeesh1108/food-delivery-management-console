class DeliveryPersonController:
    def __init__(self, deliveryPerson_repo, restaurant_repo):
        self.deliveryPersonRepository = deliveryPerson_repo
        self.restaurantRepository = restaurant_repo

    def handleDeliveryFlow(self):
        try:
            dp_id = int(input("Enter Delivery Person ID: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if dp_id not in self.deliveryPersonRepository.deliveryPersons:
            print("Delivery Person not found!")
            return
            
        dp = self.deliveryPersonRepository.deliveryPersons[dp_id]
        
        while True:
            print("\n1. View 'Ready for Pickup' Orders")
            print("2. Accept an Order")
            print("3. Deliver an Order")
            print("4. Go back")
            try:
                addChoice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if addChoice == 1:
                found = False
                for rest in self.restaurantRepository.restaurants.values():
                    for order in rest.pendingOrders.values():
                        if order.status == "Ready for Pickup":
                            print(order)
                            print(f"Pickup from: {rest.rest_name}")
                            print("-" * 20)
                            found = True
                if not found:
                    print("No orders ready for pickup.")
                    
            elif addChoice == 2:
                try:
                    order_id = int(input("Enter Order ID to accept: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                order_found = None
                rest_found = None
                for rest in self.restaurantRepository.restaurants.values():
                    if order_id in rest.pendingOrders and rest.pendingOrders[order_id].status == "Ready for Pickup":
                        order_found = rest.pendingOrders[order_id]
                        rest_found = rest
                        break
                        
                if order_found:
                    dp.acceptOrder(order_found)
                else:
                    print("Order not found or not ready for pickup.")
                    
            elif addChoice == 3:
                try:
                    order_id = int(input("Enter Order ID to mark delivered: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                order_found = None
                for rest in self.restaurantRepository.restaurants.values():
                    if order_id in rest.pendingOrders and rest.pendingOrders[order_id].deliveryPersonId == dp_id and rest.pendingOrders[order_id].status == "Picked Up":
                        order_found = rest.pendingOrders[order_id]
                        break
                        
                if order_found:
                    dp.deliveryOrder(order_found)
                else:
                    print("Order not found or not picked up by you.")
                    
            elif addChoice == 4:
                break
