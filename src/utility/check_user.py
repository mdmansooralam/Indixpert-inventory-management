from src.user_management.users import User

def check_user(username):
    users = User().users

    for user in users:
        if(user.username == username):
            return True
        break
    else:
        return False
