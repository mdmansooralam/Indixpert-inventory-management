from src.sales_management.sales import Sales
from src.inventory_management.inventory import Inventory


def product_available_in_inventory(id):
    products = Inventory().products
    for pd in products:
        if(pd.id == id):
            return True
    else:
        return False

def product_available_in_sales_record(id):
    sales = Sales().all_sales
    for sale in sales:
        if(sale.id == id):
            return True
    else:
        return False
    
