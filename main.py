from datetime import datetime

from models.order import Order
from models.user import User
from models.restaurant import Restaurant
from models.deliveryPerson import deliveryPerson
from models.item import Item
from models.menu import Menu
from models.cart import Cart



from repository.user_repo import userRepo
from repository.restaurant_repo import restaurantRepo
from repository.delivery_person_repo import deliveryPersonRepo
from repository.item_repo import itemRepo
from controllers.customerController import CustomerController
from controllers.restaurantController import RestaurantController
from controllers.deliveryPersonController import DeliveryPersonController


userRepository = userRepo()
restaurantRepository = restaurantRepo()
deliveryPersonRepository = deliveryPersonRepo()
itemRepository = itemRepo()


customer_ctrl = CustomerController(userRepository, restaurantRepository)
restaurant_ctrl = RestaurantController(restaurantRepository)
delivery_ctrl = DeliveryPersonController(deliveryPersonRepository, restaurantRepository)

# itemRepository.addItem(Item(1, "Tandoori", 200))
# itemRepository.addItem(Item(2, "Chicken Tikka Masala", 200))
# itemRepository.addItem(Item(3, "Alfaham", 200))
# itemRepository.addItem(Item(4, "Malai Tikka", 200))



userRepository.addUser(User(1, "Pradeesh", "7667214939", "Sri shakthi college","pradeeshkgm@gmail.com", "Coimbatore"))
userRepository.addUser(User(2, "Yashwant", "9342877060", "Ganapathy","yashwant@gmail.com", "Coimbatore"))
userRepository.addUser(User(3, "Bharath", "9999999999", "Sitra","bharath@gmail.com", "Coimbatore"))

restaurant1 = Restaurant(1,"Burooj", "Coimbatore",5)
restaurant2 = Restaurant(2, "Haryana Dhaba", "Coimbatore", 5)
restaurant3 = Restaurant(3, "Cardiff Cafe", "Peelamedu", 5)

restaurantRepository.addRestaurant(restaurant1)
restaurantRepository.addRestaurant(restaurant2)
restaurantRepository.addRestaurant(restaurant3)


menu1=Menu(1,"Starters")
menu1.addItem(Item(1, "Tandoori", 200))
menu1.addItem(Item(2, "Chicken Tikka Masala", 200))
menu1.addItem(Item(3, "Alfaham", 200))
menu1.addItem(Item(4, "Malai Tikka", 200))

restaurant1.addMenu(menu1)


# restaurant2.addMenu(Item(1, "Tandoori", 200))
# restaurant2.addMenu(Item(2, "Chicken Tikka Masala", 200))
# restaurant2.addMenu(Item(3, "Alfaham", 200))
# restaurant2.addMenu(Item(4, "Malai Tikka", 200))
#
#
# restaurant3.addMenu(Item(1, "Tandoori", 200))
# restaurant3.addMenu(Item(2, "Chicken Tikka Masala", 200))
# restaurant3.addMenu(Item(3, "Alfaham", 200))
# restaurant3.addMenu(Item(4, "Malai Tikka", 200))

deliveryPersonRepository.addDeliveryPerson(deliveryPerson(1,"Rajesh", "1234560", "Gandhi Nagar","rajesh@gmail.com","coimbatore","Available"))
deliveryPersonRepository.addDeliveryPerson(deliveryPerson(2,"Kavin", "1234560", "Gandhi Nagar","kavin@gmail.com","coimbatore","Available"))
deliveryPersonRepository.addDeliveryPerson(deliveryPerson(3,"Logesh", "1234560", "Gandhi Nagar","logesh@gmail.com","coimbatore","Available"))




while True:
    print('1. Login as Customer')
    print("2. Login as Restaurant")
    print("3. Login as Delivery Person")
    print("4. Exit")
    
    try:
        choiceValue = int(input("Enter your choice: "))
        
        if choiceValue == 1:
            customer_ctrl.handleCustomerFlow()
        elif choiceValue == 2:
            restaurant_ctrl.handleRestaurantFlow()
        elif choiceValue == 3:
            delivery_ctrl.handleDeliveryFlow()
        elif choiceValue == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
