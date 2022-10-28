from datetime import datetime 
import time

while(1):
    now = datetime.now()
    hour = '{:0>2}'.format(now.hour)
    minute = '{:0>2}'.format(now.minute)
    second = '{:0>2}'.format(now.second)
    clock = chr(16) + "   " + str(hour) + ":" + str(minute) + ":" + str(second) + "   " + chr(17) 
    print(clock, end="\r")
    time.sleep(0.5)
