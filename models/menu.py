class Menu:
    def __init__(self, menu_id, menuName):
        self.menu_id = menu_id
        self.menuName = menuName
        self.itemList = {}

    def addItem(self,item):
        if item.item_id not in self.itemList:
            self.itemList[item.item_id] = item

    def displayItem(self):
        for key, value in self.itemList.items():
            print(key,"-->", value.name, "-->", value.price)

