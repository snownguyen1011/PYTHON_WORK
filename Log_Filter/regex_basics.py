import re
from datetime import date

filename = 'access.2020-11-01_1900.log'
filePattern = re.compile(r'(^(\baccess\b[.])(2?\d{4})[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])[_](\d{4})([.]\blog\b)$)')
ipPattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
ttypePattern = re.compile(r'\s\d{3}\s')
bytesPattern = re.compile(r'(\d*\d)$')
current_date = str(date.today())

imported_regexes =[]

with open(filename, 'r') as file:
    imported_regexes = file.readlines()
    print(type(imported_regexes))  #  Generates a list

# with open(filename, 'r') as file:
#     imported_regexes = file.read()
#     print(type(imported_regexes))  #  Generates a string

for line in imported_regexes:
    line.find(str(bytesPattern))
