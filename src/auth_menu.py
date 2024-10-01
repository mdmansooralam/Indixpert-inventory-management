
from src.user_management.user_features import UserFeatures


def authentication_menu():
    auth = UserFeatures()
    
    while True:
        print(f'\n\n**********************User Authentication*********************')
        print(f'-----------------------------------------------------------------------')
        print(f'1 LOGIN')
        print(f'2 SIGNUP')
        print(f'3 EXIT')
        print(f'********************************************************************\n')

        choice = input('Please Chooose Any Option : ')
        if(choice == '1'):
            auth.login()
            continue
        elif(choice == '2'):
            auth.signup()
        elif(choice == '3'):
            break
        else:
            print('Please Choose a valid option ')
            