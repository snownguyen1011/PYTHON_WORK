import login
# import login.signup as signup
from login import *

print("===========self============\n")
for k in dict(globals()).keys():
    print(k)

print("===========login============\n")
for k in login.__dict__.keys():
    print(k)

signup('raja','123')

