from src.utility.check_user import check_user
from src.user_management.users import User
from src.user_management.user_model import UserModel
from src.user_management.user_state import UserState
from src.dashboard.manage_dashboard import manage_dashboard
import uuid



class ManageUser(User):
    
    def user_signup(self, name, username, password, role):
        if(check_user(username)):
            print("username already exist please try again")
        elif(len(self.users)>=4):
            print("you can not signup users list is full..")
        else:
            id = str(uuid.uuid4())[:10]
            new_user = UserModel(id, name, username, password, role)
            self.users.append(new_user)
            self.save_users()
            print('signup successful \n Please login')

    def login_user(self, username, password):
        for user in self.users:
            if(user.username == username):
                if(user.password == password):  
                    UserState().update_state(user)
                    manage_dashboard()
                    break
                else:
                    print('username or password are wrong please try again')
                    break
        else:
            print('username not found')
