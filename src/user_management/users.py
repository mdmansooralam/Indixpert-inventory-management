import os
import json
from src.user_management.user_model import UserModel
from src.log_exception import log_exception
USERS_FILE = 'src/database/users.json'

class User:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        if(os.path.exists(USERS_FILE)):
            with open(USERS_FILE, 'r') as file:
                all_users = json.load(file)
                return [UserModel(**user) for user in all_users]
        else:
            return []
        
    def save_users(self):
        try:
            with open(USERS_FILE, 'w') as file:
                all_users = [user.__dict__ for user in self.users]
                json.dump(all_users, file, indent=4)

        except Exception as error:
            log_exception(error)
            print('database connection error')




