
from src.user_management.manage_users import ManageUser
from src.utility.validation import *
from src.utility.check_user import check_user
from src.log_exception import log_exception

class UserFeatures(ManageUser):

    def signup(self):
        try:
            username = username_validate(input(f'Hint : no space allowed\nEnter username : '))
            if(not username):
                raise Exception('please enter a valid username')
            if(check_user(username)):
                raise Exception('uername already exists please choose another username')
            
            name =  name_validate(input('Enter Your Name : '))
            if(not name):
                raise Exception('please enter a valid name')
            
            role = role_validate(input('please enter role : '))
            if(not role):
                raise Exception('please choose a valid role and shuld be USER or ADMIN')
            
            password = password_validate(input(f'Hint : MinLength - 7 and should have lowercase uppercase symbol digit\nEnter Password : '))
            if(not password):
                raise Exception('please enter a valid password')
            
            self.user_signup(name, username, password, role)
        
        except Exception as error:
            log_exception(error)
            print(error)

    def login(self):
        try:
            username = username_validate(input(f'Enter username : '))
            if(not username):
                raise Exception('please enter a valid username : ')
            if(not check_user(username)):
                raise Exception('username not found please try again.....')
            
            password = password_validate(input(f'Enter Password : '))
            if(not password):
                raise Exception('please enter a valid password ..')
            
            self.login_user(username, password)

        except Exception as error:
            log_exception(error)
            print(error)

