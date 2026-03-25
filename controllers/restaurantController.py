class RestaurantController:
    def __init__(self, restaurant_repo):
        self.restaurantRepository = restaurant_repo

    def handleRestaurantFlow(self):
        try:
            restId = int(input("Enter Restaurant id: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if restId not in self.restaurantRepository.restaurants:
            print("Restaurant not found!")
            return
            
        restaurant = self.restaurantRepository.restaurants[restId]
        
        while True:
            print("\n1. View Orders")
            print("2. Update Order Status")
            print("3. Go back")
            try:
                addChoice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            if addChoice == 1:
                restaurant.viewPendingOrders()
            elif addChoice == 2:
                try:
                    order_id = int(input("Enter Order ID to update: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                if order_id in restaurant.pendingOrders:
                    print("1. Accept Order")
                    print("2. Reject Order")
                    print("3. Mark Ready for Pickup")
                    try:
                        status_choice = int(input("Select new status: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue
                    
                    if status_choice == 1:
                        restaurant.updateOrderStatus(order_id, "Accepted")
                    elif status_choice == 2:
                        restaurant.updateOrderStatus(order_id, "Rejected")
                    elif status_choice == 3:
                        restaurant.updateOrderStatus(order_id, "Ready for Pickup")
                    else:
                        print("Invalid choice")
                        continue
                    print(f"Order {order_id} status updated!")
                else:
                    print("Order ID not found.")
            elif addChoice == 3:
                break
