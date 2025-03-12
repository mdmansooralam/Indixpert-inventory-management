from src.sales_management.sales import Sales
from src.inventory_management.inventory import Inventory
from src.user_management.user_state import UserState


def product_available_in_inventory(id):
    products = Inventory().products
    user = UserState().get_state()
    if(user.role == 'ADMIN'):
        for pd in products:
            if(pd.id == id):
                return True
  
    if(user.role == 'USER'):
        for pd in products:
            if(pd.id == id and pd.added_by == user.username):
                return True
            

def product_available_in_sales_record(id):
    sales = Sales().all_sales
    user = UserState().get_state()
    if(user.role == 'ADMIN'):
        for sale in sales:
            if(sale.id == id):
                return True
            
    if(user.role == 'USER'):
        for sale in sales:
            if(sale.id == id and sale.added_by == user.username):
                return True
        
