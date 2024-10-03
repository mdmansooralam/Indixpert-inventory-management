from src.user_management.users import User
from src.user_management.user_state import UserState
from src.utility.validation import *
from src.utility.check_user import check_user

def delete():
     delete_feature()
    

    

def delete_feature():
        try: 
            username = username_validate(input('Enter username : '))
            if(not username):
                raise Exception('please enter a valid username')
            if(not check_user(username)):
                raise Exception('username not found')
            delete_user(username)
        
        except Exception as error:
            print(error)

def delete_user(username):
        user_data = User()
        userstate = UserState().get_state()
        if(userstate.role == 'ADMIN'):
            for user in user_data.users:
                if(user.role == 'ADMIN'):
                    print('\nAdmin account cannot not be delete')
                elif(user.username == username):
                    user_data.users.remove(user)
                    print(user.username + ' removed successful')
                    user_data.save_users()
        elif(userstate.role == 'USER'):
            print('\nYou are not authorized for this operation')