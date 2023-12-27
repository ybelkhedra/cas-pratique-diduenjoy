class Item:
    def __init__(self, item_id, name=None, price=None, ref=None, warranty=None, duration=None):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.ref = ref
        self.warranty = warranty
        self.duration = duration
    
    def getId(self):
        return self.item_id

    def __getitem__(self, label):
        return self.__dict__[label]
    
    def __setitem__(self, label, value):
        self.__dict__[label] = value
    
    def update_by_label(self, label, value):
        self.__dict__[label] = value

    def __str__(self):
        return f"Item ID : {self.item_id}, Name : {self.name}, Price : {self.price}, Ref : {self.ref}, Warranty : {self.warranty}, Duration : {self.duration}"