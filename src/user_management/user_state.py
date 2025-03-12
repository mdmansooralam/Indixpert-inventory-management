
state = None

class UserState:
    def __init__(self):
        self.__user = self.__load_state()

    def __load_state(self):
        if(state):
            return state
        else:
            return None

    def get_state(self):
        return self.__user
        
    def update_state(self, user):
        global state
        state = user
        self.__user = user
