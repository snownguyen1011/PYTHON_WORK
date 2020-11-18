import schedule
import datetime
import time

print("Testing Scheduler:", datetime.datetime.now().replace(microsecond=0))
# print(datetime.datetime.now().replace(microsecond=0))

def MINUTE():
    print ("Every Minute:", datetime.datetime.now ().replace (microsecond=0))

def SECOND():
    print ("Every Second:", datetime.datetime.now ().replace (microsecond=0))

schedule.every(1).minutes.do(MINUTE)
schedule.every(1).seconds.do(SECOND)

while True:
    schedule.run_pending()
    time.sleep(1)