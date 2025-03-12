class Product:
    def __init__(self, name, quantity, price, id, added_by):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id = id
        self.added_by = added_by
        
    def __str__(self):
        return {"name":{self.name}, "price":{self.price}, "id":{self.id}, "quantity":{self.quantity}, "added_by":{self.added_by}}