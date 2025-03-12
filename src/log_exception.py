import os
import datetime

LOG_FILE = 'src/exception_log.csv'

def log_exception(err):
    current_time = datetime.datetime.now()
    if(os.path.exists(LOG_FILE)):
        with open(LOG_FILE, 'a') as file:
            file.write(f'\n{current_time},{str(err)}')
    else:
        with open(LOG_FILE, 'w') as file:
            file.write(f'\nDate,Exception Message\n{current_time},{str(err)}')
            


