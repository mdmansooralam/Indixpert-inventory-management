from src.sales_management.manage_sales import ManageSales
from src.utility.validation import *
from src.utility.check_product import product_available_in_inventory

class SalesFeatures(ManageSales):

    def sale_product(self):
        try:
            id = id_validate(input('Enter product id.. : '))
            if(not id):
                raise Exception('Enter a valid Id and should be 4 charecter')
    
            if(not product_available_in_inventory(id)):
                raise Exception('Product not exist ')
            
            quantity = quantity_validate(input('Quantity : '))
            if(not quantity):
                raise Exception('Enter a valid Id and should be 4 charecter')

            self.add_sale(id, quantity) 

        except Exception as error:
            print(error)

    def serach_sales_product(self):
        try:
            id = id_validate(input('Enter Product Id : '))
            if(not id):
                raise Exception('Enter a valid Id and should be 4 charecter')
            
            self.get_sale_product(id)

        except Exception as error:
            print(error)

    def display_all_sales_product(self):
        try:
            self.get_all_sales_product()
        except Exception as error:
            print(error)
