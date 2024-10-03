from src.inventory_management.inventory_features import InventoryFeatures
from src.sales_management.sales_features import SalesFeatures
from src.utility.ask_for_dashboard import ask_for_dashboard





def user_dashboard():
    inventory = InventoryFeatures()
    sale = SalesFeatures()
    while True:
        print(f'\n***********************Inventory Management System*********************')
        print(f'-----------------------------------------------------------------------')
        print(f'1 ADD PRODUCT')
        print(f'2 UPDATE PRODUCT')
        print(f'3 DELETE PRODUCT')
        print(f'4 SEARCH PRODUCT')
        print(f'5 VIEW ALL PRODUCTS')
        print(f'6 ADD STOCK')
        print(f'7 SALE PRODUCT')
        print(f'8 SEARCH SALE PRODUCT')
        print(f'9 VIEW ALL SALES PRODUCT')
        print(f'10 LOGOUT')
        print(f'********************************************************************\n')

        choice = input('Please Chooose Any Option : ')
        if(choice == '1'):
            inventory.add()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == '2'):
            inventory.update()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == '3'):
            inventory.delete()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == '4'):
            inventory.search()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == '5'):
            inventory.display_all_products()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == '6'):
            inventory.restock()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == '7'):
            sale.sale_product()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == '8'):
            sale.serach_sales_product()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == '9'):
            sale.display_all_sales_product()
            if(ask_for_dashboard()):
                continue
            else:
                break
        elif(choice == '10'):
            break
            

        else:
            print("Please choose a valid option")