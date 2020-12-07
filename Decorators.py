# a decorator is just a normal, boring function. It happens to be a function taking exactly one argument,
# which is itself a function. And when called, the decorator returns a different function.


######   DECORATOR EXAMPLE 1 DECLARATION #####
def printlog(func):
    def wrapper(arg):
        print('CALLING: {}'.format(func.__name__))
        return func(arg)
    return wrapper
######   TEST BLOCK 1 - STARTS #######
@printlog
def add(x):
    print(x + 2)

add(3)
######   TEST BLOCK 1 - ENDS #########

######   TEST BLOCK 2 - STARTS #######
def sub(x):
    print(x - 2)
sub = printlog(sub)

sub(5)
######   TEST BLOCK 2 - ENDS #########
######   DECORATOR EXAMPLE 2 DECLARATION #####
#A MUCH BETTER printlog.
def printlog_new(func):
    def wrapper(*args, **kwargs):
        print('CALLING: {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

######   TEST BLOCK 3 - STARTS #######
@printlog_new
def baz(x, y):
    print( x ** y)
    return x ** y

baz(3,2)
####### EXPECTING BELOW ERROR WITH PRINTLOG BUT NOT WITH PRINTLOG_NEW ####
# Traceback (most recent call last):
#   File "/Users/Files/PYTHON_WORK/Decorators.py", line 28, in <module>
#     baz(3,2)
# TypeError: wrapper() takes 1 positional argument but 2 were given
######   TEST BLOCK 3 - ENDS #########

######   TEST BLOCK 4 - STARTS #########
######   DECORATOR EXAMPLE 3 DECLARATION #####
# This is more sensible.
def enhanced_printlog_for_method(func):
    def wrapper(self, *args, **kwargs):
        print('CALLING: {} on object ID {}'.format( func.__name__, id(self)))
        return func(self, *args, **kwargs)
    return wrapper


class Invoice:
    def __init__(self, id_number, total):
        self.id_number = id_number
        self.total = total
        self.owed = total
    @enhanced_printlog_for_method
    def record_payment(self, amount):
        self.owed -= amount
        print(self.owed)

inv = Invoice(42, 117.55)
print("ID of inv: {}".format(id(inv)))
inv.record_payment(55.2)

######   TEST BLOCK 4 - ENDS #########