import uuid
from src.product import Product
from src.inventory_management.inventory import Inventory
from src.user_management.user_state import UserState

class ManageInventory(Inventory):

    def add_product(self, name, qty, price):
            is_product_exist = False
            for product in self.products:
                if(product.name == name):
                    is_product_exist = True
                    print(f'product name is already exist')
                    break
            if(not is_product_exist):
                id = str(uuid.uuid4())[:4].upper()
                username = UserState().get_state().username
                new_product = Product(name, qty, price, id, username)
                self.products.append(new_product)
                self.save_inventory()   
                print(f"\nItem '{name}' ID : {new_product.id} added successfully!\n")

    def update_product(self, id, name, quantity, price):
        user = UserState().get_state()
        if(user.role == 'ADMIN'):
            for product in self.products:
                if(product.id == id):
                    product.name = name
                    product.quantity = quantity
                    product.price = price
                    self.save_inventory()
                    print(f'updated product \nname : {name} \nprice : {price} \nquantity: {quantity}')
                    break 
            else:
                print(f'product not found for ID : {id}')
        elif(user.role == 'USER'):
            for product in self.products:
                if(product.id == id and product.added_by == user.username):
                    product.name = name
                    product.quantity = quantity
                    product.price = price
                    self.save_inventory()
                    print(f'updated product \nname : {name} \nprice : {price} \nquantity: {quantity}')
                    break 
            else:
                print(f'product not found for ID : {id}')

    def delete_product(self, id):
        user = UserState().get_state()
        if(user.role == 'ADMIN'):
            for product in self.products:
                if product.id == id:
                    self.products.remove(product)
                    self.save_inventory()
                    print(f'{product.name} deleted successfully')
                    break
            else:
                print(f'Product not found ID : {id}')

        elif(user.role == 'USER'):
            for product in self.products:
                if(product.id == id and product.added_by == user.username):
                    self.products.remove(product)
                    self.save_inventory()
                    print(f'{product.name} deleted successfully')
                    break
            else:
                print(f'Product not found ID : {id}')
                    
    def search_product(self, *arg):
        user = UserState().get_state()
        if(user.role == 'ADMIN'):
            print('{:<10}{:<15}{:<10}{:<10}{:<10}'.format('ID', 'NAME', 'PRICE', 'QUANTITY', 'ADDED BY'))
            print('-'*55)
            product_found = False
            for product in self.products:
                if(product.id == arg[0] or product.name.startswith(arg[0])):
                    product_found = True
                    print('{:<10}{:<15}{:<10}{:<10}{:<10}'.format(product.id,product.name,product.price,product.quantity, user.username))
            else:
                if(not product_found):
                    print('\nProduct not found')
                else:
                    print('\nFinish.....')
        elif(user.role == 'USER'):
            print('{:<10}{:<15}{:<10}{:<10}'.format('ID', 'NAME', 'PRICE', 'QUANTITY'))
            print('-'*45)
            product_found = False
            for product in self.products:
                if(product.id == arg[0] or product.name.startswith(arg[0])):
                    if(product.added_by == user.username):
                        product_found = True
                        print('{:<10}{:<15}{:<10}{:<10}'.format(product.id,product.name,product.price,product.quantity))
            else:
                if(not product_found):
                    print('\nproduct not found')
                else:
                    print('\nFinish....')

    def get_all_products(self):
            user = UserState().get_state()
            if(user.role == 'ADMIN'):
                print('{:<10}{:<15}{:<10}{:<10}{:<10}'.format('ID', 'NAME', 'PRICE', 'QUANTITY', 'ADDED BY'))
                print('-'*55)
                if(not self.products):
                    print(f'\nProduct record not availabe')
                else:
                    for product in self.products:
                        print('{:<10}{:<15}{:<10}{:<10}{:<10}'.format(product.id,product.name,product.price,product.quantity, product.added_by))


            elif(user.role == 'USER'):
                print('{:<10}{:<15}{:<10}{:<10}'.format('ID', 'NAME', 'PRICE', 'QUANTITY'))
                print('-'*45)
                product_found = False
                for product in self.products:
                    if(product.added_by == user.username):
                        product_found = True
                        print('{:<10}{:<15}{:<10}{:<10}'.format(product.id, product.name, product.price, product.quantity))
                else:
                    if(product_found):
                        print('\nFinish....')
                    else:
                        print('\nProduct not found..')

    def add_stock(self, id, quantity):
        user = UserState().get_state()
        if(user):
            if(user.role == 'ADMIN'):
                for product in self.products:
                    if(product.id == id):
                        product.quantity += quantity
                        self.save_inventory()
                        print(f'stock added successful')
                        break
                else:
                    print(f'Product not found for ID: {id}')
            elif(user.role == 'USER'):
                for product in self.products:
                    if(product.id == id and product.added_by == user.username):
                        product.quantity += quantity
                        self.save_inventory()
                        print('stock added successful')
                        break
                else:
                    print('product not found ')

