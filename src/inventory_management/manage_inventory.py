import uuid
from src.product import Product
from src.inventory import Inventory

class ManageInventory(Inventory):

    def add_product(self, name, qty, price):
            is_product_exist = False
            try: #suggestion by nisha
                for product in self.products:
                    if(product.name == name):
                        is_product_exist = True
                        print(f'product name is already exist')
                        break
                if(not is_product_exist):
                    id = str(uuid.uuid4())[:4].upper()
                    new_product = Product(name, qty, price, id)
                    self.products.append(new_product)
                    self.save_inventory()   
                    print(f"\nItem '{name}' ID : {new_product.id} added successfully!\n")
            except TypeError: #suggetion by nisha
                print(f'invalid input please retry')

    def update_product(self, id, name, quantity, price):
        for product in self.products:
            if product.id == id:
                product.name = name
                product.quantity = quantity
                product.price = price
                self.save_inventory()
                print(f'updated product \nname : {name} \nprice : {price} \nquantity: {quantity}')
                break 
        else:
            print(f'product not found for ID : {id}')

    def delete_product(self, id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                self.save_inventory()
                print(f'{product.name} deleted successfully')
                break
        else:
            print(f'Product not found ID : {id}')

    def search_product(self, *arg):

        for product in self.products:
            if(not arg):
                print(f'please enter a valid product id or name')
                break
            else:
                if(product.id == arg[0] or product.name == arg[0]):
                    print(f'ID    Name         price     Quantity')
                    print(f'--------------------------------------------')
                    print(f'{product.id}  {product.name}       {product.price}       {product.quantity}')

                    print(f'\n\n\n')
                    
                    break
        else:
            print(f'product not found for given id or name')
            return {}

    def get_all_products(self):
            if(not self.products):
                print(f'Product record not availabe')
            else:
                print(f'ID    Name         price     Quantity')
                print(f'--------------------------------------------')
                for product in self.products:
                    print(f'{product.id}  {product.name}       {product.price}       {product.quantity}')

    def add_stock(self, id, quantity):
        for product in self.products:
            if(product.id == id):
                product.quantity += quantity
                self.save_inventory()
                print(f'stock added successful')
                break
        else:
            print(f'Product not found for ID: {id}')

