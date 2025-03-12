import re

def name_validate(name):

    pattern  = r"^[A-Za-z].*$"

    if(re.match(pattern, name)):
        return name.upper()
    else:
        return False

def price_validate(num):
    pattern = r'^[1-9]\d*$'
    if(re.match(pattern, num)):
        return float(num)
    else:
        return False

def quantity_validate(num):
    pattern = r'^[1-9]\d*$'
    if(re.match(pattern, num)):
        return int(num)
    else:
        return False
    
def id_validate(id):
    pattern = r"^[A-Za-z0-9]{4}$"
    if(re.match(pattern, id)):
        return id.upper()
    else:
        return False

def check_blank(string):
    pattern = r'^(?!-)\S'
    if(re.match(pattern, string)):
        return string.upper()
    else:
        return False
    
def password_validate(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{7,}$'
    if(re.match(pattern, password)):
        return password
    else:
        return False
    
def username_validate(username):
    pattern = r'^\S+$'
    if(re.match(pattern, username)):
        return username
    else:
        return False

def role_validate(role):
    if(role.upper() == 'USER' or role.upper() == 'ADMIN'):
        return role.upper()
    else:
        return False
