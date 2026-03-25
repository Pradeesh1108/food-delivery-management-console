class restaurantRepo:
    def __init__(self):
        self.restaurants = {}

    def addRestaurant(self, restaurant):
        self.restaurants[restaurant.rest_id] = restaurant

    def displayRestaurants(self):
        for rest_id, rest in self.restaurants.items():
            print(rest_id, "--->", rest.rest_name)
