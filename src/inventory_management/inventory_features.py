from src.utility.validation import *
from src.utility.check_product import product_available_in_inventory
from src.inventory_management.manage_inventory import ManageInventory

class InventoryFeatures(ManageInventory):
    
    def add(self):
        try:
            name = name_validate(input("Product Name : "))
            if(not name):
                raise Exception('Enter a valide name and should be start with alphabet')
            
            price = price_validate(input('Price : '))
            if(not price):
                raise Exception('Enter valid price should be greater than 0')
            
            quantity = quantity_validate(input("Quantity : "))
            if(not quantity):
                raise Exception('Enter valid quantity should be greater than 0')
            
            self.add_product(name, quantity, price)

        except Exception as error:
            print(error)

    def update(self):
        try:
            id = id_validate(input('enter product id : '))
            if(not id):
                raise Exception('Enter a valid Id and should be 4 charecter')

            if(not product_available_in_inventory(id)):
                raise Exception('product not exist')
            
            name = name_validate(input('enter product name : '))
            if(not name):
                raise Exception('Enter a valide name and should be start with alphabet')
            
            quantity = quantity_validate(input('enter product quantity : '))
            if(not quantity):
                raise Exception('Enter valid quantity should be greater than 0')
            
            price = price_validate(input('enter product price : '))
            if(not price):
                raise Exception('Enter valid price should be greater than 0')

            self.update_product(id, name, quantity, price)

        except Exception as error:
            print(error)

    def delete(self):
        try:
            id = id_validate(input('Product Id : '))
            if(not id):
                raise Exception('Enter a valid Id and should be 4 charecter')
            
            self.delete_product(id)
        except Exception as error:
            print(error)
    
    def restock(self):
        try:

            id = id_validate(input('Product Id : '))
            if(not id):
                raise Exception('Enter a valid Id and should be 4 charecter')
            
            if(not product_available_in_inventory(id)):
                raise Exception('product not exist')

            quantity = quantity_validate(input("Product quantity : "))
            if(not quantity):
                raise Exception('Enter a valid Id and should be 4 charecter')
            
            self.add_stock(id, quantity)
        except Exception as error:
            print(error)

    def search(self):
        try:

            id = check_blank(input('Enter Product Id / Name : '))
            if(not id):
                raise Exception('Enter a valid Id and should be 4 charecter')
            
            self.search_product(id)
        except Exception as error:
            print(error)

    def display_all_products(self):
        try:
            self.get_all_products()
        except Exception as error:
            print(error)
        

        