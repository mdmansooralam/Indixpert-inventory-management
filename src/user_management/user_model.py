
class UserModel:
    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name
        self.username = username
        self.password = password

    def __str__(self):
        return {"id":{self.id}, "name":{self.name}, "username":{self.username}, "password":{self.password}}