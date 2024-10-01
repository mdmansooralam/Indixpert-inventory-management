
from src.user_management.manage_users import ManageUser
from src.utility.validation import *
from src.utility.check_user import check_user

class UserFeatures(ManageUser):

    def signup(self):
        try:
            username = name_validate(input('Enter username : '))
            if(not username):
                raise Exception('please enter a valid username')
            if(check_user(username)):
                raise Exception('uername already exists please try again')
            
            name =  name_validate(input('Enter Your Name : '))
            if(not name):
                raise Exception('please enter a valid name')
            
            password = name_validate(input('Enter Password : '))
            if(not password):
                raise Exception('please enter a valid password')
            
            self.user_signup(name, username, password)
        
        except Exception as error:
            print(error)

    def login(self):
        try:
            username = name_validate(input('Enter username : '))
            if(not username):
                raise Exception('please enter a valid username : ')
            if(not check_user(username)):
                raise Exception('username not found please try again.....')
            
            password = name_validate(input('Enter Your Password : '))
            if(not password):
                raise Exception('please enter a valid password ..')
            
            self.login_user(username, password)

        except Exception as error:
            print(error)
