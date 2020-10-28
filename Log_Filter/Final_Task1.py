filename = 'access.2020-08-12_1900.log'

# Checking File existed or not
try:
    with open (filename, 'r') as fh:
        lines1 = fh.read ()
    print (filename, "is existed")
except Exception as err:
    print ('There was some error in the file operations.')
    print (err)

ip = []
getDictionary = {}
postDictionary = {}
with open(filename, 'r') as fh:
    lines = fh.readlines()

for i in lines:
    ip = i.split()[0]
    bytes = i.split()[9]
    ttype = i.split()[5]

    if str(ttype) == '"GET' and not getDictionary.__contains__(ip):
        getDictionary[ip] = int(bytes)

    elif getDictionary.__contains__ (ip) and str(ttype) == '"GET':
        getDictionary[ip] += int(bytes)

    if str(ttype) == '"POST' and not postDictionary.__contains__(ip):
        postDictionary[ip] = int(bytes)

    elif postDictionary.__contains__ (ip) and str(ttype) == '"POST':
        postDictionary[ip] += int(bytes)

for k,v in getDictionary.items():
    print("Host:", k, "\t GET Bytes:", v)

for k,v in postDictionary.items():
    print("Host:", k, "\t POST Bytes:", v)