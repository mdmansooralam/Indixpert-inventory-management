from src.sales_management.sales import Sales
from src.inventory_management.inventory import Inventory
from src.product import Product
from src.utility.check_product import product_available_in_sales_record
from src.user_management.user_state import UserState


class ManageSales(Sales):
    inventory = Inventory()
        
    def add_sale(self, id, quantity):
        user = UserState().get_state()
        if(user):
            if(user.role == 'ADMIN'):
                for product in self.inventory.products:
                    if(product.id == id):
                        if(quantity > product.quantity):
                            print(f'Only {product.quantity} {product.name} is  available')
                            break
                        else:
                            product.quantity -= quantity
                            self.inventory.save_inventory()
                            total = product.price * quantity
                            self.all_sales.append(Product(
                                product.name, quantity, total, product.id, product.added_by
                            ))
                            self.save_sales()
                            print(f'{quantity} {product.name} has been sold successful ..')
                            break
            elif(user.role == 'USER'):
                for product in self.inventory.products:
                    if(product.id == id and product.added_by == user.username):
                        if(quantity > product.quantity):
                            print(f'Only {product.quantity} {product.name} is  available')
                            break
                        else:
                            product.quantity -= quantity
                            self.inventory.save_inventory()
                            total = product.price * quantity
                            self.all_sales.append(Product(
                                product.name, quantity, total, product.id, product.added_by
                            ))
                            self.save_sales()
                            print(f'{quantity} {product.name} has been sold successful ..')
                            break
        if(not user):
            print('user not found')


    def get_sale_product(self, id):
        user = UserState().get_state()
        if(user.role == 'ADMIN'):
            print('{:<10}{:<15}{:<10}{:<10}{:<10}'.format('ID','PRODUCT NAME', 'QTY.', 'TOTAL', 'SALE BY'))
            print('-'*55)
            for product in self.all_sales:
                if(product.id == id):
                    print('{:<10}{:<15}{:<10}{:<10}{:<10}'.format(product.id, product.name, product.quantity, product.price, product.added_by))
                    break
            else:
                print(f'\nNo sales record found')
        elif(user.role == 'USER'):
            print('{:<10}{:<15}{:<10}{:<10}'.format('ID','PRODUCT NAME', 'QTY.', 'TOTAL'))
            print('-'*45)
            for product in self.all_sales:
                if(product.id == id and product.added_by == user.username):
                    print('{:<10}{:<15}{:<10}{:<10}'.format(product.id, product.name, product.quantity, product.price))
                    break
            else:
                print('\nNo sales record found')
            

    def get_all_sales_product(self):
        user = UserState().get_state()
        if(user.role == 'ADMIN'):
            if(len(self.all_sales)>0):
                print('{:<10}{:<15}{:<10}{:<10}{:<10}'.format('ID','PRODUCT NAME', 'QTY.', 'TOTAL', 'SALE BY'))
                print('-'*55)
                for product in self.all_sales:
                    print('{:<10}{:<15}{:<10}{:<10}{:<10}'.format(product.id, product.name, product.quantity, product.price, product.added_by))
            else:
                print('No Sales Record Found')
        elif(user.role == 'USER'):
                product_found = False
                print('{:<10}{:<15}{:<10}{:<10}'.format('ID','PRODUCT NAME', 'QTY.', 'TOTAL'))
                print('-'*45)
                for product in self.all_sales:
                    if(product.added_by == user.username):
                        product_found = True
                        print('{:<10}{:<15}{:<10}{:<10}'.format(product.id, product.name, product.quantity, product.price))
                else:
                    if(product_found):
                        print('\nFinish ..........')
                    else:
                        print("product not found")
            


