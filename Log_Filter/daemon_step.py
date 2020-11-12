
# visit https://www.childs.be/blog/post/how-to-run-a-python-script-as-a-service-in-background-as-a-daemon for instructions
# uses https://raw.githubusercontent.com/metachris/python-posix-daemon/master/src/daemon2x.py

import time, os, sys, logging
from crontab import CronTab
from datetime import datetime
from daemon import daemonize


# define the crontab for 25 minutes past the hour every hour
entry = CronTab('5 * * * *')
# find the delay from when this was run (around 11:13AM)
job = entry.rs
# job = CronTab.
# job.minute.every (1)
entry.next(default_utc=False)

# '/Users/ravirajakoineni/.pyenv/versions/3.7.9/bin/python /Users/Files/PYTHON_WORK/Log_Filter/writeDate.py'
# # Logging
logging.basicConfig (filename='/Users/Files/PYTHON_WORK/Log_Filter/daemon-example.log',
                     filemode='a',
                     format='[%(asctime)s] %(message)s',
                     datefmt='%Y/%d/%m %H:%M:%S',
                     level=logging.INFO)

# help(CronTab)

# my_cron = CronTab()
# job = my_cron.new(command='/Users/ravirajakoineni/.pyenv/versions/3.7.9/bin/python /Users/Files/PYTHON_WORK/Log_Filter/writeDate.py')
# job.minute.every (1)
#
# my_cron.write ()


####################### DAEMON SCRIPT
# https://stackoverflow.com/questions/16420092/how-to-make-python-script-run-as-service
import sys
import time

from daemon import daemonize


class YourCode(object):
    def run(self):
        while True:
            time.sleep(1)


class MyDaemon(daemonize()):
    def run(self):
        # Or simply merge your code with MyDaemon.
        your_code = YourCode()
        your_code.run()


if __name__ == "__main__":
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)

#######################   DAEMON SCRIPT END