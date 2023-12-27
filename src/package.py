from src.item import Item

class Package:
    def __init__(self, package_id, order_id=None):
        self.package_id = package_id
        self.order_id = order_id
        self.items = []

    def getId(self):
        return self.package_id
    
    def add_item(self, item):
        self.items.append(item)
    
    def hasItem(self, item_id):
        for item in self.items:
            if item.getId() == item_id:
                return True
        return False
    
    def get_item_by_id(self, item_id):
        for item in self.items:
            if item.getId() == item_id:
                return item
        return None
    
    def __getitem__(self, item_id):
        return self.get_item_by_id(item_id)

    def __str__(self):
        return f"Package ID : {self.package_id}, Order ID : {self.order_id}, Items : {self.items}"

    def print_items(self):
        for item in self.items:
            print(item)