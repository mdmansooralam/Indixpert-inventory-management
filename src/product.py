class Product:
    def __init__(self, name, quantity, price, id):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id = id
        
    def __str__(self):
        # return f'name:{self.name}, price:{self.price}, quantity:{self.quantity} id:{self.id}'
        return {"name":{self.name}, "price":{self.price}, "id":{self.id}, "quantity":{self.quantity}}