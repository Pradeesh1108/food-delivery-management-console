class deliveryPersonRepo:
    def __init__(self):
        self.deliveryPersons = {}

    def addDeliveryPerson(self, deliveryPerson):
        self.deliveryPersons[deliveryPerson.deliveryPersonId] = deliveryPerson
