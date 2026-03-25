from datetime import datetime
from models.order import Order
from models.cart import Cart

class CustomerController:
    def __init__(self, user_repo, restaurant_repo):
        self.userRepository = user_repo
        self.restaurantRepository = restaurant_repo
        self.order_counter = 1

    def handleCustomerFlow(self):
        try:
            userId = int(input("Enter your UserId: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if userId not in self.userRepository.users:
            print("User not found!")
            return

        print("-" * 33)
        print("1. View Restaurants")
        print("2. View My Orders")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        print("-" * 33)
        
        if choice == 1:
            self.restaurantRepository.displayRestaurants()
            print("-" * 33)
            try:
                restId = int(input("Enter Restaurant Id to display menu: "))
                restaurant = self.restaurantRepository.restaurants[restId]
                menu_id = list(restaurant.menu.keys())[0]
                menu = restaurant.menu[menu_id]
                menu.displayItem()
            except ValueError:
                print("Invalid input. Please enter a number.")
                return

            if restId not in self.restaurantRepository.restaurants:
                print("Restaurant not found!")
                return
                
            
            if not restaurant.menu:
                print("Menu is empty")
                return
            
            currCart = Cart()
            print("-" * 33)
            while True:
                print("1. Add Items to Cart")
                print("2. Place Order")
                print("3. Exit Menu")

                try:
                    addChoice = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                if addChoice == 1:
                    menu.displayItem()
                    print("Please enter the ID(s) of the items you want to add to cart (space separated): ")
                    try:
                        itemlist = list(map(int, input().split()))
                        for item_id in itemlist:
                            if item_id in menu.itemList:
                                currCart.addItemToCart(menu.itemList[item_id])
                            else:
                                print(f"Item {item_id} not found.")
                        print(f"Current Cart Total: {currCart.calculateTotal()}")
                    except ValueError:
                        print("Invalid input.")

                elif addChoice == 2:
                    if currCart.calculateTotal() == 0:
                        print("Cart looks empty")
                    else:
                        currOrder = Order(self.order_counter, currCart, userId, restId, currCart.calculateTotal(), "Pending", datetime.now())
                        restaurant.pendingOrders[self.order_counter] = currOrder
                        print("Order Placed Successfully!")
                        print(currOrder)
                        self.order_counter += 1
                        break
                elif addChoice == 3:
                    break
                    
        elif choice == 2:
            found = False
            for rest in self.restaurantRepository.restaurants.values():
                for order in rest.pendingOrders.values():
                    if order.customer_id == userId:
                        print(order)
                        print("-" * 20)
                        found = True
            if not found:
                print("No orders found.")
