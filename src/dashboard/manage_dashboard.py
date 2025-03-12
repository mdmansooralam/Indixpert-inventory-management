from src.user_management.user_state import UserState
from src.dashboard.inventory_menu import inventory_menu
from src.dashboard.admin_dashboard import admin_dashboard
from src.dashboard.user_dashboard import user_dashboard


def manage_dashboard():
    user = UserState().get_state()
    if(user):
        if(user.role == 'ADMIN'):
            admin_dashboard()
        elif(user.role == "USER"):
            user_dashboard()

    
