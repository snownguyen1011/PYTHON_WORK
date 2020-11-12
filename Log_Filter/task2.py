import re
from datetime import date
import subprocess

filename = 'access.2020-11-01_1900.log'
filePattern = re.compile(r'(^(\baccess\b[.])(2?\d{4})[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])[_](\d{4})([.]\blog\b)$)')
ipPattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
ttypePattern = re.compile(r'\s\d{3}\s')
bytesPattern = re.compile(r'(\d*\d)$')
current_date = str(date.today())


# Step 1: Checking Filename format
try:
    if re.match(filePattern, filename) and filename.__contains__(current_date):
        print (" Filename pattern matched ")
    else:
        print (" Filename pattern not matched !!! :( ")
except Exception as err:
    print ('There was some error in the file operations.')
    print (err)

import os.path, time
print("last modified: %s" % time.ctime(os.path.getmtime(filename)))
print("created: %s" % time.ctime(os.path.getctime(filename)))

ip = []
getDictionary = {}
postDictionary = {}
logDatetime = []
ttype = []
bytes = []

imported_regexes =[]

with open(filename, 'r') as file:
    imported_regexes = file.readlines()
    for line in imported_regexes:
        print(re.findall(ttypePattern,line))



# with open(filename, 'r') as fh:
#     for lines in fh.readlines():
#         # print(re.findall('\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b', lines))
#         # print(re.match("83.167.113.100", lines))
#         ip.append(ipPattern.findall(str(lines)))
#         ip.extend(ttypePattern.findall(str(lines)))
#         ip.extend(bytesPattern.findall((str(lines))))
#         print(ip)
        # print(type(lines))
        # ip = lines.split()[0]
        # bytes = lines.split()[9]
        # ttype = lines.split()[5]
    # logdatetime.append(i.split()[3].strip("["))
    # logdatetime.

    # if ttype.__contains__("500"):
    #     print(ip)
    # logline_date = i.split()[3]
    # print(logline_date)
#     ip = i.split()[0]
#     bytes = i.split()[9]
#     ttype = i.split()[5]
#
#     if str(ttype) == '"GET' and not getDictionary.__contains__(ip):
#         getDictionary[ip] = int(bytes)
#
#     elif getDictionary.__contains__ (ip) and str(ttype) == '"GET':
#         getDictionary[ip] += int(bytes)
#
#     if str(ttype) == '"POST' and not postDictionary.__contains__(ip):
#         postDictionary[ip] = int(bytes)
#
#     elif postDictionary.__contains__ (ip) and str(ttype) == '"POST':
#         postDictionary[ip] += int(bytes)
#
# for k,v in getDictionary.items():
#     print("Host:", k.ljust(15), "\t GET Bytes:", v)
#
# for k,v in postDictionary.items():
#     print("Host:", k.ljust(15), "\t POST Bytes:", v)








# subprocess.Popen(['/Users/ravirajakoineni/.pyenv/versions/3.7.9/bin/python', './hello.py'])