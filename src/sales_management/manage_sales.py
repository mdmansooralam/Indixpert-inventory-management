from src.sales_management.sales import Sales
from src.inventory_management.inventory import Inventory
from src.product import Product
from src.utility.check_product import product_available_in_sales_record


class ManageSales(Sales):
    inventory = Inventory()
        
    def add_sale(self, id, quantity):
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
                        product.name, quantity, total, product.id
                    ))
                    self.save_sales()
                    print(f'{quantity} {product.name} has been sold successful ..')
                    break

    def get_sale_product(self, id):
        if(product_available_in_sales_record(id)):
            print(f'ID       NAME         QTY      Total')
            print(f'-------------------------------------------------')
            for product in self.all_sales:
                if(product.id == id):
                    print(f'{product.id}     {product.name}       {product.quantity}     {product.price}')
        else:
            print(f'\nNo sales record found\n')

    def get_all_sales_product(self):
        if(len(self.all_sales)>0):
            print(f'\nID      NAME        QTY         TOTAL')
            print(f'--------------------------------------------------------')
            for product in self.all_sales:
                print(f'{product.id}     {product.name}       {product.quantity}         {product.price}')
        else:
            print('No Sales Record Found')
