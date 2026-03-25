class itemRepo:
    def __init__(self):
        self.items = {}

    def addItem(self,item):
        self.items[item.item_id] = item