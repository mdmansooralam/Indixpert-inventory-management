from src.inventory_management.inventory_features import InventoryFeatures
from src.sales_management.sales_features import SalesFeatures


def inventory_menu():
    inventory = InventoryFeatures()
    sale = SalesFeatures()
    while True:
        print(f'\n\n***********************Inventory Management System*********************')
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
            continue
        elif(choice == '2'):
            inventory.update()
            continue
        elif(choice == '3'):
            inventory.delete()
            continue
        elif(choice == '4'):
            inventory.search()
            continue
        elif(choice == '5'):
            inventory.display_all_products()
            continue
        elif(choice == '6'):
            inventory.restock()
            continue

        elif(choice == '7'):
            sale.sale_product()
            continue
        elif(choice == '8'):
            sale.serach_sales_product()
            continue
        elif(choice == '9'):
            sale.display_all_sales_product()

        elif(choice == '10'):
            break

        else:
            print("Please choose a valid option")